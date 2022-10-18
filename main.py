import sys
import os
from dotenv import load_dotenv

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView
from UI import py_ui
from Models.NIR import NirModel
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
        self.nir_model = NirModel(self.db)
        self.w_root.tableView.setModel(self.nir_model)
        self.update_nir_view()

        self.edit_record_nir_form = None

        self.delete_accept_form = Widgets.DeleteAccept()



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
        if self.edit_record_nir_form is None:
            self.edit_record_nir_form = Widgets.EditRecordNir()
            self.edit_record_nir_form.w.exec()
        else:
            self.edit_record_nir_form.close()
            self.edit_record_nir_form = None
            self.open_edit_record_nir()

    def delete_records_nir(self):
        def accept_delete(rows_to_delete):
            for row in rows_to_delete:
                query = QSqlQuery(f"DELETE FROM TP_nir WHERE codvuz={row['codvuz']} AND rnw='{row['rnw']}'")
                # qury2 = QSqlQuery()
                # qury2.exec(f"SELECT * FROM TP_nir WHERE codvuz={row['codvuz']} and rnw='{row['rnw']}'")
                # while qury2.next():
                #     print(qury2.value(0))
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
