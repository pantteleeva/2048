# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import play_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 585)
        MainWindow.setStyleSheet(u"background-color: #FFDE96")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(66, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_lb = QLabel(self.centralwidget)
        self.title_lb.setObjectName(u"title_lb")
        self.title_lb.setStyleSheet(u"font-size:90pt;\n"
"font-weight: bold;\n"
"color: #FA855A;\n"
"background:none;")
        self.title_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_lb)

        self.pole_lb = QLabel(self.centralwidget)
        self.pole_lb.setObjectName(u"pole_lb")
        self.pole_lb.setStyleSheet(u"font-size:24pt;\n"
"font-weight:bold;\n"
"color:#7A905E;\n"
"background:none")
        self.pole_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.pole_lb)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.play_btn = QPushButton(self.centralwidget)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setStyleSheet(u"background:none")
        icon = QIcon()
        icon.addFile(u":/icons/icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_btn.setIcon(icon)
        self.play_btn.setIconSize(QSize(200, 200))

        self.verticalLayout_2.addWidget(self.play_btn)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(67, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
#endif // QT_CONFIG(whatsthis)
        self.title_lb.setText(QCoreApplication.translate("MainWindow", u"2048", None))
        self.pole_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0435 5x5", None))
        self.play_btn.setText("")
    # retranslateUi

