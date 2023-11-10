from PyQt6.QtWidgets import QDialog,QSizePolicy
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal,Qt
from PyQt6.uic import loadUi


class InputWindow(QDialog):
    dataPassed = pyqtSignal(str)
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("InputWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.pushButton.clicked.connect(self.accept)
       
        self.data = None
        
    def accept(self):
        self.data = self.lineEdit.text()
        self.dataPassed.emit(self.data)
        super().accept()