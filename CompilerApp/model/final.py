import sys,os,re

name,programName= '',''
flag1=0
returnedValue = ()
instructions,table,parameters,previousName=[],[],[],[]
results,par = {},{}

pathInt = os.path.join('..', 'inputFiles', 'intFile.int')
pathTxt = os.path.join('..', 'inputFiles', 'txtFile.txt')

try:
    file = open(pathInt,'r')
except FileNotFoundError:
    print("Sorry, the file "+ pathInt + " does not exist.")

try:
    file1 = open(pathTxt,'r')
except FileNotFoundError:
    print("Sorry, the file "+ pathTxt + " does not exist.")

breakPoint = sys.argv[1]

def readIntermidiate():
    line = file.readline()
    while line!='':
        tempLine = re.split(',| ',line)
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
    parameters = []
    results[name] = {}
    nestingLevel = int(tempData['nestingLevel'])
    if nestingLevel == 0:
        programName = name
    for i in range(len(table[number])-1):
        data = eval(table[number][i])
        if data['type'] == 'Var':
            results[name][data['name']] = 0
        if data['type'] == 'Par':
                parameters.append((data['name'],data['parMode']))
    results[name]['Par'] =  parameters
    results[name]['nl'] = nestingLevel
  
def block():
    global instructions,lines
    
    begin = ['begin_block',programName]
    end = ['end_block',programName]
    i=instructions.index(begin)
    while  i <= instructions.index(end):
        if instructions[i][0] == 'halt': break

        z = funCommands(instructions[i])
        if z == lines:
            break

        if z!= -1:
            i=z
        else:
            i+=1
           
    return z

def funCommands(i):
    global name,par,returnedValue,programName,flag1,lines
    
    if i[0] == 'begin_block':
        name = i[1]

    elif i[0] == ':=':
        temp = checkString(i[1])
        
        for dict in results:
            if name == dict: flag1=1
            if  flag1==1 and i[-1] in results[dict]:
                flag1=0
                if type(temp) is str:
                    for dict1 in results:
                        if name == dict1: flag1=1
                        if flag1==1 and i[1] in results[dict1]:
                            results[dict][i[-1]] = results[dict1][i[1]] 
                            break
                        elif flag1==1 and results[dict1]['nl'] == 1:
                            results[dict][i[-1]] = results[programName][i[1]] 
                            break
                    break
                else:
                    results[dict][i[-1]] = temp
                    break
                
            elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                flag1=0
                if type(temp) is str:
                    for dict1 in results:
                        if name == dict1: flag1=1
                        if flag1==1 and i[1] in results[dict1]:
                            results[programName][i[-1]] = results[dict1][i[1]] 
                            break
                        elif flag1==1 and results[dict1]['nl'] == 1:
                            results[programName][i[-1]] = results[programName][i[1]] 
                            break
                    break
                else:
                    results[programName][i[-1]] = temp
                    break
                
                
            
        flag1=0
                        
    if i[0] == '+' or i[0] == '/' or i[0] == '-' or i[0] == '*':
        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[1] in results[dict]:
                    op1 = results[dict][i[1]]
                    break
                elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                    op1 = results[programName][i[1]]
                    break
                
        flag1=0

        if type(op2) is str:
            for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[2] in results[dict]:
                    op2 = results[dict][i[2]]
                    break
                elif flag1==1 and i[2] not in results[dict] and results[dict]['nl'] == 1:
                    op2 = results[programName][i[2]]
                    break
              
        flag1=0
        
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
            for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[1] in results[dict]:
                    temp = results[dict][i[1]]
                    break
                elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                    temp =  results[programName][i[1]]
                    break
            flag1=0
                
        print('The value of {a} is {b}'.format(a=i[1],b=temp))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        temp1 = checkString(temp1)
        for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[1] in results[dict]:
                    results[dict][i[1]] = temp1
                    break
                elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                    results[programName][i[1]] = temp1
                    break
        flag1=0
        
        
    elif i[0] == 'retv':
        if returnedValue != ():
            for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[1] in results[dict]:
                    results[returnedValue[0]][returnedValue[1]] = results[dict][i[1]]
                    break
                elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                    results[returnedValue[0]][returnedValue[1]] = results[programName][i[1]]
                    break
            flag1=0
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or i[0] == '<>' or i[0] == '<=' or i[0] == '>=':

        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            for dict in results:
                if name == dict: flag1=1
                if flag1==1 and i[1] in results[dict]:
                    op1 = results[dict][i[1]]
                    break
                elif flag1==1 and i[1] not in results[dict] and results[dict]['nl'] == 1:
                    op1 =  results[programName][i[1]]
                    break
            flag1=0
            

        if type(op2) is str:
            for dict in results:
                if name == dict: flag1=1
                if  flag1==1 and i[2] in results[dict]:
                    op2 = results[dict][i[2]]
                    break
                elif flag1==1 and i[2] not in results[dict] and results[dict]['nl'] == 1:
                    op2 =  results[programName][i[2]]
                    break
            flag1=0
       
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
            returnedValue = (name,i[1])
        else:
            if name not in par:
                parameters.clear()
            parameters.append((i[1],i[2])) 
            par[name] = parameters 
    elif i[0] == 'jump':
        return int(i[-1])-1   
    
    elif i[0] == 'call':
        previousName.append(name)
        a=0
        if name in par:
            for parameter in par[name]:
                results[i[1]][results[i[1]]['Par'][a][0]] = results[name][parameter[0]]
                a+=1

        begin = ['begin_block',i[1]]
        end = ['end_block',i[1]]
        j=instructions.index(begin)
        while j <= instructions.index(end):
            z = funCommands(instructions[j])
            if z!= -1:
                j=z
            else:
                j+=1

            if lines==j: return j

        name = previousName[-1]  
        
        a=0  
        if name in par:
            for parameter in par[name]:
                if parameter[1] == 'REF':
                    results[name][parameter[0]] = results[i[1]][results[i[1]]['Par'][a][0]]
                a+=1
               
            del par[name]
        previousName.pop()
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
            
def printTable(line):
    print('-')
    print('Line in Intermidiate Code:',line+1,'\n')
    for dict in results:
        print(dict,results[dict])
        
def checkBreakpoint():
    global lines,breakPoint
    
    if breakPoint != 'None':
        lines = int(breakPoint)-1
    else:
        lines = None        


if __name__ == '__main__':
    readIntermidiate()
    checkBreakpoint()
    for i in range(len(table)):
        readTable(i)
    line = block()
    for dict in results:
        del results[dict]['nl']
        del results[dict]['Par']
    if breakPoint != 'None':
        printTable(line)

    