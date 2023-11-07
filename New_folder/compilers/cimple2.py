import sys
global listofquads,cp

f=open(sys.argv[1],'r')
line=1
listofquads = []
listoftemp = []
listofscopes = []
parameters = []
countq = 1
variableT = 0

#conditions
Cstart=0
Cdigit=1
Cidk=2
Csmaller=3
Clarger=4
Casgn=5
Ccom=6

#characters
idk=0
dig=1
plus=2
minus=3
mult=4
div=5
smaller=6
larger=7
eq=8
gquestion_mark=9
comma=10
colon=11
lbracket=12
rbracket=13
lquotation_mark=14
rquotation_mark=15
lblock=16
rblock=17
dot=18
hashtag=19
white_char=20
change_line=21
EOF=22
other=23

#Tokens
idk_tk=100
dig_tk=101
plus_tk=102
minus_tk=103
mult_tk=104
div_tk=105
smaller_tk=106
larger_tk=107
eq_tk=108
gquestion_mark_tk=109
comma_tk=110
colon_tk=111
lbracket_tk=112
rbracket_tk=113
lquotation_mark_tk=114
rquotation_mark_tk=115
lblock_tk=116
rblock_tk=117
lessorequal_tk=118
greaterorequal_tk=119
notequal_tk=120
assign_tk=121
EOF_tk=122
dot_tk=123

program_tk=200
declare_tk=201
if_tk=202
else_tk=203
while_tk=204
switchcase_tk=205
forcase_tk=206
incase_tk=207
case_tk=208
default_tk=209
not_tk=210
and_tk=211
or_tk=212
function_tk=213
procedure_tk=214
call_tk=215
return_tk=216
in_tk=217
inout_tk=218
input_tk=219
print_tk=220

#Errors
Error_comandEOF=-1
Error_digitletter=-2
Error_other=-3
Error_outofboundaries=-4
Error_over30=-5
Error_assign=-6


#Tables
num = ['0','1','2','3','4','5','6','7','8','9']
alph = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
reserved_words = ['program','declare','if','else','while','switchcase','forcase','incase','case','default','not','and','or','function','procedure','call','return','in','inout','input','print']


tables=[
    #Cstart
    [Cidk,Cdigit,plus_tk,minus_tk,mult_tk,div_tk,Csmaller,Clarger,eq_tk,gquestion_mark_tk,comma_tk,Casgn,
    lbracket_tk,rbracket_tk,lquotation_mark_tk,rquotation_mark_tk,lblock_tk,rblock_tk,dot_tk,Ccom,Cstart,Cstart,EOF_tk,Error_other],
    #Cdig
    [Error_digitletter,Cdigit,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,
    dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,dig_tk,Error_other],
    #Cidk
    [Cidk,Cidk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,idk_tk,
    idk_tk,idk_tk,idk_tk,idk_tk,Error_other],
    #Csmaller
    [smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,notequal_tk,lessorequal_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,
    smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,smaller_tk,Error_other],
    #Clarger
    [larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,greaterorequal_tk,larger_tk,larger_tk,larger_tk,larger_tk,
    larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,larger_tk,Error_other],
    #Casgn
    [Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,assign_tk,Error_assign,Error_assign,Error_assign,
    Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_assign,Error_other],
    #Ccom
    [Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Ccom,Cstart,Ccom,Ccom,Error_comandEOF,Ccom]

    ]




def checkerrors(error):

    if(error==Error_other):
        print("WARNING: Not an acceptable language symbol")
    elif(error==Error_over30):
        print("WARNING: The word's length is over 30") 
    elif(error==Error_outofboundaries):
        print("WARNING: Number out of the boundaries -(2^32-1),2^32-1 ")
    elif(error==Error_digitletter):
        print("WARNING: Letter after a number")
    elif(error==Error_assign):
        print("WARNING: Expected \"=\"  after \":\"")
    elif(error==Error_comandEOF):
        print("WARNING: Opened comment section  but not closed ") 
    return


