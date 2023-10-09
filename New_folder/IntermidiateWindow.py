from PyQt6.QtCore import QIODevice, QTextStream,QProcess
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from DebuggingWindow import *
from FinalWindow import *
import sys

class IntermidiateWindow(QMainWindow):
    def __init__(self):
        super(IntermidiateWindow,self).__init__()
        loadUi("IntermidiateWindow.ui",self)
        self.number_line()
        self.init()
        self.setWindowIcon(QtGui.QIcon('compiler.png'))

        self.actionStart.triggered.connect(self.start)
        self.pushButton.clicked.connect(self.run)

    def start(self):
        self.window2 = DebugWindow()
        self.window2.show()
        self.window2.setWindowTitle("Debug Window")
     
    def run(self):
        self.p = QProcess()
        self.p.start(sys.executable, ["final.py"], QIODevice.OpenMode(QIODevice.OpenModeFlag.ReadWrite))
        
        
    def number_line(self):
        self.textEdit.textChanged.connect(self.update_line_numbers)
        self.line_number_edit = self.textBrowser
        self.line_number_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def update_line_numbers(self):
        text = self.textEdit.toPlainText()
        line_count = text.count('\n') + 1
        line_numbers_text = '\n'.join(map(str, range(1, line_count + 1)))
        self.line_number_edit.setPlainText(line_numbers_text)

    def init(self):
        self.textEdit.verticalScrollBar().valueChanged.connect(self.sync_scroll_bars)
        self.textBrowser.verticalScrollBar().valueChanged.connect(self.sync_scroll_bars)

    def sync_scroll_bars(self):
        scroll_value = self.sender().value()
        self.textEdit.verticalScrollBar().setValue(scroll_value)
        self.textBrowser.verticalScrollBar().setValue(scroll_value)
    
    def resizeEvent(self, event):
        new_size = event.size()
        
        self.textEdit.setGeometry(40, 31, new_size.width() - 60, new_size.height() - 120)
        self.textBrowser.setGeometry(10, 31, 31, new_size.height() - 120)
        self.pushButton.move(10, new_size.height() - 80)
        self.label.move((self.textEdit.width() // 2)-31,0)

