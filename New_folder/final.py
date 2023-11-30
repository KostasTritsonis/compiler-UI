import sys

name,currentName= '',''
counter,returnedValue=0,0
par,code,instructions,table =[],[],[],[]
listofCode,results,globalVariables = {},{},{}

f = open('intFile.int','r')
f1 = open('txtFile.txt','r')
breakpoint = sys.argv[1]

def readIntermidiate():
    lread = f.readline()
    while lread!='':
        lread1 = lread.split(' ')
        lread1.remove('\n')
        lread1 = list(filter(('_').__ne__, lread1))
        instructions.append(lread1)
        lread = f.readline()

    file_contents = f1.read() 
    lines = file_contents.strip().split('-')
    del lines[-1]
    for i in range(len(lines)):
        tmp = lines[i].split("\n")
        if tmp[0] == '':
            del tmp[0]
        if tmp[-1] == '':
            del tmp[-1]
        table.append(tmp)
    
    f.close()
    f1.close()

def readTable(number):
    tempData = eval(table[number][-1])
    name = tempData['name']
    results[name] = {}
    nestingLevel = int(tempData['nestingLevel'])
    for i in range(len(table[number])-1):
        data = eval(table[number][i])
        if nestingLevel == 0 and data['type'] == 'Var':
            globalVariables[data['name']] = 0 
        results[name][data['name']] = 0
    results[name]['nestingLevel'] = nestingLevel

       
def block():
    global instructions,lines

    i=0
    while  i < len(instructions):
        if instructions[i][0] == 'halt':
            break  
        
        if lines != None:
            lines -=1
            if lines == 0:
                break
       
        j = funCommands(instructions[i])
        if j!=-1:
            i=j
        else:
            i+=1  
    return 

def funCommands(i):
    global counter,name,par,code,returnedValue,currentName

    code.append(i)
    if i[0] == 'begin_block':
        readTable(counter)
        name = i[1]   

    elif i[0] == ':=':
        temp = checkString(i[1]) 

        if type(temp) is str:
            results[name][i[-1]] = results[name][i[1]]
        else:
            results[name][i[-1]] = temp 

    if i[0] == '+' or i[0] == '/' or i[0] == '-' or i[0] == '*':

        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            op1 = results[name][i[1]]

        if type(op2) is str:
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
            temp = results[name][i[1]]

        print('The value of {a} is {b}'.format(a=i[1],b=temp))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        results[name][i[1]]  = checkString(temp1)
        
    elif i[0] == 'retv':
        if returnedValue != 0:
            results[currentName][returnedValue] = results[name][i[1]]
        
    elif i[0] == 'end_block':
        del code[0]
        del code[-1]
        listofCode[name] = code
        counter+=1
        code=[]
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>':

        temp1 = checkString(i[1])
        temp2 = checkString(i[2])

        if type(temp1) is str:
            temp1 = results[name][i[1]]

        if type(temp2) is str:
            temp2 = results[name][i[2]]
       
        if i[0] == '=':
            if temp1 == temp2:
                return int(i[-1])-1
        elif i[0] == '<':
            if temp1 < temp2:
                return int(i[-1])-1
        elif i[0] == '>':
            if temp1 > temp2:
                return int(i[-1])-1
                
    elif i[0] == 'par':
        if i[2] == 'RET':
            returnedValue = i[1]
        else:
            par.append([i[1],i[2]])  
    
    elif i[0] == 'jump':
        return int(i[-1])-1   
    
    elif i[0] == 'call':
        currentName = name

        if i[1] not in results:
            print('There is not function with name:',i[1])
            exit(1)

        for parameter in par:
            if parameter[1] == 'CV':
                for variable in results[i[1]].keys():
                    if variable == parameter[0]:
                        results[i[1]][variable] = results[name][variable]

        name = i[1]
        for j in listofCode[i[1]]:
            funCommands(j)

        name = currentName
        for parameter in par:
            if parameter[1] == 'REF':
                for variable in results[i[1]].keys():
                    if variable == parameter[0]:
                        results[name][variable] = results[i[1]][variable]

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
    global lines,breakpoint
    
    if breakpoint != 'None':
        breakpoint = int(breakpoint)
        lines = breakpoint+1
    else:
        lines = None        


if __name__ == '__main__':
    readIntermidiate()
    checkBreakpoint()
    block()
    if breakpoint != 'None':
        printTable()
