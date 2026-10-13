import random
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel



mainWin = QMainWindow()
mainUi = Ui_MainWindow()
mainUi.setupUi(mainWin)

gameWin = QMainWindow()
gameUi = Ui_MainWindow()
gameUi.setupUi(gameWin)

resultWin = QMainWindow()
resultUi = Ui_MainWindow()
resultUi.setupUi(resultWin)

mainUi.play_btn.clicked.connect(play)
resultUi.b_home.clicked.connect(home)
resultUi.b_restart.clicked.connect(restart)
resultUi.b_exit.clicked.connect(exit_game)
gameUi.play_btn.clicked.connect(home)
gameUi.play_btn.clicked.connect(restart)
gameUi.b_exit.clicked.connect(exit_game)


def play():
    mainWin.hide()
    gameWin.show()

def home():
    gameWin.hide()
    resultWin.hide()
    mainWin.show()

def restart():
    gameWin.hide()
    gameWin.show()

def exit_game():
    mainWin.close()
    gameWin.close()
    resultWin.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin.show()
    sys.exit(app.exec())
