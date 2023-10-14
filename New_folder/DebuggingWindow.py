from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.QtCore import QProcess
from PyQt6.uic import loadUi
from BreakpointWindow import *

class DebugWindow(QMainWindow):
    breakpoint = ''
    def __init__(self):
        super(DebugWindow,self).__init__()
        loadUi("DebugWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.pushButton.clicked.connect(self.stop)
        
        dialog = BreakpointWindow()
        dialog.dataPassed.connect(self.setBreakpoint)
        dialog.exec()
        
        self.debug()
    
    def resizeEvent(self, event):
        new_size = event.size()
         
        self.textEdit.setGeometry(9, 31, new_size.width() - 20, new_size.height() - 100)
        self.pushButton.move(10, new_size.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)

        
    def stop(self):
        self.close()
        
    def debug(self):
        self.p = QProcess()
        script_path  = "python {compiler} {current_path} {line}".format(compiler='final.py',current_path='intFile.int',line=breakpoint)
        self.p.startCommand(script_path)
        self.p.waitForFinished()
        output = self.p.readAllStandardOutput().data().decode()
        self.textEdit.setText(output)
        
    def setBreakpoint(self,data):
        global breakpoint
        if data == '':
            breakpoint = '0'
        else:
            breakpoint = data
        