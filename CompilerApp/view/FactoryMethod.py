from ErrorWindow import *
from IntermidiateWindow import *
from DebuggingWindow import *
from MappingWindow import *
from FinalWindow import *
from InputWindow import *
from BreakpointWindow import *

def command(self,type):
    if type == 'errorComp':
        self.ErrWindow = ErrorWindow()
        self.ErrWindow.show()
        self.ErrWindow.label.setText("Choose Compiler first")
        self.ErrWindow.setWindowTitle("Error Window")
    elif type == 'intermidiate':
        self.InterWindow = IntermidiateWindow()
        self.InterWindow.setPath(self.currentPath)
        self.InterWindow.setCompiler(self.compiler)
        self.InterWindow.run()
    elif type == 'error':
        self.ErrWindow = ErrorWindow()
        self.ErrWindow.show()
        self.ErrWindow.label.setText(self.output)
        self.ErrWindow.setWindowTitle("Error Window") 
    elif type == 'debug':
        self.DebWindow = DebuggingWindow()
        self.DebWindow.show()
        self.DebWindow.setWindowTitle("Debug Window")
    elif type == 'map':
        self.MapWindow = MappingWindow()
        self.MapWindow.setPath(self.path)
        self.MapWindow.setOutput(self.output)
        self.MapWindow.run()
    elif type == 'final':
        self.FinalWindow = FinalWindow()
        self.FinalWindow.show()
        self.FinalWindow.setWindowTitle("Final Window") 
    elif type == 'input': 
        self.dialog = InputWindow()
        self.dialog.label.setText(self.line)
        self.dialog.dataPassed.connect(self.setInputValue)
        self.dialog.exec()
    elif type == 'breakpoint':
        self.dialog = BreakpointWindow()
        self.dialog.dataPassed.connect(self.setBreakpoint)
        self.dialog.exec()  