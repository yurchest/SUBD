from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator, QColor, QBrush
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtWidgets import QWidget, QComboBox

from Models import VuzModel, NirModel
from UI import py_ui


class FilterNir(QWidget):
    data_to_filter = \
        {
            "z2": None,
            "region": None,
            "city": None,
            "oblname": None,
        }

    def __init__(self, vuz_model: VuzModel, nir_model: NirModel):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.filter_nir.Ui_Form()
        self.w_root.setupUi(self.w)

        self.vuz_model = vuz_model
        self.nir_model = nir_model

        self.vuz_data = self.vuz_model.get_distinct_data(self.data_to_filter)
        self.set_values(self.vuz_data)

        self.w_root.lineEdit.setMaxLength(2)
        self.w_root.lineEdit.setValidator(QIntValidator())

        self.w_root.comboBox_2.currentTextChanged.connect(self.region_changed)
        self.w_root.comboBox_3.currentTextChanged.connect(self.oblname_changed)
        self.w_root.comboBox_4.currentTextChanged.connect(self.city_changed)
        self.w_root.comboBox_5.currentTextChanged.connect(self.vuz_changed)

        self.w_root.pushButton_4.clicked.connect(self.reset)
        self.w_root.pushButton_2.clicked.connect(self.filter_update_nir_table)
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

    def set_values(self, values, key_of_none_combobox=None):

        comboboxes = {
            'region': 'comboBox_2',
            'oblname': 'comboBox_3',
            'city': 'comboBox_4',
            'z2': 'comboBox_5',
        }

        self.w_root.comboBox_2.blockSignals(True)
        self.w_root.comboBox_3.blockSignals(True)
        self.w_root.comboBox_4.blockSignals(True)
        self.w_root.comboBox_5.blockSignals(True)

        self.clear_inputs()

        self.w_root.comboBox_2.addItem('')
        self.w_root.comboBox_3.addItem('')
        self.w_root.comboBox_4.addItem('')
        self.w_root.comboBox_5.addItem('')

        self.w_root.comboBox_2.addItems(values['region'])
        self.w_root.comboBox_3.addItems(values['oblname'])
        self.w_root.comboBox_4.addItems(values['city'])
        self.w_root.comboBox_5.addItems(values['z2'])

        for combobox in self.w.findChildren(QComboBox):
            if combobox.count() == 2:
                combobox.setCurrentText(combobox.itemText(1))
            if key_of_none_combobox:
                if comboboxes[key_of_none_combobox] == combobox.objectName():
                    combobox.setCurrentText('')

        self.w_root.lineEdit.setText('')

        self.w_root.comboBox_2.blockSignals(False)
        self.w_root.comboBox_3.blockSignals(False)
        self.w_root.comboBox_4.blockSignals(False)
        self.w_root.comboBox_5.blockSignals(False)

    def vuz_combobox_changed(self, value, key_of_combobox):
        priority_less = ["region", "oblname", "city", "z2"]
        values_to_distinct = {
            "region": None,
            "oblname": None,
            "city": None,
            "z2": None,
        }
        if value:
            values_to_distinct.update({key_of_combobox: value})
            self.set_values(self.vuz_model.get_distinct_data(values_to_distinct))
        else:
            values_to_distinct = {
                "region": self.w_root.comboBox_2.currentText(),
                "oblname": self.w_root.comboBox_3.currentText(),
                "city": self.w_root.comboBox_4.currentText(),
                "z2": self.w_root.comboBox_5.currentText(),
            }
            stop = False
            for priority in priority_less:
                if priority == key_of_combobox:
                    stop = True
                if stop:
                    values_to_distinct.update({priority: None})
            self.set_values(self.vuz_model.get_distinct_data(values_to_distinct), key_of_none_combobox=key_of_combobox)

    def filter_update_nir_table(self):
        where_filter = (f""" codvuz IN (
                                SELECT codvuz 
                                FROM VUZ
                                WHERE region LIKE '{self.w_root.comboBox_2.currentText()}%'
                                AND z2 LIKE '{self.w_root.comboBox_5.currentText()}%'
                                AND city LIKE '{self.w_root.comboBox_4.currentText()}%'
                                AND oblname LIKE '{self.w_root.comboBox_3.currentText()}%'
                                ) 
                                AND (SUBSTR(f10, 1, 2)  LIKE '%{self.w_root.lineEdit.text()}%'
                                OR SUBSTR(f10, 10, 11) LIKE '%{self.w_root.lineEdit.text()}%')
                                """)

        query = QSqlQuery(f"""SELECT * FROM Tp_nir 
                                WHERE {where_filter}
                                """)
        data = []
        while query.next():
            data.append(query.value(0))
        if not data:
            self.w_root.label_8.setText("Записей с такими параметрами не найдено")
            self.w_root.label_8.setText("Записей с такими параметрами не найдено")
        else:
            self.w_root.label_8.setText("")
            self.nir_model.setFilter(where_filter)
            self.w.close()

    def region_changed(self, value):
        self.vuz_combobox_changed(value, 'region')

    def oblname_changed(self, value):
        self.vuz_combobox_changed(value, 'oblname')

    def city_changed(self, value):
        self.vuz_combobox_changed(value, 'city')

    def vuz_changed(self, value):
        self.vuz_combobox_changed(value, 'z2')
