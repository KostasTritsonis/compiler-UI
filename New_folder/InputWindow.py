from PyQt6.QtWidgets import QDialog,QApplication
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from PyQt6.uic import loadUi
import sys


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
        new_size = event.size()
        self.pushButton.move(new_size.width()-230, new_size.height()-50)
        self.label.move(new_size.width()-380,new_size.height()- 100)
        self.lineEdit.move(new_size.width()-250,new_size.height()-100)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = InputWindow()
    ui.show()
    app.exec()    
