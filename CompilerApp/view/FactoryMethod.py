from ErrorWindow import *
from IntermediateWindow import *
from DebuggingWindow import *
from MappingWindow import *
from FinalWindow import *
from InputWindow import *
from BreakpointWindow import *
from AboutWindow import *

def command(self,type):
    if type == 'errorComp':
        self.ErrWindow = ErrorWindow()
        self.ErrWindow.show()
        self.ErrWindow.label.setText("Choose Compiler first")
        self.ErrWindow.setWindowTitle("Error Window")
    elif type == 'intermidiate':
        self.InterWindow = IntermediateWindow()
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
        self.MapWindow.setWindowTitle("Mapping Window")
        self.MapWindow.run()
    elif type == 'final':
        self.FinalWindow = FinalWindow()
        self.FinalWindow.show()
        self.FinalWindow.setWindowTitle("Final Window") 
    elif type == 'input': 
        self.InputWindow = InputWindow()
        self.InputWindow.label.setText(self.line)
        self.InputWindow.dataPassed.connect(self.setInputValue)
        self.InputWindow.exec()
    elif type == 'breakpoint':
        self.BreakWindow = BreakpointWindow()
        self.BreakWindow.dataPassed.connect(self.setBreakpoint)
        self.BreakWindow.exec()  
    elif type == 'about':
        self.AboutWindow = AboutWindow()
        self.AboutWindow.show()
