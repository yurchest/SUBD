import sys
from PyQt6.QtWidgets import QApplication, QWidget
from form import *


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QMainWindow()
        self.w_root = Ui_MainWindow()
        self.w_root.setupUi(self.w)

        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
