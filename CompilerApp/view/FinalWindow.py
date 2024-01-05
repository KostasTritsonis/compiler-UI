from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
import os,subprocess,FactoryMethod

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
        scriptPath  = "python -u {compiler} None".format(compiler=self.path)
        self.process = subprocess.Popen(scriptPath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        finalTtext = ''
        while self.process.poll() is None:
            line = self.process.stdout.readline().strip()
            if line:
                if 'Give input' in line:
                    self.line = line
                    self.giveInput()
                    self.process.stdin.write(self.inputValue + "\n")
                    self.process.stdin.flush()
                else:
                    finalTtext+=line+'\n'
            self.textEdit.setText(finalTtext)
        self.process.stdin.close()
        
    def giveInput(self):
        FactoryMethod.command(self,'input')
        
    def setInputValue(self,data):
        self.inputValue = data

    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(9, 39, newSize.width() - 20, newSize.height() - 100)
        self.label.move((self.textEdit.width() // 2),10)

