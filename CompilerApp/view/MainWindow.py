from PyQt6.QtWidgets import  QMainWindow, QFileDialog,QApplication
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6.uic import loadUi
from IntermidiateWindow import *
from ErrorWindow import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("MainWindow.ui",self)

        self.currentPath = None
        self.compiler = None
        self.numberLine()
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
        self.currentPath = None

    def saveFile(self):
        if self.currentPath is not None:
            with open(self.currentPath, 'w') as file:
                file.write(self.textEdit.toPlainText())
        else:
            self.saveFileAs()

    def saveFileAs(self):
        pathName = QFileDialog.getSaveFileName(self, 'Save file', '', 'Cimple files(*.ci)')
        if(pathName[0]!=""):
            with open(pathName[0], 'w') as file:
                file.write(self.textEdit.toPlainText())
            self.currentPath = pathName[0]
            self.setWindowTitle(pathName[0])
        else:
            return

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file','', 'Cimple files(*.ci)')
        if(fileName[0]!=""):
            self.setWindowTitle(fileName[0])
            with open(fileName[0], 'r') as file:
                fileText = file.read()
                self.textEdit.setText(fileText)
            self.currentPath = fileName[0]
        else:
            return
        
    def selectCompiler(self):
        fileName = QFileDialog.getOpenFileName(self, 'Choose Compiler','', 'Python files (*.py)')
        self.compiler = fileName[0]

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
        if self.compiler == '' or self.compiler == None :
            self.ErrWindow = ErrorWindow()
            self.ErrWindow.show()
            self.ErrWindow.label.setText("Choose Compiler first")
            self.ErrWindow.setWindowTitle("Error Window") 
        else:
            self.InterWindow = IntermidiateWindow()
            self.InterWindow.setPath(self.currentPath)
            self.InterWindow.setCompiler(self.compiler)
            self.InterWindow.run()
        
      
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
        self.textEdit.setGeometry(50, 30, newSize.width() - 70, newSize.height() - 120)
        self.textBrowser.setGeometry(10, 30, 51, newSize.height() - 120)
        self.pushButton.move(10, newSize.height() - 80)
        self.pushButton1.move(newSize.width()-100, 0)
        self.label.move(newSize.width()-150, 0)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec()    
