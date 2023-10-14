from PyQt6.QtWidgets import QDialog
from PyQt6 import QtGui
from PyQt6.uic import loadUi


class BreakpointWindow(QDialog):
    def __init__(self):
        super(BreakpointWindow,self).__init__()
        loadUi("BreakpointWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
       
        