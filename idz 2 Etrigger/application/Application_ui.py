# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Application.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import STATES_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.BackImg = QLabel(self.centralwidget)
        self.BackImg.setObjectName(u"BackImg")
        self.BackImg.setGeometry(QRect(-60, -80, 821, 571))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 100, 61, 71))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 400, 61, 71))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 240, 111, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BackImg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/states/STATE1110.svg\"/></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u044b\u043a\u0430\u043b\u043a\u0430 \n"
" 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u044b\u043a\u0430\u043b\u043a\u0430 \n"
"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u044b\u043a\u043d\u0443\u0442\u044c \u043e\u0431\u0435\n"
"\u0442\u044b\u043a\u0430\u043b\u043a\u0438", None))
    # retranslateUi

