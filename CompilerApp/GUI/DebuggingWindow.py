from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from BreakpointWindow import *
from InputWindow import *
import os,subprocess

path = os.path.join('..', 'src', 'final.py')


class DebugWindow(QMainWindow):
    breakPoint = ''
    inputValue = ''
    def __init__(self):
        super(DebugWindow,self).__init__()
        loadUi("DebugWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.pushButton.clicked.connect(self.stop)
        self.pushButton_2.clicked.connect(self.runAgain)
        self.giveBreakPoint()
        self.debug()
    
    def resizeEvent(self, event):
        newSize = event.size()
         
        self.textEdit.setGeometry(9, 31, newSize.width() - 20, newSize.height() - 100)
        self.pushButton.move(90, newSize.height() - 60)
        self.pushButton_2.move(10, newSize.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)

        
    def stop(self):
        self.close()

    def runAgain(self):
        self.giveBreakPoint()
        self.debug()
        
    def debug(self):
        scriptPath  = "python -u {compiler} {line}".format(compiler=path,line=breakPoint)
        self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        finalText = ''
        while self.process.poll() is None:
            line = self.process.stdout.readline().strip()
            if line:
                if 'Give input' in line:
                    self.giveInput(line)
                    self.process.stdin.write(inputValue + "\n")
                    self.process.stdin.flush()
                if line == '-':
                    while self.process.poll() is None:
                        line = self.process.stdout.readline().strip()
                        finalText+=line+'\n'
        self.textEdit.setText(finalText.strip())
        self.process.stdin.close()
        
    def setBreakpoint(self,data):
        global breakPoint
        if data == '':
            self.giveBreakPoint()
        else:
            breakPoint = data
            
    def setInputValue(self,data):
        global inputValue
        inputValue = data
        
    def giveInput(self,line):
            dialog = InputWindow()
            dialog.label.setText(line)
            dialog.dataPassed.connect(self.setInputValue)
            dialog.exec()  
            
    def giveBreakPoint(self):
        dialog = BreakpointWindow()
        dialog.dataPassed.connect(self.setBreakpoint)
        dialog.exec()
            