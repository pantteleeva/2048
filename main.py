import random
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel,QKeyEvent
from main_window_ui import Ui_MainWindow as homeUi
from play_window_ui2 import Ui_PlayWindow as playUi
from result_window_ui import Ui_MainWindow as resUi
from logic import *

app = QApplication(sys.argv)

def play():
    mainWin.close()
    gameWin.show()

def home():
    gameWin.close()
    resultWin.close()
    mainWin.show()

def restart():
    gameWin.close()
    gameWin.show()

def exit_game():
    mainWin.close()
    gameWin.close()
    resultWin.close()


mainWin = QMainWindow()
mainUi = homeUi()
mainUi.setupUi(mainWin)

gameWin = QMainWindow()
gameUi =playUi()
gameUi.setupUi(gameWin)

gameUi.b_home.setFocusPolicy(Qt.FocusPolicy.NoFocus)
gameUi.pushButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
gameUi.pushButton_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

resultWin = QMainWindow()
resultUi = resUi()
resultUi.setupUi(resultWin)

mainUi.play_btn.clicked.connect(play)
resultUi.b_home.clicked.connect(home)
resultUi.b_restart.clicked.connect(restart)
resultUi.b_exit.clicked.connect(exit_game)
gameUi.b_home.clicked.connect(home)
gameUi.pushButton.clicked.connect(restart)
gameUi.pushButton_2.clicked.connect(exit_game)



def handle_key_press(event: QKeyEvent):
    if event.key() == Qt.Key.Key_Left:
        print("Лево")
    elif event.key() == Qt.Key.Key_Right:
        print("Право")
    elif event.key() == Qt.Key.Key_Up:
        print("Вверх")
    elif event.key() == Qt.Key.Key_Down:
        print("Низ")
gameWin.keyPressEvent = handle_key_press

if __name__ == "__main__":
    mainWin.show()
    sys.exit(app.exec())
