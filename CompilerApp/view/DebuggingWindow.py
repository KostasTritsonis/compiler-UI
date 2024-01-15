from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
import os,FactoryMethod,Controller


class DebuggingWindow(QMainWindow):
    def __init__(self):
        self.path = os.path.join('..', 'model', 'final.py')
        self.breakPoint = ''
        self.inputValue = ''
        self.line = ''
        super(DebuggingWindow,self).__init__()
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
        Controller.runDebug(self)
        
    def setBreakpoint(self,data):
        if data == '':
            self.giveBreakPoint()
        else:
            self.breakPoint = data
            
    def setInputValue(self,data):
        self.inputValue = data

        
    def giveInput(self):
        FactoryMethod.command(self,'input')
            
    def giveBreakPoint(self):
        FactoryMethod.command(self,'breakpoint')
    
    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(9, 31, newSize.width() - 20, newSize.height() - 100)
        self.pushButton.move(90, newSize.height() - 60)
        self.pushButton_2.move(10, newSize.height() - 60)
        self.pushButton_3.move(newSize.width()-170, newSize.height() - 60)
        self.pushButton_4.move(newSize.width()-90, newSize.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)
              
