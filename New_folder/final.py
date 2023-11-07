import sys
instructions = []
results = {}
commands = {}
temp = {}
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
    f.close()

def readTable():
    file_contents = f1.read() 
    lines = file_contents.split('\n') 
    data = eval(lines[-1])
    name = data['name']
    temp[name] = {}
    counter = 0
    for i in range(len(lines)-1): 
        data = eval(lines[i])
        temp[name][data['name']] = 0
        counter+=1
        if lines[i] == '-':
            break
    print(temp)
    
    
    
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
def funCommands(i):
    global name
    if i[0] == 'begin_block':
        readTable()
        name = i[1]
        
    if i[0] == ':=':
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
        print (temp[name][i[1]])
    elif i[0] == 'inp':
        print("Give input:")
        temp1 =  sys.stdin.readline().strip()
        temp[name][i[1]]  = checkString(temp1)
    elif i[0] == 'retv':
        return temp[name][i[1]]
    
  
    
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

