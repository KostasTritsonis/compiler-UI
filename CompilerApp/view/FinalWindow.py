from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
import os,FactoryMethod,Controller

class FinalWindow(QMainWindow):
    def __init__(self):
        self.path = os.path.join('..', 'model', 'final.py')
        self.inputValue = ''
        self.line = ''
        super(FinalWindow,self).__init__()
        loadUi("FinalWindow.ui",self)
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.readfile()
        
    def readfile(self):
        Controller.runFinal(self)
        
    def giveInput(self):
        FactoryMethod.command(self,'input')
        
    def setInputValue(self,data):
        self.inputValue = data

    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(9, 39, newSize.width() - 20, newSize.height() - 100)
        self.label.move((self.textEdit.width() // 2),10)

