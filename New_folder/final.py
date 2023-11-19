import sys,subprocess
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
    global instructions,lines,commands,numpass
    numpass = -1
    i=0
    while  i < len(instructions):
        
        if instructions[i][0] == 'halt':
            break  
        
        if lines != None:
            lines -=1
            if lines == 0:
                break
        if numpass == -1 or i == int(numpass)-1:
            numpass = funCommands(instructions[i])
          
        i+=1  
    code.write('\n{a}()'.format(a=list(temp)[-1]))
    code.close()
    return
 
 
 
name =''
counter,totalSpace=0,0
code = open('finalCode.py','w+')
listOfCode,par = [],[]   

def funCommands(i):
    global counter,name,code,par,totalSpace
    
    if i[0] == 'begin_block':
        totalSpace = readTable(counter)
        code.write(totalSpace*'\t'+'def {func}():\n'.format(func=i[1]))
        name = i[1]
        totalSpace+=1   
        
    elif i[0] == ':=':
        code.write(totalSpace*'\t'+'{c} = {a}\n'.format(a=i[-1],c=i[1]))
        
        if i[1] in temp[name] and temp[name][i[1]]!=0:
         temp[name][i[-1]] = temp[name][i[1]]
        else:
          temp[name][i[-1]] = checkString(i[1])  
            
    elif i[0] == '+':
        code.write(totalSpace*'\t'+'{c} = {a} + {b}\n'.format(a=i[1],b=i[2],c=i[3]))
        temp[name][i[-1]]  = temp[name][i[1]] + temp[name][i[2]]
        
    elif i[0] == '/':
        code.write(totalSpace*'\t'+'{c} = {a} / {b}\n'.format(a=i[1],b=i[2],c=i[3]))
        temp[name][i[-1]]  = temp[name][i[1]] / temp[name][i[2]]
        
    elif i[0] == '-':
        code.write(totalSpace*'\t'+'{c} = {a} - {b}\n'.format(a=i[1],b=i[2],c=i[3]))
        temp[name][i[-1]]  = temp[name][i[1]] - temp[name][i[2]]
        
    elif i[0] == '*':
        code.write(totalSpace*'\t'+'{c} = {a} * {b}\n'.format(a=i[1],b=i[2],c=i[3]))
        temp[name][i[-1]]  = temp[name][i[1]] * temp[name][i[2]]
        
    elif i[0] == 'out':
        code.write(totalSpace*'\t'+'print({c})\n'.format(c=i[1]))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        temp[name][i[1]]  = checkString(temp1)
        code.write(totalSpace*'\t'+'{a} = {b}\n'.format(a=i[1],b=temp1))
        
    elif i[0] == 'retv':
        code.write(totalSpace*'\t'+'return {d}\n\n'.format(d=i[1]))
        
    elif i[0] == 'end_block':
        counter+=1
        listOfCode.append(code)
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or  i[0] == '!=' :
        if i[0] == '=':
            code.write(totalSpace*'\t'+'if {a} {b} {c}:\n'.format(a=i[1],b='==',c=i[2]))
        else:
            code.write(totalSpace*'\t'+'if {a} {b} {c}:\n'.format(a=i[1],b=i[0],c=i[2]))
        totalSpace+=1
        return i[3]
        
    elif i[0] == 'par':
        if i[2] == 'RET':
            code.write(totalSpace*'\t'+'{a} = '.format(a=i[1]))
        else:
            par.append(i[1])
            
    elif i[0] == 'call':
        c = ''
        for j in par:
            c +='{j},'.format(j=j)
        c = c.strip(',')
        code.write('{a}({b})\n'.format(a=i[1],b=c))
        
        new_line = 'def {a}({b}):\n'.format(a=i[1],b=c)
        
        code.seek(0)
        file = code.readlines()
        temporary = 'def {a}():\n'.format(a=i[1])
        for line in file:            
            if temporary in line:
                file[file.index(line)] = new_line
        
        code.seek(0)
        code.writelines(file) 
        code.seek(code.tell()) 
        par = []
    
        
    elif i[0] == 'jump':
        totalSpace-=1
        code.write(totalSpace*'\t'+'else:\n')
        totalSpace+=1
        
    
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
    subprocess.run(['python', 'finalCode.py'])
    if breakpoint != 'None':
        printTable()
    print(temp)
