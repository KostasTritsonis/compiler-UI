import sys
instructions,table = [],[]
results,commands,temp = {},{},{}


f = open('intFile.int','r')
f1 = open('txtFile.txt','r')
breakpoint = "None"   

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
    for i in range(len(table[number])-1): 
        data = eval(table[number][i])
        temp[name][data['name']] = 0
    
    
    
def block():
    global instructions,lines,commands

    for i in instructions:
        if lines != None:
            lines -=1
            if lines == 0:
                break
        funCommands(i)
        
        if i[0] == 'halt':
            break  
    return
    


name =''
counter=0
code = ''
listOfCode = []
def funCommands(i):
    global counter,name,code
    if i[0] == 'begin_block':
        code += 'def {func}():\n'.format(func=i[1])
        readTable(counter)
        name = i[1]
    if i[0] == ':=':
        if i[1] in temp[name] and temp[name][i[1]]!=0:
         temp[name][i[-1]] = temp[name][i[1]]
        else:
          temp[name][i[-1]] = checkString(i[1])
    elif i[0] == '+':
        code+= '\t{a} + {b}\n'.format(a=temp[name][i[1]],b=temp[name][i[2]])
        temp[name][i[-1]]  = temp[name][i[1]] + temp[name][i[2]]
    elif i[0] == '/':
        code+= '\t{a} / {b}\n'.format(a=temp[name][i[1]],b=temp[name][i[2]])
        temp[name][i[-1]]  = temp[name][i[1]] / temp[name][i[2]]
    elif i[0] == '-':
        code+= '\t{a} - {b}\n'.format(a=temp[name][i[1]],b=temp[name][i[2]])
        temp[name][i[-1]]  = temp[name][i[1]] - temp[name][i[2]]
    elif i[0] == '*':
        code+= '\t{a} * {b}\n'.format(a=temp[name][i[1]],b=temp[name][i[2]])
        temp[name][i[-1]]  = temp[name][i[1]] * temp[name][i[2]]
    elif i[0] == 'out':
        code+= '\tprint({c})\n'.format(c=temp[name][i[1]])
        print (temp[name][i[1]])
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        temp[name][i[1]]  = checkString(temp1)
    elif i[0] == 'retv':
        code+='\treturn {d}\n\n'.format(d=temp[name][i[1]])
    elif i[0] == 'end_block':
        counter+=1
        listOfCode.append(code)
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or  i[0] == '!=':
        code+= '\tif {a} {b} {c}:\n'.format(a=i[1],b=i[0],c=i[2])
  
    
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
    print(code)

