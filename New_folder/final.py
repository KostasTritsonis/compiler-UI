import sys

name,programName,currentName= '','',''
returnedValue,flag=0,0
par,instructions,table =[],[],[]
results = {}

file = open('intFile.int','r')
file1 = open('txtFile.txt','r')
breakPoint = sys.argv[1]

def readIntermidiate():
    line = file.readline()
    while line!='':
        tempLine = line.split(' ')
        tempLine.remove('\n')
        tempLine = list(filter(('_').__ne__, tempLine))
        instructions.append(tempLine)
        line = file.readline()

    fileContents = file1.read() 
    lines = fileContents.strip().split('-')
    del lines[-1]
    for i in range(len(lines)):
        temp = lines[i].split("\n")
        if temp[0] == '':
            del temp[0]
        if temp[-1] == '':
            del temp[-1]
        table.append(temp)
    
    file.close()
    file1.close()

def readTable(number):
    global programName
    tempData = eval(table[number][-1])
    name = tempData['name']
    results[name] = {}
    nestingLevel = int(tempData['nestingLevel'])
    if nestingLevel == 0:
        programName = name
    for i in range(len(table[number])-1):
        data = eval(table[number][i])
        if data['type'] == 'Var': 
            results[name][data['name']] = 0
        if data['type'] == 'function' or data['type'] == 'procedure':
            results[name][data['name']] = results[data['name']]

  
def block():
    global instructions,lines,flag
    flag = 0
    i=0
    while  i < len(instructions):
        if instructions[i][0] == 'halt':
            break 

        if lines != None:
            lines -=1
            if lines == 0:
                break
        if programName == instructions[i][1]:
            flag = 1  
        if flag == 1:
            z = funCommands(instructions[i])
            if z!= -1:
                i=z
            else:
                i+=1
        else:
            i+=1
        
    return 

