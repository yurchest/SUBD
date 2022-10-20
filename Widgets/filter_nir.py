from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QColor, QBrush
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
        self.set_values(self.vuz_data)

        self.w_root.lineEdit.setInputMask("00.00.00")

        self.w_root.comboBox_2.currentTextChanged.connect(self.region_changed)
        self.w_root.comboBox_3.currentTextChanged.connect(self.oblname_changed)
        self.w_root.comboBox_4.currentTextChanged.connect(self.city_changed)
        self.w_root.comboBox_5.currentTextChanged.connect(self.vuz_changed)

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
        self.w_root.comboBox_2.setStyleSheet('')
        self.w_root.comboBox_3.setStyleSheet('')
        self.w_root.comboBox_4.setStyleSheet('')
        self.w_root.comboBox_5.setStyleSheet('')
        self.w_root.lineEdit.setText('')

    def set_values(self, values):
        self.w_root.comboBox_2.blockSignals(True)
        self.w_root.comboBox_3.blockSignals(True)
        self.w_root.comboBox_4.blockSignals(True)
        self.w_root.comboBox_5.blockSignals(True)

        self.clear_inputs()

        if self.data_to_filter['region']:
            self.w_root.comboBox_2.addItems(self.vuz_data['region'])
            self.w_root.comboBox_2.setItemData(self.w_root.comboBox_2.findText(self.data_to_filter['region']),
                                               QColor.fromRgb(124, 252, 0), Qt.ItemDataRole.BackgroundRole)
            self.w_root.comboBox_2.setCurrentText(self.data_to_filter['region'])
        else:
            self.w_root.comboBox_2.addItems(values['region'])

        if self.data_to_filter['oblname']:
            self.w_root.comboBox_3.addItems(self.vuz_data['oblname'])
            self.w_root.comboBox_3.setItemData(self.w_root.comboBox_3.findText(self.data_to_filter['oblname']),
                                               QColor.fromRgb(124, 252, 0), Qt.ItemDataRole.BackgroundRole)
            self.w_root.comboBox_3.setCurrentText(self.data_to_filter['oblname'])
        else:
            self.w_root.comboBox_3.addItems(values['oblname'])

        if self.data_to_filter['city']:
            self.w_root.comboBox_4.addItems(self.vuz_data['city'])
            self.w_root.comboBox_4.setItemData(self.w_root.comboBox_4.findText(self.data_to_filter['city']),
                                               QColor.fromRgb(124, 252, 0), Qt.ItemDataRole.BackgroundRole)
            self.w_root.comboBox_4.setCurrentText(self.data_to_filter['city'])
        else:
            self.w_root.comboBox_4.addItems(values['city'])

        if self.data_to_filter['z2']:
            self.w_root.comboBox_5.addItems(self.vuz_data['z2'])
            self.w_root.comboBox_5.setItemData(self.w_root.comboBox_5.findText(self.data_to_filter['z2']),
                                               QColor.fromRgb(124, 252, 0), Qt.ItemDataRole.BackgroundRole)
            self.w_root.comboBox_5.setCurrentText(self.data_to_filter['z2'])
        else:
            self.w_root.comboBox_5.addItems(values['z2'])

        self.w_root.lineEdit.setText('')

        self.w_root.comboBox_2.blockSignals(False)
        self.w_root.comboBox_3.blockSignals(False)
        self.w_root.comboBox_4.blockSignals(False)
        self.w_root.comboBox_5.blockSignals(False)

    def region_changed(self):
        self.data_to_filter['city'] = None
        self.data_to_filter['z2'] = None
        self.data_to_filter['oblname'] = None
        self.data_to_filter['region'] = self.w_root.comboBox_2.currentText()
        distincted_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        self.set_values(distincted_data)

    def oblname_changed(self):
        self.data_to_filter['region'] = None
        self.data_to_filter['city'] = None
        self.data_to_filter['z2'] = None
        self.data_to_filter['oblname'] = self.w_root.comboBox_3.currentText()
        distincted_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        self.data_to_filter['region'] = distincted_data['region'][0]
        self.set_values(distincted_data)

    def city_changed(self):
        self.data_to_filter['region'] = None
        self.data_to_filter['oblname'] = None
        self.data_to_filter['z2'] = None
        self.data_to_filter['city'] = self.w_root.comboBox_4.currentText()
        distincted_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        self.data_to_filter['region'] = distincted_data['region'][0]
        self.data_to_filter['oblname'] = distincted_data['oblname'][0]
        self.set_values(distincted_data)

    def vuz_changed(self):
        self.data_to_filter['region'] = None
        self.data_to_filter['oblname'] = None
        self.data_to_filter['city'] = None
        self.data_to_filter['z2'] = self.w_root.comboBox_5.currentText()
        distincted_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        self.data_to_filter['region'] = distincted_data['region'][0]
        self.data_to_filter['oblname'] = distincted_data['oblname'][0]
        self.data_to_filter['city'] = distincted_data['city'][0]
        self.set_values(distincted_data)
