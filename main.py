import sys
import os

from PyQt6.QtGui import QIntValidator
from dotenv import load_dotenv

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView
from UI import py_ui
import Models
from PyQt6.QtCore import Qt

# from Widgets.edit_record_nir import EditRecordNir
import Widgets

load_dotenv()


def connect_db(db_name=None):
    try:
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(db_name)
    except:
        msgBox = QMessageBox()
        msgBox.setText("Ошибка подключения к БД")
        msgBox.exec()
        sys.exit()
    return db


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QMainWindow()
        self.w_root = py_ui.form.Ui_MainWindow()
        self.w_root.setupUi(self.w)

        self.db = connect_db(os.getenv('DB_URL'))
        self.nir_model = Models.NirModel(self.db)
        self.vuz_model = Models.VuzModel(self.db)
        self.w_root.tableView.setModel(self.nir_model)
        self.update_nir_view()

        self.delete_accept_form = Widgets.DeleteAccept()
        self.edit_record_nir_form = Widgets.EditRecordNir()

        self.w_root.pushButton.clicked.connect(self.open_edit_record_nir)
        self.w_root.pushButton_3.clicked.connect(self.delete_records_nir)

        self.w.show()

    def update_nir_view(self):
        self.w_root.tableView.setSortingEnabled(True)
        self.w_root.tableView.horizontalHeader().moveSection(3, 0)
        self.w_root.tableView.horizontalHeader().moveSection(4, 1)
        self.w_root.tableView.horizontalHeader().moveSection(8, 2)
        self.w_root.tableView.horizontalHeader().moveSection(6, 3)
        self.w_root.tableView.horizontalHeader().moveSection(7, 4)
        self.w_root.tableView.horizontalHeader().moveSection(8, 5)
        self.w_root.tableView.horizontalHeader().setFixedHeight(60)
        self.resize_columns_nir()
        self.w_root.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def resize_columns_nir(self):
        for i in range(9):
            self.w_root.tableView.resizeColumnToContents(i)
            self.w_root.tableView.setColumnWidth(i, self.w_root.tableView.columnWidth(i) - 10)
        self.w_root.tableView.setColumnWidth(6, 200)

    def open_edit_record_nir(self):
        rows_to_edit = []
        for index in self.w_root.tableView.selectionModel().selectedRows():
            rows_to_edit.append(
                {'codvuz': self.nir_model.data(self.nir_model.index(index.row(), 0)),
                 'rnw': self.nir_model.data(self.nir_model.index(index.row(), 1)),
                 'f1': self.nir_model.data(self.nir_model.index(index.row(), 2)),
                 'z2': self.nir_model.data(self.nir_model.index(index.row(), 3)),
                 'f6': self.nir_model.data(self.nir_model.index(index.row(), 4)),
                 'f10': self.nir_model.data(self.nir_model.index(index.row(), 5)),
                 'f2': self.nir_model.data(self.nir_model.index(index.row(), 6)),
                 'f7': self.nir_model.data(self.nir_model.index(index.row(), 7)),
                 'f18': self.nir_model.data(self.nir_model.index(index.row(), 8)),
                 })
        if len(rows_to_edit) == 1:
            edit_row = rows_to_edit[0]
            query = QSqlQuery()
            query.exec("SELECT * FROM VUZ")
            vuzes = []
            while query.next():
                vuzes.append(query.value(3))

            ## ВУЗ
            self.edit_record_nir_form.w_root.comboBox_2.addItems(vuzes)
            self.edit_record_nir_form.w_root.comboBox_2.setCurrentText(edit_row['z2'])

            ## Регисрационный номер
            self.edit_record_nir_form.w_root.lineEdit.setText(edit_row['rnw'])

            ## Характер НИР
            match edit_row['f1']:
                case 'Ф':
                    char_nir = 'Фундаментальное исследование'
                case 'П':
                    char_nir = 'Прикладное исследование'
                case 'Р':
                    char_nir = 'Экспериментальная разработка'
            self.edit_record_nir_form.w_root.comboBox.setCurrentText(char_nir)

            ## Наименование ВУЗа
            query.exec(f"SELECT z1 FROM VUZ WHERE codvuz={edit_row['codvuz']}")
            while query.next():
                current_vuz = query.value(0)
            self.edit_record_nir_form.w_root.textEdit.setText(current_vuz)

            ## Руководитель НИР
            self.edit_record_nir_form.w_root.lineEdit_7.setText(edit_row['f6'])

            ## Код темы по ГРНТИ
            self.edit_record_nir_form.w_root.lineEdit_4.setText(edit_row['f10'].partition(';')[0])
            self.edit_record_nir_form.w_root.lineEdit_9.setText(edit_row['f10'].partition(';')[2])

            ## Плановый объем финансирования
            self.edit_record_nir_form.w_root.lineEdit_5.setValidator(QIntValidator())
            self.edit_record_nir_form.w_root.lineEdit_5.setText(str(edit_row['f18']))

            ## Наименование НИР
            self.edit_record_nir_form.w_root.textEdit_2.setText(edit_row['f2'])

            ## Должность руководителя
            self.edit_record_nir_form.w_root.lineEdit_8.setText(edit_row['f7'])

            # ----------------------------------------------------------

            self.edit_record_nir_form.w_root.pushButton_2.clicked.connect(self.change_record_button)

            self.edit_record_nir_form.w.show()

    def change_record_button(self):
        query = QSqlQuery(f"SELECT * FROM VUZ WHERE z2='{self.edit_record_nir_form.w_root.comboBox_2.currentText()}'")
        while query.next():
            codvuz = query.value(0)

        match self.edit_record_nir_form.w_root.comboBox.currentText():
            case 'Фундаментальное исследование':
                char_nir = 'Ф'
            case 'Прикладное исследование':
                char_nir = 'П'
            case 'Экспериментальная разработка':
                char_nir = 'Р'

        edited_row = \
            {
                'codvuz': codvuz,
                'rnw': self.edit_record_nir_form.w_root.lineEdit.text(),
                'f1': char_nir,
                'z2': self.nir_model.data(self.nir_model.index(index.row(), 3)),
                'f6': self.nir_model.data(self.nir_model.index(index.row(), 4)),
                'f10': self.nir_model.data(self.nir_model.index(index.row(), 5)),
                'f2': self.nir_model.data(self.nir_model.index(index.row(), 6)),
                'f7': self.nir_model.data(self.nir_model.index(index.row(), 7)),
                'f18': self.nir_model.data(self.nir_model.index(index.row(), 8)),
            }

    def delete_records_nir(self):
        def accept_delete(rows_to_delete):
            for row in rows_to_delete:
                query = QSqlQuery(f"DELETE FROM TP_nir WHERE codvuz={row['codvuz']} AND rnw='{row['rnw']}'")
                self.nir_model.setQuery(query)
            self.nir_model.update()
            self.update_nir_view()
            # self.w_root.tableView.setModel(self.nir_model)

            self.delete_accept_form.w.close()

        rows_to_delete = []
        for index in self.w_root.tableView.selectionModel().selectedRows():
            rows_to_delete.append(
                {'codvuz': self.nir_model.data(self.nir_model.index(index.row(), 0)),
                 'rnw': self.nir_model.data(self.nir_model.index(index.row(), 1))
                 })
        if rows_to_delete:
            self.delete_accept_form.w.show()
            self.delete_accept_form.w_root.pushButton.clicked.connect(lambda: accept_delete(rows_to_delete))
            self.delete_accept_form.w_root.pushButton_2.clicked.connect(lambda: self.delete_accept_form.w.close())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
