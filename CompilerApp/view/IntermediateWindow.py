from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from PyQt6.uic import loadUi
import FactoryMethod,Controller

class IntermediateWindow(QMainWindow):
    def __init__(self):
        super(IntermediateWindow,self).__init__()
        loadUi("IntermediateWindow.ui",self)
        self.path = None
        self.compiler = None
        self.output = ''
        self.totalLines = ''
        self.numberLine()
        self.init()
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.setWindowTitle("Intermediate Window")

        
        self.actionStart.triggered.connect(self.startDebug)
        self.pushButton.clicked.connect(self.finalRun)
        self.actionSource_Code_Mapping.triggered.connect(self.startMap)

    def setPath(self,path):
        self.path = path

    def setCompiler(self,compiler):
        self.compiler = compiler  

    def run(self):
        Controller.runIntermediate(self)

    def startDebug(self):
        FactoryMethod.command(self,'debug')

    def startMap(self):
        FactoryMethod.command(self,'map')

    def setOutput(self,output):
        text=''
        temp = output.split('\n')
        if len(temp[0].split(' ')) == 5:
            for i in temp:
                temp1 = i.split(' ')
                del temp1[-1]
                text+=' '.join(temp1)+'\n'
            text.strip()
        else:
            return output
        return text
    
    def finalRun(self):
        FactoryMethod.command(self,'final')

    def numberLine(self):
        self.textEdit.textChanged.connect(self.updateLineNumbers)
        self.lineNumberEdit = self.textBrowser
        self.lineNumberEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def updateLineNumbers(self):
        text = self.textEdit.toPlainText()
        lineCount = text.count('\n') + 1
        lineNumbersText = '\n'.join(map(str, range(1, lineCount + 1)))
        self.totalLines = lineCount
        self.lineNumberEdit.setPlainText(lineNumbersText)

    def init(self):
        self.textEdit.verticalScrollBar().valueChanged.connect(self.syncScrollBars)
        self.textBrowser.verticalScrollBar().valueChanged.connect(self.syncScrollBars)

    def syncScrollBars(self):
        scrollValue = self.sender().value()
        self.textEdit.verticalScrollBar().setValue(scrollValue)
        self.textBrowser.verticalScrollBar().setValue(scrollValue)
    
    def resizeEvent(self, event):
        newSize = event.size()
        self.textEdit.setGeometry(40, 31, newSize.width() - 60, newSize.height() - 120)
        self.textBrowser.setGeometry(10, 31, 31, newSize.height() - 120)
        self.pushButton.move(10, newSize.height() - 80)
        self.label.move((self.textEdit.width() // 2)-31,0)