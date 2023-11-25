import sys
instructions,table = [],[]
results,commands,temp = {},{},{}

f = open('intFile.int','r')
f1 = open('txtFile.txt','r')
breakpoint = 'None' 

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
        temp1 = lines[i].split("\n")
        if temp1[0] == '':
            del temp1[0]
        if temp1[-1] == '':
            del temp1[-1]
        table.append(temp1)
    
    f.close()
    f1.close()

def readTable(number):
    data = eval(table[number][-1])
    name = data['name']
    temp[name] = {}
    totalSpace = int(data['nestingLevel'])
    for i in range(len(table[number])-1): 
        data = eval(table[number][i])
        temp[name][data['name']] = 1
    return totalSpace
    
    
    
def block():
    global instructions,lines,commands
    
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
            i=int(j)
        else:
            i+=1  
    return
 
 
 
name= ''
counter,totalSpace=0,0
par,code =[],[]
listofCode = {}   

def funCommands(i):
    global counter,name,par,totalSpace,code,return1
    code.append(i)
    if i[0] == 'begin_block':
        totalSpace = readTable(counter)
       
        name = i[1]
        totalSpace+=1       
    elif i[0] == ':=':
        if i[1] in temp[name] and temp[name][i[1]]!=0:
         temp[name][i[-1]] = temp[name][i[1]]
        else:
          temp[name][i[-1]] = checkString(i[1])  
            
    elif i[0] == '+':
        temp[name][i[-1]]  = temp[name][i[1]] + temp[name][i[2]]
        
    elif i[0] == '/':
        temp[name][i[-1]]  = temp[name][i[1]] / temp[name][i[2]]
        
    elif i[0] == '-':
        temp[name][i[-1]]  = temp[name][i[1]] - temp[name][i[2]]
        
    elif i[0] == '*':
        temp[name][i[-1]]  = temp[name][i[1]] * temp[name][i[2]]
        
    elif i[0] == 'out':
       print(temp[name][i[1]])
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        temp[name][i[1]]  = checkString(temp1)
        
    elif i[0] == 'retv':
        return1 =  temp[name][i[1]]
        
    elif i[0] == 'end_block':
        del code[0]
        del code[-1]
        listofCode[name] = code
        counter+=1
        code=[]
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or  i[0] == '!=' :
        return i[-1]
        
    elif i[0] == 'par':
            
        if i[2] == 'RET':
            temp[name][i[1]] = return1
        else:
            par.append(i[1])  
    
    elif i[0] == 'jump':
        return i[-1]   
    
    elif i[0] == 'call':
        for i in listofCode[i[1]]:
            funCommands(i)
             
   
          
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
    for key, value in commands.items():
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
    print(temp)
