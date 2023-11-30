from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from DebuggingWindow import *
from InputWindow import *
from ErrorWindow import *

class FinalWindow(QMainWindow):
    inputValue = ''
    def __init__(self):
        super(FinalWindow,self).__init__()
        loadUi("FinalWindow.ui",self)
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.readfile()
        
        
    def resizeEvent(self, event):
        new_size = event.size()
         
        self.textEdit.setGeometry(9, 39, new_size.width() - 20, new_size.height() - 100)
        self.label.move((self.textEdit.width() // 2),10)
        
    def readfile(self):
        script_path  = "python -u {compiler} None".format(compiler='final.py',line=breakpoint)
        self.p = subprocess.Popen(script_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        text = ''
        while self.p.poll() is None:
            line = self.p.stdout.readline().strip()
            if line:
                if 'Give input' in line:
                    self.giveInput(line)
                    self.p.stdin.write(inputValue + "\n")
                    self.p.stdin.flush()
                else:
                    text+=line+'\n'
            self.textEdit.setText(text)
        self.p.stdin.close()
        
    def giveInput(self,line):
        dialog = InputWindow()
        dialog.label.setText(line)
        dialog.dataPassed.connect(self.setInputValue)
        dialog.exec()  
        
    def setInputValue(self,data):
        global inputValue
        inputValue = data

