from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi

class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow,self).__init__()
        loadUi("AboutWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        
        