from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class ErrorWindow(QMainWindow):
    def __init__(self):
        super(ErrorWindow,self).__init__()
        loadUi("ErrorWindow.ui",self) 

        self.pushButton.clicked.connect(self.stop)


    def stop(self):
        self.close()