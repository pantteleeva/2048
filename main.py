import random
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel
from main_window_ui import Ui_MainWindow as homeUi
from play_window_ui2 import Ui_PlayWindow as playUi
from result_window_ui import Ui_MainWindow as resUi

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


if __name__ == "__main__":
    mainWin.show()
    sys.exit(app.exec())
