# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import icons_play_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 572)
        MainWindow.setStyleSheet(u"background-color: #FFDE96;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_6 = QSpacerItem(229, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 6, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 3, 0, 1, 2)

        self.label_score = QLabel(self.centralwidget)
        self.label_score.setObjectName(u"label_score")
        self.label_score.setStyleSheet(u"font-size: 50pt;\n"
"color: #C93638;\n"
"font-weight: bold;\n"
"font-family: Inter;")

        self.gridLayout.addWidget(self.label_score, 2, 3, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_home = QPushButton(self.centralwidget)
        self.b_home.setObjectName(u"b_home")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_home.setIcon(icon)
        self.b_home.setIconSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.b_home)

        self.b_restart = QPushButton(self.centralwidget)
        self.b_restart.setObjectName(u"b_restart")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/restart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_restart.setIcon(icon1)
        self.b_restart.setIconSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.b_restart)

        self.b_exit = QPushButton(self.centralwidget)
        self.b_exit.setObjectName(u"b_exit")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_exit.setIcon(icon2)
        self.b_exit.setIconSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.b_exit)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(330, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 35pt;\n"
"color: #7A905E;\n"
"font-weight: bold;\n"
"font-family: Inter;")

        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(294, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(137, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 8, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(165, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 3, 7, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(192, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(122, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 70pt;\n"
"color: #C93638;\n"
"font-weight: bold;\n"
"font-family: Inter;\n"
"")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0438\u0433\u0440\u044b", None))
        self.label_score.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.b_home.setText("")
        self.b_restart.setText("")
        self.b_exit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"score", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