def checkwords(cur):
    global word
    if(cur == idk_tk):
        if(word in reserved_words):
            if (word == 'program'):
                cur = program_tk
            elif (word == 'declare'):
                cur = declare_tk
            elif (word == 'if'):
                cur = if_tk
            elif (word == 'else'):
                cur = else_tk
            elif (word == 'while'):
                cur = while_tk
            elif (word == 'switchcase'):
                cur = switchcase_tk
            elif (word == 'forcase'):
                cur = forcase_tk
            elif (word == 'incase'):
                cur = incase_tk
            elif (word == 'case'):
                cur = case_tk
            elif (word == 'default'):
                cur = default_tk
            elif (word == 'not'):
                cur = not_tk
            elif (word == 'and'):
                cur = and_tk
            elif (word == 'or'):
                cur = or_tk
            elif (word == 'function'):
                cur = function_tk
            elif (word == 'procedure'):
                cur = procedure_tk
            elif (word == 'call'):
                cur = call_tk
            elif (word == 'return'):
                cur = return_tk
            elif (word == 'in'):
                cur = in_tk
            elif (word == 'inout'):
                cur = inout_tk 
            elif (word == 'input'):
                cur = input_tk
            elif (word == 'print'):
                cur = print_tk  
    return cur


def lex():
    global line,word
    word=''
    cur=Cstart
    counter=line
    results=[]
    while(cur>=0 and cur<=6):
        c = f.read(1)
        if(c in alph):
            c_tk = idk
        elif(c in num):
            c_tk = dig
        elif(c == '+'):
            c_tk = plus
        elif(c == '-'):
            c_tk = minus
        elif(c == '*'):
            c_tk = mult
        elif(c == '/'):
            c_tk = div
        elif(c == '<'):
            c_tk = smaller
        elif(c == '>'):
            c_tk = larger
        elif(c == '='):
            c_tk = eq
        elif(c == ';'):
            c_tk = gquestion_mark
        elif(c == ','):
            c_tk = comma
        elif(c == ':'):
            c_tk = colon
        elif(c == '['):
            c_tk = lbracket
        elif(c == ']'):
            c_tk = rbracket
        elif(c == '('):
            c_tk = lquotation_mark
        elif(c == ')'):
            c_tk = rquotation_mark
        elif(c == '{'):
            c_tk = lblock
        elif(c == '}'):
            c_tk = rblock
        elif(c == '.'):
            c_tk = dot
        elif(c == '#'):
            c_tk = hashtag
        elif(c == ' ' or c == '\t'):
            c_tk = white_char
        elif(c == '\n'):
            counter = counter+1
            c_tk = change_line
        elif(c == ''):  
            c_tk = EOF
        else:
            c_tk = other

        cur=tables[cur][c_tk]
        
        if(len(word)<30):
            if(cur!=Cstart and cur!=Ccom):
                word+=c
        else:
            cur=Error_over30

    if( cur==dig_tk or cur==idk_tk or cur==smaller_tk or cur==larger_tk ):
        if (c == '\n'):
            counter -= 1

        word = word[:-1]
        c=f.seek(f.tell()-1,0)

    if (cur == dig_tk):
        if (int(word)>= pow(2,32)):
            cur = Error_outofboundaries


    cur = checkwords(cur)
    checkerrors(cur)   
    results.append(cur)
    results.append(word)
    results.append(counter)
    line = counter
    return results


def nextquad():
    global countq

    return countq

def genquad(op,x,y,z):
    global countq,listofquads
    l = [nextquad()]
    l += [op]+[x]+[y]+[z]
    countq += 1 
    listofquads += [l]

    return l

def emptylist():

    listoflabel = []

    return listoflabel

def makelist(x):

    listoflabel1 = [x]

    return listoflabel1

def merge(list1,list2):

    list3 = []
    list3 += list1 + list2 

    return list3

def backpatch(list,z):
    global listofquads

    for i in range(len(list)):
        for j in range(len(listofquads)):
            if(list[i] == listofquads[j][0] and listofquads[j][4] == '_'):
                listofquads[j][4] = z

    return 

topScope = None

class Variable:
    def __init__(self):
        self.name = ''
        self.type=''
        self.offset = 0

class SubProgram():
    def __init__(self):
        self.name =''
        self.type = ''
        self.argument = []
        self.sQuad = 0
        self.framelength = 0

class TempVar():
    def __init__(self):
        self.name=''
        self.type = 'Temp'  
        self.offset = 0

