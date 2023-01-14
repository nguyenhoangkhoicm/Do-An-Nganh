
# pip install pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.vaui import Ui_SIRI
from PyQt5.QtCore import pyqtSignal, Qt, QThread
from PyQt5.QtGui import QMovie
import os


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_SIRI()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton.clicked.connect(self.run)
       # run ảnh gif
        self.movie = QMovie("./imgqrc/va (1).gif")
        self.uic.label_2.setMovie(self.movie)
        self.movie.start()

    def run(self):
        os.system("py main.py")

    def show(self):
        # command to run
        self.main_win.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())
