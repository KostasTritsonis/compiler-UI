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
        self.number_line()
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
        self.p = QProcess()
        script_path  = "python {compiler} {current_path}".format(current_path=self.path,compiler=self.compiler)
        self.p.startCommand(script_path)
        if(self.p.waitForFinished() == False):
            return
        output = self.p.readAllStandardOutput().data().decode()
        self.output = output
        error = self.p.exitCode()
        if error == 1:
            self.err = ErrorWindow()
            self.err.show()
            self.err.label.setText(output)
            self.err.setWindowTitle("Error Window")  
        else:
            output = self.setOutput(output)
            self.textEdit.setText(output)
            self.show()

    def startDebug(self):
        self.window2 = DebugWindow()
        self.window2.show()
        self.window2.setWindowTitle("Debug Window")

    def startMap(self):
        self.window3 = MappingWindow()
        self.window3.setPath(self.path)
        self.window3.setOutput(self.output)
        self.window3.run()

    def setOutput(self,output):
        s=''
        temp1 = output.split('\n')
        for i in temp1:
            temp2 = i.split(' ')
            del temp2[-1]
            s+=' '.join(temp2)+'\n'
        return s
    
    def finalRun(self):
        self.window1 = FinalWindow()
        self.window1.show()
        self.window1.setWindowTitle("Final Window")     

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