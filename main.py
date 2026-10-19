import random
import sys
import icons_play_rc
from ctypes.wintypes import SIZE
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel,QKeyEvent
from main_window_ui import Ui_MainWindow as homeUi
from play_window_ui import Ui_PlayWindow as playUi
from result_window_ui import Ui_MainWindow as resUi
from logic import *

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
matrix = [[0] * 5 for _ in range(5)]
score = 0


def draw():
    for r in range(5):
        for c in range(5):
            v = matrix[r][c]
            text = str(v) if v else ""
            color = COLORS.get(v, "#EDEAEA")
            tiles[r][c].setText(text)
            tiles[r][c].setStyleSheet(f"background-color: {color}; font-size: 36pt; border-radius: 20px; color: black; font-weight: bold;")

def play():
    global matrix, score
    mainWin.close()
    matrix = create_new_matrix() 
    score = 0
    gameUi.title_lb_2.setText(f"{score}")
    draw()
    gameWin.show()


def home():
    gameWin.close()
    resultWin.close()
    mainWin.show()

def restart():
    global matrix, score
    resultWin.close()
    matrix = create_new_matrix() 
    score = 0
    gameUi.title_lb_2.setText(f"{score}")
    draw()
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
    global matrix, score
    old_matrix = [row[:] for row in matrix]
    turn_score = 0

    if event.key() == Qt.Key.Key_Left:
        matrix, turn_score = move_matrix(matrix, "left")
    elif event.key() == Qt.Key.Key_Right:
        matrix, turn_score = move_matrix(matrix, "right")
    elif event.key() == Qt.Key.Key_Up:
        matrix, turn_score = move_matrix(matrix, "up")
    elif event.key() == Qt.Key.Key_Down:
        matrix, turn_score = move_matrix(matrix, "down")
    else:
        return

    if matrix != old_matrix:
        score += turn_score
        draw()
        gameUi.title_lb_2.setText(f"{score}")

        if check_win(matrix):
            show_result(is_win=True)
            return

        if check_lose(matrix):
            show_result(is_win=False)
            return



gameWin.keyPressEvent = handle_key_press

def show_result(is_win):
    global score
    gameWin.close()
    
    if is_win:
        resultUi.label_score.setText("Крутой")
    else:
        resultUi.label_score.setText("Лох цветочный")
        
    resultUi.label_2.setText(str(score)) 
    
    resultWin.show()




if __name__ == "__main__":
    mainWin.show()
    sys.exit(app.exec())
