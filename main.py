import random
import sys
from ctypes.wintypes import SIZE

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel,QKeyEvent
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

game_matrix = [] # Числа
tile_widgets = [] # Квадраты
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

tiles = [
    [gameUi.square, gameUi.square_2, gameUi.square_3, gameUi.square_4, gameUi.square_5],
    [gameUi.square_6, gameUi.square_7, gameUi.square_8, gameUi.square_9, gameUi.square_10],
    [gameUi.square_11, gameUi.square_12, gameUi.square_13, gameUi.square_14, gameUi.square_15],
    [gameUi.square_16, gameUi.square_17, gameUi.square_18, gameUi.square_19, gameUi.square_20],
    [gameUi.square_21, gameUi.square_22, gameUi.square_23, gameUi.square_24, gameUi.square_25],
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
