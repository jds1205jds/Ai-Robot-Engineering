# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'control_button.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_go = QPushButton(self.centralwidget)
        self.btn_go.setObjectName(u"btn_go")
        self.btn_go.setGeometry(QRect(190, 150, 61, 61))
        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(190, 240, 61, 61))
        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(190, 330, 61, 61))
        self.btn_right = QPushButton(self.centralwidget)
        self.btn_right.setObjectName(u"btn_right")
        self.btn_right.setGeometry(QRect(280, 240, 61, 61))
        self.btn_left = QPushButton(self.centralwidget)
        self.btn_left.setObjectName(u"btn_left")
        self.btn_left.setGeometry(QRect(100, 240, 61, 61))
        self.service_btn = QGroupBox(self.centralwidget)
        self.service_btn.setObjectName(u"service_btn")
        self.service_btn.setGeometry(QRect(460, 90, 171, 161))
        self.btn_reset = QPushButton(self.service_btn)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(30, 60, 95, 25))
        self.btn_add = QPushButton(self.service_btn)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(30, 100, 95, 25))
        self.service_btn_2 = QGroupBox(self.centralwidget)
        self.service_btn_2.setObjectName(u"service_btn_2")
        self.service_btn_2.setGeometry(QRect(460, 290, 171, 161))
        self.btn_navi = QPushButton(self.service_btn_2)
        self.btn_navi.setObjectName(u"btn_navi")
        self.btn_navi.setGeometry(QRect(30, 30, 95, 25))
        self.progressBar = QProgressBar(self.service_btn_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 60, 118, 23))
        self.progressBar.setValue(24)
        self.btn_squre = QPushButton(self.service_btn_2)
        self.btn_squre.setObjectName(u"btn_squre")
        self.btn_squre.setGeometry(QRect(20, 100, 51, 51))
        self.btn_triangle = QPushButton(self.service_btn_2)
        self.btn_triangle.setObjectName(u"btn_triangle")
        self.btn_triangle.setGeometry(QRect(100, 100, 51, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statbar = QStatusBar(MainWindow)
        self.statbar.setObjectName(u"statbar")
        MainWindow.setStatusBar(self.statbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_go.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.btn_back.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.btn_right.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.btn_left.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.service_btn.setTitle(QCoreApplication.translate("MainWindow", u"SERVICE BUTTON", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"OBSTACLE", None))
        self.service_btn_2.setTitle(QCoreApplication.translate("MainWindow", u"ACTION BUTTON", None))
        self.btn_navi.setText(QCoreApplication.translate("MainWindow", u"NAVIGATE", None))
        self.btn_squre.setText(QCoreApplication.translate("MainWindow", u"\u25a0", None))
        self.btn_triangle.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
    # retranslateUi

