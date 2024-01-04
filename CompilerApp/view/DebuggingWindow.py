from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from BreakpointWindow import *
from InputWindow import *
import os,subprocess


class DebugWindow(QMainWindow):
    def __init__(self):
        self.path = os.path.join('..', 'view', 'final.py')
        self.breakPoint = ''
        self.inputValue = ''
        self.totalLines = ''
        super(DebugWindow,self).__init__()
        loadUi("DebugWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.pushButton.clicked.connect(self.stop)
        self.pushButton_2.clicked.connect(self.runAgain)
        self.pushButton_3.clicked.connect(self.runPrev)
        self.pushButton_4.clicked.connect(self.runNext)
        self.giveBreakPoint()
        self.debug()
        
    def stop(self):
        self.close()

    def runAgain(self):
        self.giveBreakPoint()
        self.debug()
    
    def runNext(self):
        self.breakPoint = int( self.breakPoint)
        self.breakPoint =  self.breakPoint + 1
        self.breakPoint = str( self.breakPoint)
        self.setBreakpoint( self.breakPoint)
        self.debug()

    def runPrev(self):
        self.breakPoint = int( self.breakPoint)
        self.breakPoint =  self.breakPoint - 1
        self.breakPoint = str( self.breakPoint)
        self.setBreakpoint( self.breakPoint)
        self.debug()
        
    def debug(self):
        global breakPoint
        scriptPath  = "python -u {compiler} {line}".format(compiler=self.path,line=self.breakPoint)
        self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        finalText = ''
        while self.process.poll() is None:
            line = self.process.stdout.readline().strip()
            if line:
                if 'Give input' in line:
                    self.giveInput(line)
                    self.process.stdin.write(self.inputValue + "\n")
                    self.process.stdin.flush()
                if line == '-':
                    while self.process.poll() is None:
                        line = self.process.stdout.readline().strip()
                        finalText+=line+'\n'
        self.textEdit.setText(finalText.strip())
        self.process.stdin.close()
        
    def setBreakpoint(self,data):
        if data == '':
            self.giveBreakPoint()
        else:
            self.breakPoint = data
            
    def setInputValue(self,data):
        self.inputValue = data

    def setTotalLines(self,lines):
        self.totalLines = lines
        
    def giveInput(self,line):
        dialog = InputWindow()
        dialog.label.setText(line)
        dialog.dataPassed.connect(self.setInputValue)
        dialog.exec()  
            
    def giveBreakPoint(self):
        global breakPoint
        dialog = BreakpointWindow()
        dialog.dataPassed.connect(self.setBreakpoint)
        dialog.exec()
    
    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(9, 31, newSize.width() - 20, newSize.height() - 100)
        self.pushButton.move(90, newSize.height() - 60)
        self.pushButton_2.move(10, newSize.height() - 60)
        self.pushButton_3.move(newSize.width()-170, newSize.height() - 60)
        self.pushButton_4.move(newSize.width()-90, newSize.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)
              
