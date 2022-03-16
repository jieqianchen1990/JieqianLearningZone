from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(0, 0, 1920, 1080)
    win.setWindowTitle("This is Jieqian's Window")

    win1 = QPushButton("Push me")

    win.show()
    win1.show()
    sys.exit(app.exec())


window()
