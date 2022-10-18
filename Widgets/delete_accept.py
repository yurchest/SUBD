from UI import py_ui
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal


class DeleteAccept(QWidget):

    delete_confirmation = pyqtSignal(bool)

    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.delete_accept.Ui_Dialog()
        self.w_root.setupUi(self.w)

        # self.w_root.pushButton.clicked.connect()
        # self.w_root.pushButton_2.clicked.connect(lambda : self.w.close())
