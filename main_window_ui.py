# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
    QSizePolicy, QVBoxLayout, QWidget)
import play_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 844)
        MainWindow.setStyleSheet(u"background-color: #FFDE96")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-10, 0, 811, 844))
        self.menu = QVBoxLayout(self.layoutWidget)
        self.menu.setObjectName(u"menu")
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.title_lb = QLabel(self.layoutWidget)
        self.title_lb.setObjectName(u"title_lb")
        self.title_lb.setStyleSheet(u"font-size:90pt;\n"
"font-weight: bold;\n"
"color: #FA855A;\n"
"background:none;")
        self.title_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.menu.addWidget(self.title_lb)

        self.pole_lb = QLabel(self.layoutWidget)
        self.pole_lb.setObjectName(u"pole_lb")
        self.pole_lb.setStyleSheet(u"font-size:24pt;\n"
"font-weight:bold;\n"
"color:#7A905E;\n"
"background:none")
        self.pole_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.menu.addWidget(self.pole_lb)

        self.play_btn = QPushButton(self.layoutWidget)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setStyleSheet(u"background:none")
        icon = QIcon()
        icon.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_btn.setIcon(icon)
        self.play_btn.setIconSize(QSize(200, 200))

        self.menu.addWidget(self.play_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
#endif // QT_CONFIG(whatsthis)
        self.title_lb.setText(QCoreApplication.translate("MainWindow", u"2048", None))
        self.pole_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 5x5", None))
        self.play_btn.setText("")
    # retranslateUi

