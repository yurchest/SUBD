from typing import Dict

from PyQt6.QtGui import QIntValidator

from UI import py_ui
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtWidgets


class EditRecordNir(QWidget):
    isAdd = False

    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QDialog()
        self.w_root = py_ui.edit_record_nir.Ui_Form()
        self.w_root.setupUi(self.w)

        self.w_root.lineEdit_5.setValidator(QIntValidator())
        self.w_root.lineEdit_4.setInputMask("00.00.00")
        self.w_root.lineEdit_9.setInputMask("00.00.00")

        self.w_root.pushButton_3.clicked.connect(lambda: self.w.close())

    def set_vales(self, values: Dict) -> None:
        ## ВУЗ
        self.w_root.comboBox_2.addItems(values['vuzes'])
        self.w_root.comboBox_2.setCurrentText(values['current_vuz'])

        ## Регистрационный номер
        self.w_root.lineEdit.setText(values['reg_nomer'])

        ## Характер НИР
        match values['type_of_nir']:
            case 'Ф':
                char_nir = 'Фундаментальное исследование'
            case 'П':
                char_nir = 'Прикладное исследование'
            case 'Р':
                char_nir = 'Экспериментальная разработка'
        self.w_root.comboBox.setCurrentText(char_nir)

        ## Руководитель НИР
        self.w_root.lineEdit_7.setText(values['head_name'])

        ## Код темы по ГРНТИ
        self.w_root.lineEdit_4.setText(values['key_grnti'].partition(';')[0])
        self.w_root.lineEdit_9.setText(values['key_grnti'].partition(';')[2])

        ## Плановый объем финансирования
        self.w_root.lineEdit_5.setText(str(values['amount_of_funding']))

        ## Наименование НИР
        self.w_root.textEdit_2.setText(values['name_of_nir'])

        ## Должность руководителя
        self.w_root.lineEdit_8.setText(values['head_position'])

    def clear_form(self):
        self.w_root.comboBox_2.setCurrentIndex(0)
        self.w_root.lineEdit.setText('')
        self.w_root.comboBox.setCurrentIndex(0)
        self.w_root.lineEdit_7.setText('')
        self.w_root.lineEdit_4.setText('')
        self.w_root.lineEdit_9.setText('')
        self.w_root.lineEdit_5.setText('')
        self.w_root.textEdit_2.setText('')
        self.w_root.lineEdit_8.setText('')
        self.w_root.lineEdit_8.setText('')
        self.w_root.label_11.setText('')
        self.w_root.label_6.setStyleSheet('')

    def get_grnti(self):
        if self.w_root.lineEdit_9.text() == '..':
            kod_grnti = self.w_root.lineEdit_4.text()
            if len(kod_grnti) != 8:
                self.w_root.label_6.setStyleSheet('color: rgb(255, 0, 0);')
                kod_grnti = False
        else:
            kod_grnti = self.w_root.lineEdit_4.text() + ';' + self.w_root.lineEdit_9.text()
            if len(kod_grnti) != 17:
                self.w_root.label_6.setStyleSheet('color: rgb(255, 0, 0);')
                kod_grnti = False
        return kod_grnti

    def get_char_nir(self):
        match self.w_root.comboBox.currentText():
            case 'Фундаментальное исследование':
                return 'Ф'
            case 'Прикладное исследование':
                return 'П'
            case 'Экспериментальная разработка':
                return 'Р'

    def get_data(self):
        error = False
        key_grnti = None
        if self.get_grnti():
            key_grnti = self.get_grnti()
        else:
            error = True
        edited_row = \
            {
                'codvuz': None,
                'rnw': self.w_root.lineEdit.text(),
                'f1': self.get_char_nir(),
                'z2': self.w_root.comboBox_2.currentText(),
                'f6': self.w_root.lineEdit_7.text(),
                'f10': key_grnti,
                'f2': self.w_root.textEdit_2.toPlainText(),
                'f7': self.w_root.lineEdit_8.text(),
                'f18': self.w_root.lineEdit_5.text(),
                'error': error,
            }

        return edited_row

    # def get_codvuz_from_z1



