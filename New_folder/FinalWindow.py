from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
from DebuggingWindow import *


class FinalWindow(QMainWindow):
    def __init__(self):
        super(FinalWindow,self).__init__()
        loadUi("FinalWindow.ui",self)