from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi

class MappingWindow(QMainWindow):
    def __init__(self):
        super(MappingWindow,self).__init__()
        loadUi("MappingWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.setWindowTitle("Mapping Window")
        self.path = None
        self.output = ''
        self.input = ''

    def run(self):
        self.readSourcefile()
        self.createOutput()
        self.textEdit.setText(self.output)
        self.show()

    def setOutput(self,output):
        self.output = output

    def setPath(self,path):
        self.path = path

    def createOutput(self):
        s=''
        temp1 = self.output.split('\n')
        del temp1[-1]
        del temp1[-1]

        temp2 = temp1[0].split(' ')
        temp2[-1] = temp2[-1].replace('\r','')
        sourceLine = self.input[int(temp2[-1])-2].strip()
        s = sourceLine
        
        for i in temp1:
            temp2 = i.split(' ')
            temp2[-1] = temp2[-1].replace('\r','')
            sourceLine = self.input[int(temp2[-1])-1].strip()
            del temp2[-1]
            if sourceLine in s:
                s +='\t\t'+' '.join(temp2)+'\n'
            else:
                s += sourceLine+'\n'
                s +='\t\t'+' '.join(temp2)+'\n'
        self.output = s
        
    def readSourcefile(self):
        file = open(self.path,'r')
        lines = file.read()
        self.input = lines.split("\n")

    def resizeEvent(self, event):
        new_size = event.size()
        self.textEdit.setGeometry(13, 20, new_size.width() - 25, new_size.height() - 50)
        self.label.move((self.textEdit.width() // 2)-31,0)   
