from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget

from Models import VuzModel
from UI import py_ui


class FilterNir(QWidget):
    data_to_filter = \
        {
            "z2": None,
            "region": None,
            "city": None,
            "oblname": None,
        }

    def __init__(self, vuz_model: VuzModel):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.filter_nir.Ui_Form()
        self.w_root.setupUi(self.w)
        self.vuz_model = vuz_model

        self.vuz_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        print(self.vuz_data)
        self.set_values(self.vuz_data)

        self.w_root.lineEdit.setInputMask("00.00.00")

        self.w_root.comboBox_2.currentTextChanged.connect(self.region_changed)
        self.w_root.pushButton_4.clicked.connect(self.reset)
        self.w_root.pushButton_3.clicked.connect(lambda: self.w.close())

    def reset(self):
        self.data_to_filter = \
            {
                "z2": None,
                "region": None,
                "city": None,
                "oblname": None,
            }
        self.set_values(self.vuz_data)

    def clear_inputs(self):
        self.w_root.comboBox_2.clear()
        self.w_root.comboBox_3.clear()
        self.w_root.comboBox_4.clear()
        self.w_root.comboBox_5.clear()
        self.w_root.lineEdit.setText('')

    def set_values(self, values):
        self.w_root.comboBox_2.blockSignals(True)
        self.w_root.comboBox_3.blockSignals(True)
        self.w_root.comboBox_4.blockSignals(True)
        self.w_root.comboBox_5.blockSignals(True)

        self.clear_inputs()

        self.w_root.comboBox_2.addItems(values['region'])
        self.w_root.comboBox_3.addItems(values['oblname'])
        self.w_root.comboBox_4.addItems(values['city'])
        self.w_root.comboBox_5.addItems(values['z2'])
        self.w_root.lineEdit.setText('')

        self.w_root.comboBox_2.blockSignals(False)
        self.w_root.comboBox_3.blockSignals(False)
        self.w_root.comboBox_4.blockSignals(False)
        self.w_root.comboBox_5.blockSignals(False)

    def region_changed(self):
        self.data_to_filter['region'] = self.w_root.comboBox_2.currentText()
        filtered_data = self.vuz_model.filter_x(self.data_to_filter)
        self.set_values()