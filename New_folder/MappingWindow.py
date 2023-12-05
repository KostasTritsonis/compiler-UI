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
        text=''
        temp = self.output.split('\n')
        del temp[-1]
        del temp[-1]

        temp1 = temp[0].split(' ')
        temp1[-1] = temp1[-1].replace('\r','')
        sourceLine = self.input[int(temp1[-1])-2].strip()
        text = sourceLine
        
        for i in temp:
            temp1 = i.split(' ')
            temp1[-1] = temp1[-1].replace('\r','')
            sourceLine = self.input[int(temp1[-1])-1].strip()
            del temp1[-1]
            if sourceLine in text:
                text +='\t\t'+' '.join(temp1)+'\n'
            else:
                text += sourceLine+'\n'
                text +='\t\t'+' '.join(temp1)+'\n'
        self.output = text
        
    def readSourcefile(self):
        file = open(self.path,'r')
        lines = file.read()
        self.input = lines.split("\n")

    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(13, 20, newSize.width() - 25, newSize.height() - 50)
        self.label.move((self.textEdit.width() // 2)-31,0)   
