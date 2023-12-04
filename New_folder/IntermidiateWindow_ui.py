# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IntermidiateWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 645)
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color:rgb(33,33,33);\n"
"color:#FFFFFF;\n"
"}\n"
"QTextEdit{\n"
"background-color:rgb(46,46,46);\n"
"border:0;\n"
"}\n"
"QMenuBar::item:selected{\n"
"color:#000000;\n"
"}")
        self.actionStart = QAction(MainWindow)
        self.actionStart.setObjectName(u"actionStart")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionControl_Flow_Graph = QAction(MainWindow)
        self.actionControl_Flow_Graph.setObjectName(u"actionControl_Flow_Graph")
        self.actionSource_Code_Mapping = QAction(MainWindow)
        self.actionSource_Code_Mapping.setObjectName(u"actionSource_Code_Mapping")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 0, 131, 20))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(40, 31, 1041, 671))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.textEdit.setFont(font1)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 31, 31, 671))
        self.textBrowser.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 710, 75, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
        self.menuDebugging = QMenu(self.menubar)
        self.menuDebugging.setObjectName(u"menuDebugging")
        self.menuMap = QMenu(self.menubar)
        self.menuMap.setObjectName(u"menuMap")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDebugging.menuAction())
        self.menubar.addAction(self.menuMap.menuAction())
        self.menuDebugging.addAction(self.actionStart)
        self.menuMap.addAction(self.actionSource_Code_Mapping)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.actionControl_Flow_Graph.setText(QCoreApplication.translate("MainWindow", u"Control Flow Graph", None))
        self.actionSource_Code_Mapping.setText(QCoreApplication.translate("MainWindow", u"Source Code Mapping", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  Intermidiate Code", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuDebugging.setTitle(QCoreApplication.translate("MainWindow", u"Debugging", None))
        self.menuMap.setTitle(QCoreApplication.translate("MainWindow", u"Map", None))
    # retranslateUi

