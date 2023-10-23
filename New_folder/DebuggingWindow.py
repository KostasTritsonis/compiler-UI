from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from BreakpointWindow import *
from InputWindow import *
import subprocess
class DebugWindow(QMainWindow):
    breakpoint = ''
    inputValue = ''
    def __init__(self):
        super(DebugWindow,self).__init__()
        loadUi("DebugWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.pushButton.clicked.connect(self.stop)
        self.giveBreakPoint()
        self.debug()
    
    def resizeEvent(self, event):
        new_size = event.size()
         
        self.textEdit.setGeometry(9, 31, new_size.width() - 20, new_size.height() - 100)
        self.pushButton.move(10, new_size.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)

        
    def stop(self):
        self.close()
        
    def debug(self):
        script_path  = "python -u {compiler} {current_path} {line}".format(compiler='final.py',current_path='intFile.int',line=breakpoint)
        self.p = subprocess.Popen(script_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
        text = ''
        while self.p.poll() is None:
            line = self.p.stdout.readline().strip()
            if line:
                if 'Give input:' in line:
                    self.giveInput()
                    self.p.stdin.write(inputValue + "\n")
                    self.p.stdin.flush()
                if line == '-':
                    while self.p.poll() is None:
                        line = self.p.stdout.readline().strip()
                        text+=line+'\n'
        self.textEdit.setText(text.strip())
        self.p.stdin.close()
        
    def setBreakpoint(self,data):
        global breakpoint
        if data == '':
            self.giveBreakPoint()
        else:
            breakpoint = data
            
    def setInputValue(self,data):
        global inputValue
        inputValue = data
        
    def giveInput(self):
            dialog = InputWindow()
            dialog.dataPassed.connect(self.setInputValue)
            dialog.exec()  
            
    def giveBreakPoint(self):
        dialog = BreakpointWindow()
        dialog.dataPassed.connect(self.setBreakpoint)
        dialog.exec()
            