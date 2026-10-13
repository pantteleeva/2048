# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'play_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_play_rc

class Ui_PlayWindow(object):
    def setupUi(self, PlayWindow):
        if not PlayWindow.objectName():
            PlayWindow.setObjectName(u"PlayWindow")
        PlayWindow.resize(1167, 654)
        PlayWindow.setStyleSheet(u"background-color:#FFDE96")
        self.centralwidget = QWidget(PlayWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pole = QFrame(self.centralwidget)
        self.pole.setObjectName(u"pole")
        self.pole.setGeometry(QRect(310, 60, 571, 581))
        self.pole.setMaximumSize(QSize(16777214, 16777215))
        self.pole.setSizeIncrement(QSize(500, 500))
        self.pole.setStyleSheet(u"background-color:#FA855A;\n"
"border:none;\n"
"border-radius: 20px")
        self.pole.setFrameShape(QFrame.Shape.StyledPanel)
        self.pole.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.pole)
        self.gridLayout.setObjectName(u"gridLayout")
        self.square_12 = QLabel(self.pole)
        self.square_12.setObjectName(u"square_12")
        self.square_12.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_12, 2, 1, 1, 1)

        self.square_21 = QLabel(self.pole)
        self.square_21.setObjectName(u"square_21")
        self.square_21.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_21, 4, 0, 1, 1)

        self.square_4 = QLabel(self.pole)
        self.square_4.setObjectName(u"square_4")
        self.square_4.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_4, 0, 3, 1, 1)

        self.square = QLabel(self.pole)
        self.square.setObjectName(u"square")
        self.square.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square, 0, 0, 1, 1)

        self.square_2 = QLabel(self.pole)
        self.square_2.setObjectName(u"square_2")
        self.square_2.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_2, 0, 1, 1, 1)

        self.square_16 = QLabel(self.pole)
        self.square_16.setObjectName(u"square_16")
        self.square_16.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_16, 3, 0, 1, 1)

        self.square_11 = QLabel(self.pole)
        self.square_11.setObjectName(u"square_11")
        self.square_11.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_11, 2, 0, 1, 1)

        self.square_7 = QLabel(self.pole)
        self.square_7.setObjectName(u"square_7")
        self.square_7.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_7, 1, 1, 1, 1)

        self.square_18 = QLabel(self.pole)
        self.square_18.setObjectName(u"square_18")
        self.square_18.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_18, 3, 2, 1, 1)

        self.square_10 = QLabel(self.pole)
        self.square_10.setObjectName(u"square_10")
        self.square_10.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_10, 1, 4, 1, 1)

        self.square_17 = QLabel(self.pole)
        self.square_17.setObjectName(u"square_17")
        self.square_17.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_17, 3, 1, 1, 1)

        self.square_23 = QLabel(self.pole)
        self.square_23.setObjectName(u"square_23")
        self.square_23.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_23, 4, 2, 1, 1)

        self.square_8 = QLabel(self.pole)
        self.square_8.setObjectName(u"square_8")
        self.square_8.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_8, 1, 2, 1, 1)

        self.square_15 = QLabel(self.pole)
        self.square_15.setObjectName(u"square_15")
        self.square_15.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_15, 2, 4, 1, 1)

        self.square_14 = QLabel(self.pole)
        self.square_14.setObjectName(u"square_14")
        self.square_14.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_14, 2, 3, 1, 1)

        self.square_20 = QLabel(self.pole)
        self.square_20.setObjectName(u"square_20")
        self.square_20.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_20, 3, 4, 1, 1)

        self.square_19 = QLabel(self.pole)
        self.square_19.setObjectName(u"square_19")
        self.square_19.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_19, 3, 3, 1, 1)

        self.square_24 = QLabel(self.pole)
        self.square_24.setObjectName(u"square_24")
        self.square_24.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_24, 4, 3, 1, 1)

        self.square_22 = QLabel(self.pole)
        self.square_22.setObjectName(u"square_22")
        self.square_22.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_22, 4, 1, 1, 1)

        self.square_9 = QLabel(self.pole)
        self.square_9.setObjectName(u"square_9")
        self.square_9.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_9, 1, 3, 1, 1)

        self.square_3 = QLabel(self.pole)
        self.square_3.setObjectName(u"square_3")
        self.square_3.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_3, 0, 2, 1, 1)

        self.square_5 = QLabel(self.pole)
        self.square_5.setObjectName(u"square_5")
        self.square_5.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_5, 0, 4, 1, 1)

        self.square_13 = QLabel(self.pole)
        self.square_13.setObjectName(u"square_13")
        self.square_13.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_13, 2, 2, 1, 1)

        self.square_6 = QLabel(self.pole)
        self.square_6.setObjectName(u"square_6")
        self.square_6.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_6, 1, 0, 1, 1)

        self.square_25 = QLabel(self.pole)
        self.square_25.setObjectName(u"square_25")
        self.square_25.setStyleSheet(u"background-color: #EDEAEA;\n"
"border:none;\n"
"border-radius: 20px")
        self.square_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.square_25, 4, 4, 1, 1)

        self.title_lb = QLabel(self.centralwidget)
        self.title_lb.setObjectName(u"title_lb")
        self.title_lb.setGeometry(QRect(20, 30, 271, 121))
        self.title_lb.setStyleSheet(u"font-size:90pt;\n"
"font-weight: bold;\n"
"color: #C93638;\n"
"background:none;")
        self.title_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_home = QPushButton(self.centralwidget)
        self.b_home.setObjectName(u"b_home")
        self.b_home.setGeometry(QRect(90, 200, 121, 101))
        self.b_home.setStyleSheet(u"background:none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_home.setIcon(icon)
        self.b_home.setIconSize(QSize(100, 100))
        self.title_lb_2 = QLabel(self.centralwidget)
        self.title_lb_2.setObjectName(u"title_lb_2")
        self.title_lb_2.setGeometry(QRect(900, 60, 271, 150))
        self.title_lb_2.setStyleSheet(u"font-size:65pt;\n"
"font-weight: bold;\n"
"color: #7A905E;\n"
"background:none;")
        self.title_lb_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.count_lb = QLabel(self.centralwidget)
        self.count_lb.setObjectName(u"count_lb")
        self.count_lb.setGeometry(QRect(910, 40, 241, 161))
        self.count_lb.setStyleSheet(u"font-size:20pt;\n"
"font-weight: bold;\n"
"color: #C93638;\n"
"background-color:#FA855A;\n"
"border-radius:20px;")
        self.count_lb.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(970, 240, 122, 228))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/restart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton_2)

        PlayWindow.setCentralWidget(self.centralwidget)
        self.pole.raise_()
        self.title_lb.raise_()
        self.b_home.raise_()
        self.count_lb.raise_()
        self.title_lb_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(PlayWindow)

        QMetaObject.connectSlotsByName(PlayWindow)
    # setupUi

    def retranslateUi(self, PlayWindow):
        PlayWindow.setWindowTitle(QCoreApplication.translate("PlayWindow", u"\u042d\u043a\u0440\u0430\u043d \u0438\u0433\u0440\u044b", None))
        self.square_12.setText("")
        self.square_21.setText("")
        self.square_4.setText("")
        self.square.setText("")
        self.square_2.setText("")
        self.square_16.setText("")
        self.square_11.setText("")
        self.square_7.setText("")
        self.square_18.setText("")
        self.square_10.setText("")
        self.square_17.setText("")
        self.square_23.setText("")
        self.square_8.setText("")
        self.square_15.setText("")
        self.square_14.setText("")
        self.square_20.setText("")
        self.square_19.setText("")
        self.square_24.setText("")
        self.square_22.setText("")
        self.square_9.setText("")
        self.square_3.setText("")
        self.square_5.setText("")
        self.square_13.setText("")
        self.square_6.setText("")
        self.square_25.setText("")
        self.title_lb.setText(QCoreApplication.translate("PlayWindow", u"2048", None))
        self.b_home.setText("")
        self.title_lb_2.setText(QCoreApplication.translate("PlayWindow", u"2048", None))
        self.count_lb.setText(QCoreApplication.translate("PlayWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0441\u0447\u0451\u0442", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

