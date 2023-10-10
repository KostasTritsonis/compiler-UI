from PyQt6.QtWidgets import  QMainWindow, QFileDialog,QApplication
from PyQt6.QtCore import Qt,QProcess
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from IntermidiateWindow import *
from ErrorWindow import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("MainWindow.ui",self)

        self.current_path = None
        self.compiler = None
        self.number_line()
        self.init()
        self.textEdit.setPlaceholderText("Type your text here...")
        self.setWindowIcon(QtGui.QIcon('compiler.png'))

        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.pushButton.clicked.connect(self.compile)
        self.pushButton1.clicked.connect(self.selectCompiler)

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

    def saveFile(self):
        if self.current_path is not None:
            with open(self.current_path, 'w') as f:
                f.write(self.textEdit.toPlainText())
        else:
            self.saveFileAs()

    def saveFileAs(self):
        pathname = QFileDialog.getSaveFileName(self, 'Save file', '', 'Python files(*.py)')
        if(pathname[0]!=""):
            with open(pathname[0], 'w') as f:
                f.write(self.textEdit.toPlainText())
            self.current_path = pathname[0]
            self.setWindowTitle(pathname[0])
        else:
            return

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','', 'Cimple files(*.ci);;Python files (*.py)')
        if(fname[0]!=""):
            self.setWindowTitle(fname[0])
            with open(fname[0], 'r') as f:
                filetext = f.read()
                self.textEdit.setText(filetext)
            self.current_path = fname[0]
        else:
            return
        
    def selectCompiler(self):
        fname = QFileDialog.getOpenFileName(self, 'Choose Compiler','', 'Python files (*.py)')
        self.compiler = fname[0]

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()

    def compile(self):
        self.p = QProcess()
        script_path  = "python {compiler} {current_path}".format(current_path=self.current_path,compiler='cimple.py')
        
        self.p.startCommand(script_path)
        self.p.waitForFinished()
        output = self.p.readAllStandardOutput().data().decode()
        error = self.p.exitCode()
        if error == 1:
            self.err = ErrorWindow()
            self.err.show()
            self.err.label.setText(output)
            self.err.setWindowTitle("Error Window")  
        else:
            self.window1 = IntermidiateWindow()
            self.window1.show()
            self.window1.textEdit.setText(output)
            self.window1.setWindowTitle("Intermidiate Window")   
        
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
        self.textEdit.setGeometry(50, 30, new_size.width() - 70, new_size.height() - 120)
        self.textBrowser.setGeometry(10, 30, 51, new_size.height() - 120)
        self.pushButton.move(10, new_size.height() - 80)
        self.pushButton1.move(new_size.width()-100, 0)
        self.label.move(new_size.width()-150, 0)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec()    
