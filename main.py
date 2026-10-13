import random
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel
from main_window_ui import Ui_MainWindow as homeUi
from play_window_ui2 import Ui_PlayWindow as playUi
from result_window_ui import Ui_MainWindow as resUi

COLORS = {
    2: "#F6FFEA",
    4: "#D6DFCB",
    8: "#FFDE96",
    16: "#F9C34E",
    32: "#FF6264",
    64: "#C93638",
    128: "#87E9FF",
    256: "#62C4DA",
    512: "#CA8AFA",
    1024: "#852CC8",
    2048: "#CEE568",
}
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


tiles = [
    [ui.square, ui.square_2, ui.square_3, ui.square_4, ui.square_5],
    [ui.square_6, ui.square_7, ui.square_8, ui.square_9, ui.square_10],
    [ui.square_11, ui.square_12, ui.square_13, ui.square_14, ui.square_15],
    [ui.square_16, ui.square_17, ui.square_18, ui.square_19, ui.square_20],
    [ui.square_21, ui.square_22, ui.square_23, ui.square_24, ui.square_25],
]

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
