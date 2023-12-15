from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from DebuggingWindow import *
from InputWindow import *
from ErrorWindow import *
import os,subprocess



class FinalWindow(QMainWindow):
    path = os.path.join('..', 'src', 'final.py')
    inputValue = ''
    def __init__(self):
        super(FinalWindow,self).__init__()
        loadUi("FinalWindow.ui",self)
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.readfile()
        
        
    def resizeEvent(self, event):
        newSize = event.size()
         
        self.textEdit.setGeometry(9, 39, newSize.width() - 20, newSize.height() - 100)
        self.label.move((self.textEdit.width() // 2),10)
        
    def readfile(self):
        scriptPath  = "python -u {compiler} None".format(compiler=path)
        self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        finalTtext = ''
        while self.process.poll() is None:
            line = self.process.stdout.readline().strip()
            if line:
                if 'Give input' in line:
                    self.giveInput(line)
                    self.process.stdin.write(inputValue + "\n")
                    self.process.stdin.flush()
                else:
                    finalTtext+=line+'\n'
            self.textEdit.setText(finalTtext)
        self.process.stdin.close()
        
    def giveInput(self,line):
        dialog = InputWindow()
        dialog.label.setText(line)
        dialog.dataPassed.connect(self.setInputValue)
        dialog.exec()  
        
    def setInputValue(self,data):
        global inputValue
        inputValue = data

