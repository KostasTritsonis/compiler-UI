from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi


class DebugWindow(QMainWindow):
    def __init__(self):
        super(DebugWindow,self).__init__()
        loadUi("DebugWindow.ui",self) 
        self.setWindowIcon(QtGui.QIcon('compiler.png'))

        self.pushButton.clicked.connect(self.stop)

    
    def resizeEvent(self, event):
        new_size = event.size()
         
        self.textEdit.setGeometry(9, 31, new_size.width() - 20, new_size.height() - 100)
        #self.textBrowser.setGeometry(10, 30, new_size.width()-70, new_size.height() - 120)
        self.pushButton.move(10, new_size.height() - 60)
        self.label.move((self.textEdit.width() // 2),10)

        

    def stop(self):
        self.close()