def funCommands(i):
    global name,par,returnedValue,programName,currentName

    if i[0] == 'begin_block':
        name = i[1]

    elif i[0] == ':=':
        temp = checkString(i[1]) 

        if type(temp) is str:

            if (i[1] not in results[programName]) and (i[1] not in results[name]):
                return -1
        
            if (i[1]  in results[programName]) and (i[1] not in results[name]):

                if (i[-1] in results[programName]) and (i[-1] not in results[name]):
                    results[programName][i[-1]] = results[programName][i[1]]
                else:
                    results[name][i[-1]] = results[programName][i[1]]
            else:
                if (i[-1] in results[programName]) and (i[-1] not in results[name]):
                    results[programName][i[-1]] = results[name][i[1]]
                else:
                    results[name][i[-1]] = results[name][i[1]]
        else:
            if (i[-1] in results[programName]) and (i[-1] not in results[name]):
                results[programName][i[-1]] = temp
            else:
                results[name][i[-1]] = temp

    if i[0] == '+' or i[0] == '/' or i[0] == '-' or i[0] == '*':
        op1 = checkString(i[1])
        op2 = checkString(i[2])

        
        
        if (i[-1] in results[programName]) and (i[-1] not in results[name]):

            if type(op1) is str:
                if (i[1] not in results[programName]) and (i[1] not in results[name]):
                    return -1
                if (i[1] in results[programName]) and (i[1] not in results[name]):
                    op1 = results[programName][i[1]]
                else:
                    op1 = results[name][i[1]]

            if type(op2) is str:
                if (i[2] not in results[programName]) and (i[2] not in results[name]):
                    return -1
                if (i[2] in results[programName]) and (i[2] not in results[name]):
                    op2 = results[programName][i[2]]
                else:
                    op2 = results[name][i[2]]

            if i[0] == '+':
               results[programName][i[-1]]  = op1 + op2
                
            elif i[0] == '/':
                if op1 != 0 and op2 != 0:
                    results[programName][i[-1]]  = op1 / op2
                
            elif i[0] == '-':
                results[programName][i[-1]]  = op1 - op2
                
            elif i[0] == '*':
                results[programName][i[-1]]  = op1 * op2
        else:

            if type(op1) is str:
                if (i[1] not in results[programName]) and (i[1] not in results[name]):
                    return -1
                if (i[1] in results[programName]) and (i[1] not in results[name]):
                    op1 = results[programName][i[1]]
                else:
                    op1 = results[name][i[1]]

            if type(op2) is str:
                if (i[2] not in results[programName]) and (i[2] not in results[name]):
                    return -1
                if (i[2] in results[programName]) and (i[2] not in results[name]):
                    op2 = results[programName][i[2]]
                else:
                    op2 = results[name][i[2]]

            if i[0] == '+':
                results[name][i[-1]]  = op1 + op2
                
            elif i[0] == '/':
                if op1 != 0 and op2 != 0:
                    results[name][i[-1]]  = op1 / op2
                
            elif i[0] == '-':
                results[name][i[-1]]  = op1 - op2
                
            elif i[0] == '*':
                results[name][i[-1]]  = op1 * op2



    elif i[0] == 'out':

        temp = checkString(i[1]) 

        if type(temp) is str:
            if (i[1] not in results[programName]) and (i[1] not in results[name]):
                return -1
            
            if (i[1]  in results[programName]) and (i[1] not in results[name]):
                temp = results[programName][i[1]]
            else:
                temp = results[name][i[1]]
                
        print('The value of {a} is {b}'.format(a=i[1],b=temp))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        if (i[1] not in results[programName]) and (i[1] not in results[name]):
                return -1
        
        if (i[1] in results[programName]) and (i[1] not in results[name]):
            results[programName][i[1]]  = checkString(temp1)
        else:
            results[name][i[1]]  = checkString(temp1)
        
    elif i[0] == 'retv':
        if returnedValue != 0:
            if (i[1] not in results[programName]) and (i[1] not in results[name]):
                return -1
            
            if (i[1] in results[programName]) and (i[1] not in results[name]):
                results[currentName][returnedValue] = results[programName][i[1]]
            else:
                results[currentName][returnedValue] = results[name][i[1]]
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or i[0] == '<>' or i[0] == '<=' or i[0] == '>=':

        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            if (i[1] not in results[programName]) and (i[1] not in results[name]):
                return -1
            
            if (i[1] in results[programName]) and (i[1] not in results[name]):
                op1 = results[programName][i[1]]
            else:
                op1 = results[name][i[1]]
            

        if type(op2) is str:
            if (i[2] not in results[programName]) and (i[2] not in results[name]):
                return -1
            
            if (i[2] in results[programName]) and (i[2] not in results[name]):
                op2 = results[programName][i[2]]
            else:
                op2 = results[name][i[2]]
       
        if i[0] == '=':
            if op1 == op2:
                return int(i[-1])-1
        elif i[0] == '<':
            if op1 < op2:
                return int(i[-1])-1
        elif i[0] == '>':
            if op1 > op2:
                return int(i[-1])-1   
        elif i[0] == '<>':
            if op1 != op2:
                return int(i[-1])-1
        elif i[0] == '<=':
            if op1 <= op2:
                return int(i[-1])-1
        elif i[0] == '>=':
            if op1 >= op2:
                return int(i[-1])-1
                
    elif i[0] == 'par':
        if i[2] == 'RET':
            returnedValue = i[1]
        else:
            par.append([i[1],i[2]])  
    
    elif i[0] == 'jump':
        return int(i[-1])-1   
    
    elif i[0] == 'call':
        currentName = i[1]
        if i[1] not in results:
            print('There is not function with name:',i[1])
            exit(1)

        for parameter in par:
            results[i[1]][parameter[0]] = results[name][parameter[0]]

        begin = ['begin_block',i[1]]
        end = ['end_block',i[1]]
        j=instructions.index(begin)
        while j < instructions.index(end):
            z = funCommands(instructions[j])
            if z!= -1:
                j=z
            else:
                j+=1

        for parameter in par:
            if parameter[1] == 'REF':
                results[name][parameter[0]] = results[i[1]][parameter[0]]
                    

        par = []
    
    return -1


def checkString(string):
    if string.isdigit():
        return int(string)
    else:
        try: 
            float(string)
            return float(string)
        except ValueError:
            return string
            
def printTable():
    print('-')
    for key, value in results.items():
        print(key, ":", value)
        
def checkBreakpoint():
    global lines,breakPoint
    
    if breakPoint != 'None':
        breakPoint = int(breakPoint)
        lines = breakPoint+1
    else:
        lines = None        


if __name__ == '__main__':
    readIntermidiate()
    checkBreakpoint()
    for i in range(len(table)):
        readTable(i)
    block()
    if breakPoint != 'None':
        printTable()
    print(results[programName])