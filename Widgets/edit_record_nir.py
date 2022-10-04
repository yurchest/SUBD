from UI.py_ui.edit_record_nir import *
from PyQt6.QtWidgets import QWidget


class EditRecordNir(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = Ui_Form()
        self.w_root.setupUi(self.w)

        self.w_root.pushButton_3.clicked.connect(lambda: self.w.close())
