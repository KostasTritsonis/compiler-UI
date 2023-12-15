from PyQt6.QtCore import Qt,QProcess
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from DebuggingWindow import *
from FinalWindow import *
from MappingWindow import *

class IntermidiateWindow(QMainWindow):
    def __init__(self):
        super(IntermidiateWindow,self).__init__()
        loadUi("IntermidiateWindow.ui",self)
        self.path = None
        self.compiler = None
        self.output = ''
        self.numberLine()
        self.init()
        self.setWindowIcon(QtGui.QIcon('compiler.png'))
        self.setWindowTitle("Intermidiate Window")

        
        self.actionStart.triggered.connect(self.startDebug)
        self.pushButton.clicked.connect(self.finalRun)
        self.actionSource_Code_Mapping.triggered.connect(self.startMap)

    def setPath(self,path):
        self.path = path

    def setCompiler(self,compiler):
        self.compiler = compiler  

    def run(self):
        self.process = QProcess()
        scriptPath  = "python {compiler} {currentPath}".format(currentPath=self.path,compiler=self.compiler)
        self.process.startCommand(scriptPath)
        if(self.process.waitForFinished() == False):
            return
        output = self.process.readAllStandardOutput().data().decode()
        self.output = output
        error = self.process.exitCode()
        if error == 1:
            self.ErrWindow = ErrorWindow()
            self.ErrWindow.show()
            self.ErrWindow.label.setText(output)
            self.ErrWindow.setWindowTitle("Error Window")  
        else:
            output = self.setOutput(output)
            self.textEdit.setText(output)
            self.show()

    def startDebug(self):
        self.DebWindow = DebugWindow()
        self.DebWindow.show()
        self.DebWindow.setWindowTitle("Debug Window")

    def startMap(self):
        self.MapWindow = MappingWindow()
        self.MapWindow.setPath(self.path)
        self.MapWindow.setOutput(self.output)
        self.MapWindow.run()

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
        self.FinalWindow = FinalWindow()
        self.FinalWindow.show()
        self.FinalWindow.setWindowTitle("Final Window")     

    def numberLine(self):
        self.textEdit.textChanged.connect(self.updateLineNumbers)
        self.lineNumberEdit = self.textBrowser
        self.lineNumberEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def updateLineNumbers(self):
        text = self.textEdit.toPlainText()
        lineCount = text.count('\n') + 1
        lineNumbersText = '\n'.join(map(str, range(1, lineCount + 1)))
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