class Parameter():
    def __init__(self):
        self.name=''
        self.type = 'Par'
        self.parMode = '' 
        self.offset = 0

class Scope():
    def __init__(self):
        self.name = ''
        self.entity = []
        self.nestingLevel = 0
        self.totalOffset = 12
        
def final_framelength():
    for e in topScope.entity:
        for a in listofscopes:
            if a.name == e.name:
                e.framelength = a.totalOffset 
            
def new_argument(obj):
    global topScope
    topScope.entity[-1].argument.append(obj[0])
    
def new_parameters(obj):
    global topScope
    parameters.append(obj)
              
def new_entity(obj):
    global topScope
    
    topScope.entity.append(obj)
    
def newtemp():
    global variableT,listoftemp

    l = ['T_']
    l.append(str(variableT))
    l=''.join(l)
    listoftemp+=[l]
    variableT += 1

    e = TempVar()                             
    e.type = 'Temp'                           
    e.name = l
    e.offset = topScope.totalOffset 
    topScope.totalOffset += 4                        
    new_entity(e)   

    return l

def new_scope(name):
    global topScope
    nextScope = Scope()
    nextScope.name = name
    nextScope.enScope = topScope
    if(topScope == None):
        nextScope.nestingLevel = 0
    else:
        nextScope.nestingLevel = topScope.nestingLevel + 1

    topScope = nextScope
    listofscopes.append(topScope)

def delete_scope():
    global topScope
    
    delScope = topScope
    topScope = topScope.enScope

    del delScope
    
def add_parameters():
    global topScope
    for a in parameters:
        e = Parameter()
        e.name = a[1]
        e.type = 'Par'
        e.parMode = a[0]
        e.offset = topScope.totalOffset
        topScope.totalOffset += 4
        new_entity(e)
    parameters.clear()   


def patchStart(quadNo):
    global listofscopes

    if len(listofscopes) < 2: return
    topScope.enScope.entity[-1].sQuad = quadNo

def write_Symbol_table():
    global topScope,cp
    scope=topScope
    final_framelength()
    for e in scope.entity:
        cp.write(str(vars(e))+"\n")
    scope.entity = []
    cp.write(str(vars(scope))) 
    scope = scope.enScope    



