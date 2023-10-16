import sys,os
instructions = []
results = {}
f = open(sys.argv[1],'r')
breakpoint = sys.argv[2]
    
lread = f.readline()
while lread!='':
    lread1 = lread.split(' ')
    lread1.remove('\n')
    lread1 = list(filter(('_').__ne__, lread1))
    instructions.append(lread1)
    lread = f.readline()
f.close()
    
def block():
    global instructions,lines
    for i in instructions:
        if lines != None:
            lines -=1
            if lines == 0:
                break
        if i[0] == ':=':
            if i[1] in results:
                results[i[-1]] = results[i[1]]
            else:
                results[i[-1]] = checkString(i[1])
        elif i[0] == '+':
            results[i[-1]] = results[i[1]] + results[i[2]]
        elif i[0] == '/':
            results[i[-1]] = results[i[1]] / results[i[2]]
        elif i[0] == '-':
            results[i[-1]] = results[i[1]] - results[i[2]]
        elif i[0] == '*':
            results[i[-1]] = results[i[1]] * results[i[2]]
        elif i[0] == 'out':
            print(results[i[1]])
        elif i[0] == 'halt':
            break
        elif i[0] == 'inp':
            print("Give input:")
            temp =  sys.stdin.readline().strip()
            results[i[1]] = checkString(temp)
    return
        
    
    
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
    for key, value in results.items():
        print(key, ":", value)
        
        
if breakpoint != 'None':
    breakpoint = int(breakpoint)
    lines = breakpoint+1
else:
    lines = None 
       
block()
if breakpoint != 'None':
    print('-')
    printTable()

       
