from UI import py_ui
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets


class DeleteAccept(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.delete_accept.Ui_Dialog()
        self.w_root.setupUi(self.w)

        self.w_root.pushButton_2.clicked.connect(lambda: self.w.close())