def syn():
    global line,lex1
    lex1 = lex()
    line = lex1[2]

    def program():
        global lex1,line

        if(lex1[0] == program_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk):
                token = lex1[1]
                lex1 = lex()
                line = lex1[2]
                block(token,-1)

                if(lex1[0] == dot_tk):
                    lex1 = lex()
                    line = lex1[2]
                    return

                else:
                    print("ERROR:The program needs \".\" to close in line ",line)
                    exit(1)

            else:
                print("ERROR:Missing programs name in line ",line)
                exit(1)

        else:
            print("ERROR:The program must start with the word \"program\" in line ",line)
            exit(1)

    def block(token,halt):
        new_scope(token)
        if halt != -1:
            add_parameters()
        patchStart(nextquad())
        declarations()
        subprograms()
        genquad('begin_block',token,'_','_')
        statements()
        if(halt == -1):
            genquad('halt','_','_','_')
        genquad('end_block',token,'_','_')
        write_Symbol_table()
        delete_scope()

    def declarations():
        global lex1,line

        while(lex1[0] == declare_tk):
            lex1 = lex()
            line = lex1[2]
            varlist()
            

            if(lex1[0] == gquestion_mark_tk):
                lex1 = lex()
                line = lex1[2]

            else:
                print("ERROR:There is not a \";\" after the variable in line ",line)
                exit(1)
        return

    def varlist():
        global lex1,line,topScope
        
        if(lex1[0] == idk_tk):
            
            e = Variable()                          
            e.type = 'Var'                       
            e.name = lex1[1] 
            e.offset = topScope.totalOffset
            topScope.totalOffset += 4
            new_entity(e) 
            
            lex1 = lex()
            line = lex1[2]
            
            while(lex1[0] == comma_tk):
                lex1 = lex()
                line = lex1[2]
                
                if(lex1[0] == idk_tk):

                    e = Variable()                          
                    e.type = 'Var'                       
                    e.name = lex1[1] 
                    e.offset = topScope.totalOffset
                    topScope.totalOffset += 4
                    new_entity(e)   

                    lex1 = lex()
                    line = lex1[2]

                else:
                    print("ERROR:There is not \",\" before variable  or between the variables in line ",line)
                    exit(1)
        return

    def subprograms():
        global lex1,listofscopes
        
        while(lex1[0] == function_tk or lex1[0] == procedure_tk):
            subprogram()
        return

    def subprogram():
        global lex1,line
        if(lex1[0] == function_tk):
            lex1 = lex()
            line = lex1[2]  
            if(lex1[0] == idk_tk):
                
                token = lex1[1]
                e = SubProgram()                                      
                e.name = token
                e.type = 'function'
                new_entity(e)
                
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    formalparlist()

                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        block(token,1)

                        return

                    else:
                        print("ERROR:There is not a \")\"  at line ",line)
                        exit(1)

                else:
                    print("ERROR:There is not a \"(\"  at line ",line)
                    exit(1)

            else:
                print("ERROR:Expected variable's name after function  at line",line)
                exit(1)

        elif(lex1[0] == procedure_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk):
                
                token = lex1[1]
                e = SubProgram()                                      
                e.name = token
                e.type = 'procedure'
                new_entity(e)
                 
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    formalparlist()

                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        block(token,1)
                        return

                    else:
                        print("ERROR:There is not a \")\"  at line ",line)
                        exit(1)

                else:
                    print("ERROR:There is not a \"(\"  at line ",line)
                    exit(1)

            else:
                print("ERROR:Expected variable after procedure  at line",line)
                exit(1)
        
    def formalparlist():
        global lex1,line
        formalparitem()

        while(lex1[0] == comma_tk):
            lex1 = lex()
            line = lex1[2]
            
            formalparitem()

        return

    def formalparitem():
        global lex1,line,topScope
        par = ()
        if(lex1[0] == in_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk): 
                
                par = ('cv',lex1[1])
                new_parameters(par)
                lex1 = lex()
                line = lex1[2]

            else:
                print("ERROR:Expected variable name after \"in\" in line ",line)
                exit(1)

        elif(lex1[0] == inout_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk):
                
                par = ('ref',lex1[1])
                new_parameters(par)
                lex1 = lex()
                line = lex1[2]

            else:
                print("ERROR:Expected variable name after \"inout\" in line ",line)
                exit(1)
        new_argument(par)
        return par

    def statements():
        global lex1,line

        if(lex1[0] == lblock_tk):
            lex1 = lex()
            line = lex1[2]
            statement()

            while(lex1[0] == gquestion_mark_tk):
                lex1 = lex()
                line = lex1[2]
                statement()

            if(lex1[0] == rblock_tk):
                lex1 = lex()
                line = lex1[2]
                return

            else:
                print("ERROR:Missing \"}\" in statements in line ",line)
                exit(1)

        else:
            
            statement()
            if(lex1[0] == gquestion_mark_tk):
                lex1 = lex()
                line = lex1[2]
                return

            else:
                print("ERROR:Expected \";\" after statement in line ",line)
                exit(1)

    def statement():
        global lex1 
        
        if(lex1[0] == idk_tk):
            assignStat()
        elif(lex1[0] == if_tk):
            ifStat()
        elif(lex1[0] == while_tk):
            whileStat()
        elif(lex1[0] == switchcase_tk):
            switchcaseStat()
        elif(lex1[0] == forcase_tk):
            forcaseStat()
        elif(lex1[0] == incase_tk):
            incaseStat()
        elif(lex1[0] == call_tk):
            callStat()
        elif(lex1[0] == return_tk):
            returnStat()
        elif(lex1[0] == input_tk):
            inputStat()
        elif(lex1[0] == print_tk):
            printStat()
        return

    def assignStat():
        global lex1,line
        token = lex1[1]
        if(lex1[0] == idk_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == assign_tk):
                lex1 = lex()
                line = lex1[2]
                E_place = expression()
                #{P1}
                genquad(':=',E_place,'_',token)

                return

            else:
                print("ERROR:Expected \":=\" after the variable name in line ",line)
                exit(1)

        else:
            print("ERROR:Expected name in line ",line)
            exit(1)

    def ifStat():
        global lex1,line

        if(lex1[0] == if_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]
                #{P1}
                B = condition()
                backpatch(B[0],nextquad())


                if(lex1[0] == rquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    statements()
                    #{P2}
                    
                    ifList = makelist(nextquad())
                    genquad('jump','_','_','_')
                    backpatch(B[1],nextquad())
                    elsepart()
                    #{P3}
                    backpatch(ifList,nextquad())
                    return

                else:
                    print("ERROR:Expected \")\" after condition in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"(\" after if statement in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the  \"if\" statement in line ",line)
            exit(1)

    def elsepart():
        global lex1,line

        if(lex1[0] == else_tk):
            lex1 = lex()
            line = lex1[2]
            statements()

        return

    def whileStat():
        global lex1,line

        if(lex1[0] == while_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]
                #{P1}
                Bquad = nextquad() 
                B = condition()
                #{P2}
                backpatch(B[0],nextquad())

                if(lex1[0] == rquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    statements()
                    #{P3}
                    genquad('jump','_','_',Bquad)
                    backpatch(B[1],nextquad())
                    return

                else:
                    print("ERROR:Expected \")\" after condition in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"(\" after while statement in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"while\" statement in line ",line)
            exit(1)

    def switchcaseStat():
        global lex1,line

        if(lex1[0] == switchcase_tk):
            lex1 = lex()
            line = lex1[2]
            #{P1}
            exitlist = emptylist()

            while(lex1[0] == case_tk):
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    B = condition()
                    #{P2}
                    backpatch(B[0],nextquad())

                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        statements()
                        #{P3}
                        e = makelist(nextquad())
                        genquad('jump','_','_','_')
                        exitlist = merge(exitlist,e)
                        backpatch(B[1],nextquad())

                        
                     
                    else:
                        print("ERROR:Expected \")\" after condition in line ",line)
                        exit(1)

                else:
                    print("ERROR:Expected \"(\" after case statement in line ",line)
                    exit(1)

            if(lex1[0] == default_tk):
                lex1 = lex()
                line = lex1[2]
                statements()
                backpatch(exitlist,nextquad())

            else:
                print("ERROR:An error occured during the \"default\"  in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"switchcase\"  in line ",line)
            exit(1)

    def forcaseStat():
        global lex1,line

        if(lex1[0] == forcase_tk):
            lex1 = lex()
            line = lex1[2]
            #{P1}
            Bquad = nextquad()

            while(lex1[0] == case_tk):
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    B = condition()
                    #{P2}
                    backpatch(B[0],nextquad())

                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        statements()
                        genquad('jump','_','_',Bquad)
                        backpatch(B[1],nextquad())
                        
                        
                    else:
                        print("ERROR:Expected \")\" after condition in line ",line)
                        exit(1)

                else:
                    print("ERROR:Expected \"(\" after case statement in line ",line)
                    exit(1)

            if(lex1[0] == default_tk):
                lex1 = lex()
                line = lex1[2]
                statements()

            else:
                print("ERROR:An error occured during the \"default\"  in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"forcase\"  in line ",line)
            exit(1)

    def incaseStat():
        global lex1,line

        if(lex1[0] == incase_tk):
            lex1 = lex()
            line = lex1[2]
            Bquad = nextquad()
            w = newtemp()
            genquad(':=',1,'_',w)

            while(lex1[0] == case_tk):
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    B = condition()
                    backpatch(B[0],nextquad())

                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        statements()
                        genquad(':=',0,'_',w)
                        backpatch(B[1],nextquad())
                        
                    else:
                        print("ERROR:Expected \")\" after condition in line ",line)
                        exit(1)

                else:
                    print("ERROR:Expected \"(\" after case statement in line ",line)
                    exit(1)
            genquad(':=',w,0,Bquad)            
        else:
            print("ERROR:An error occured during the \"incase\"  in line ",line)
            exit(1)

    def returnStat():
        global lex1,line

        if(lex1[0] == return_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]
                E_place = expression()

                if(lex1[0] == rquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    #{P1}
                    genquad('retv',E_place,'_','_')

                else:
                    print("ERROR:Expected \")\" after condition in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"(\" after case statement in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"return\" in line ",line)
            exit(1)

    def callStat():
        global lex1,line

        if(lex1[0] == call_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk):
                token = lex1[1]
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == lquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    actualparlist()
                    
                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        genquad('call',token,'_','_')
                        return

                    else:
                        print("ERROR:Expected \")\" after astualparlist in line ",line)
                        exit(1)

                else:
                    print("ERROR:Expected \"(\" after variable statement in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected variable after call in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"call\" in line ",line)
            exit(1)
        return

    def printStat():
        global lex1,line

        if(lex1[0] == print_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]
                E_place = expression()

                if(lex1[0] == rquotation_mark_tk):
                    lex1 = lex()
                    line = lex1[2]
                    #{P2}
                    genquad('out',E_place,'_','_')

                else:
                    print("ERROR:Expected \")\" after expression in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"(\" after print statement in line ",line)
                exit(1)

        else:
            print("ERROR:Expected \"print\" in line ",line)
            exit(1)

        return

    def inputStat():
        global lex1,line

        if(lex1[0] == input_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]

                if(lex1[0] == idk_tk):
                    token = lex1[1]
                    lex1 = lex()
                    line = lex1[2]
            
                    if(lex1[0] == rquotation_mark_tk):
                        lex1 = lex()
                        line = lex1[2]
                        #{P1}
                        genquad('inp',token,'_','_')
                        return

                    else:
                        print("ERROR:Expected \")\" after variable in line ",line)
                        exit(1)

                else:
                    print("ERROR:Expected variable in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"(\" after input statement in line ",line)
                exit(1)

        else:
            print("ERROR:An error occured during the \"input\"  in line ",line)
            exit(1)


    def actualparlist():
        global lex1,line

        actualparitem()

        while(lex1[0] == comma_tk):
            lex1 = lex()
            line = lex1[2]
            actualparitem()
        return

    def actualparitem():
        global lex1,line

        if(lex1[0] == in_tk):
            lex1 = lex()
            line = lex1[2]
            E = expression()
            genquad('par',E,'CV','_')

        elif(lex1[0] == inout_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == idk_tk):
                token = lex1[1]
                lex1 = lex()
                line = lex1[2]
                genquad('par',token,'REF','_')

            else:
                print("ERROR:Expected variable name after inout in line ",line)
                exit(1)

        return

    def condition():
        global lex1,line

        #{P1}
        P1 = boolterm()
        B_T = P1[0]
        B_F = P1[1]

        while(lex1[0] == or_tk):
            lex1 = lex()
            line = lex1[2]
            #{P2}
            backpatch(B_F,nextquad())
            P2 = boolterm()
            #{P3}
            B_T = merge(B_T,P2[0])
            B_F = P2[1]

        return B_T,B_F

    def boolterm():
        global lex1,line

        #{P1}
        R1 = boolfactor()
        Q_T = R1[0]
        Q_F = R1[1]

        while(lex1[0] == and_tk):
            lex1 = lex()
            line = lex1[2]
            #{P2}
            backpatch(Q_T,nextquad())
            R2 = boolfactor()
            #{P3}
            Q_T = R2[0]
            Q_F = merge(Q_F,R2[1])

        return Q_T,Q_F 

    def boolfactor():
        global lex1,line

        R_T = []
        R_F = []
        if(lex1[0] == not_tk):
            lex1 = lex()
            line = lex1[2]

            if(lex1[0] == lbracket_tk):
                lex1 = lex()
                line = lex1[2]
                B = condition()

                if(lex1[0] == rbracket_tk):
                    lex1 = lex()
                    line = lex1[2]
                    #{P1}
                    R_T = B[1]
                    R_F = B[0]

                else:
                    print("ERROR:Expected \"]\" after condition in line ",line)
                    exit(1)

            else:
                print("ERROR:Expected \"[\" after not in line ",line)
                exit(1)

        elif(lex1[0] == lbracket_tk):
            lex1 = lex()
            line = lex1[2]
            B = condition()

            if(lex1[0] == rbracket_tk):
                lex1 = lex()
                line = lex1[2]
                #{P1}
                R_T = B[0]
                R_F = B[1]

            else:
                print("ERROR:Expected \"]\" after condition in line ",line)
                exit(1)

        else:

            E1_place = expression()
            relop = REL_OP()
            E2_place = expression()
            #{P1}
            R_T = makelist(nextquad())
            genquad(relop,E1_place,E2_place,'_')
            R_F = makelist(nextquad())
            genquad('jump','_','_','_')

        return R_T,R_F

    def expression():
        global lex1,line
        
        sign = optimalSign()
        T1_place =  term()
        
        if sign == '-':
            w = newtemp()         
            genquad('-', 0, T1_place, w)
            T1_place = w

        while(lex1[0] == plus_tk or lex1[0] == minus_tk):
            operator = ADD_OP()
            T2_place = term()
            #{P1}
            w=newtemp()
            genquad(operator,T1_place,T2_place,w)
            T1_place = w

        #{P2}
        E_place = T1_place

        return E_place

    def term():
        global lex1,line
        
        F1_place = factor()

        while(lex1[0] == mult_tk or lex1[0] == div_tk):
            operator = MUL_OP()
            F2_place = factor()
            #{P1}
            w = newtemp()
            genquad(operator,F1_place,F2_place,w)
            F1_place = w

        #{P2}
        T_place = F1_place

        return T_place

    def factor():
        global lex1,line
       

        if(lex1[0] == dig_tk):
            F_place = lex1[1]
            lex1 = lex()
            line = lex1[2] 

        elif(lex1[0] == lquotation_mark_tk):
            lex1 = lex()
            line = lex1[2]
            E_place = expression()
            #{P1}
            F_place = E_place
            if(lex1[0] == rquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]

            else:
                print("ERROR:Expected \")\" after expression in line ",line)
                exit(1)

        elif(lex1[0] == idk_tk):
            token = lex1[1]
            lex1 = lex()
            line = lex1[2]
            F_place = idtail(token)

        else:
            print("ERROR:Expected integer or \"(\" or variable in line ",line)
            exit(1)
        return F_place

    def idtail(token):
        global lex1,line
        

        if(lex1[0] == lquotation_mark_tk):
            lex1 = lex()
            line = lex1[2]
            actualparlist()
            w = newtemp()
            genquad('par',w,'RET','_')
            genquad('call',token,'_','_')

            if(lex1[0] == rquotation_mark_tk):
                lex1 = lex()
                line = lex1[2]
                return w

            else:
                print("ERROR: Expected \")\" after the actualparlist in line ",line)
                exit(1)

        else:
            return token

    def optimalSign():
        global lex1,line
       

        if(lex1[0] == plus_tk or lex1[0] == minus_tk):
            return ADD_OP()
        return

    def REL_OP():
        global lex1,line
      

        if(lex1[0] == eq_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        elif(lex1[0] == lessorequal_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        elif(lex1[0] == greaterorequal_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        elif(lex1[0] == larger_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        elif(lex1[0] == smaller_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        elif(lex1[0] == notequal_tk):
            relop = lex1[1]
            lex1 = lex()
            line = lex1[2]
        else:
            print("ERROR:Expected \"=\" or \"<=\" or \">=\" or \">\" or \"<\" or \"<>\" in line ",line)
            exit(1)
        return relop

    def ADD_OP():
        global lex1,line
        

        if(lex1[0] == plus_tk):
            token = lex1[1]
            lex1 = lex()
            line = lex1[2]

        elif(lex1[0] == minus_tk):
            token = lex1[1]
            lex1 = lex()
            line = lex1[2]

        return token

    def MUL_OP():
        global lex1,line
        

        if(lex1[0] == mult_tk):
            token = lex1[1]
            lex1 = lex()
            line = lex1[2]
            

        elif(lex1[0] == div_tk):
            token = lex1[1]
            lex1 = lex()
            line = lex1[2]

        return token

    program()

    return


def intFile(file):
    text = ""
    for i in range(len(listofquads)):
        q = listofquads[i]
        text += str(q[1])+" "+str(q[2])+" "+str(q[3])+" "+str(q[4])+"\n"
    print(text)
    
    for i in range(len(listofquads)):
        q = listofquads[i]
        file.write(str(q[1])+" ")
        file.write(str(q[2])+" ")
        file.write(str(q[3])+" ")
        file.write(str(q[4])+" ")
        file.write("\n")
        
if __name__ == '__main__':
    cp = open('txtFile.txt','w')
    intf = open('intFile.int','w')
    syn()
    intFile(intf)
    cp.close()
    intf.close()
