from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from DebuggingWindow import *
from InputWindow import *


class FinalWindow(QMainWindow):
    breakpoint = ''
    def __init__(self):
        super(FinalWindow,self).__init__()
        loadUi("FinalWindow.ui",self)
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        
        self.p = QProcess()
        script_path  = "python {compiler} {current_path} 100".format(compiler='final.py',current_path='intFile.int')
        self.p.startCommand(script_path)
        f = open('intFile.int','r')
        f1 = f.read()
        if 'inp' in f1:
            dialog = InputWindow()
            dialog.dataPassed.connect(self.setBreakpoint)
            dialog.exec()
            self.p.write(breakpoint.encode())
            self.p.closeWriteChannel()
        self.p.waitForFinished()
        output = self.p.readAllStandardOutput().data().decode()
        self.textEdit.setText(output)
        
        
    
    def resizeEvent(self, event):
        new_size = event.size()
         
        self.textEdit.setGeometry(9, 39, new_size.width() - 20, new_size.height() - 100)
        self.label.move((self.textEdit.width() // 2),10)
        
    def setBreakpoint(self,data):
        global breakpoint
        breakpoint = data
