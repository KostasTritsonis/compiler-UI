from PyQt6.QtWidgets import QDialog
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from PyQt6.uic import loadUi


class InputWindow(QDialog):
    dataPassed = pyqtSignal(str)
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("InputWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.pushButton.clicked.connect(self.accept)
       
        self.data = None
        
    def accept(self):
        self.data = self.lineEdit.text()
        self.dataPassed.emit(self.data)
        super().accept()
        
    def resizeEvent(self, event):
        newSize = event.size()
        self.pushButton.move(newSize.width()-230, newSize.height()-50)
        self.label.move(newSize.width()-380,newSize.height()- 100)
        self.lineEdit.move(newSize.width()-250,newSize.height()-100)
    