from PyQt6.QtGui import QIntValidator

from UI import py_ui
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets


class EditRecordNir(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.edit_record_nir.Ui_Form()
        self.w_root.setupUi(self.w)

        self.w_root.lineEdit_5.setValidator(QIntValidator())
        self.w_root.lineEdit_4.setInputMask("00.00.00")
        self.w_root.lineEdit_9.setInputMask("00.00.00")

        self.w_root.pushButton_3.clicked.connect(lambda: self.w.close())
