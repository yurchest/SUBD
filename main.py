import sys
import os

from PyQt6.QtGui import QIntValidator
from dotenv import load_dotenv

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView
from UI import py_ui
from utils.update_table_views import update_table_views
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
        self.fin_vuz_model = Models.FinanceVuzModel(self.db)

        self.w_root.tableView.setModel(self.nir_model)
        self.w_root.tableView_2.setModel(self.fin_vuz_model)
        self.w_root.tableView_3.setModel(self.vuz_model)


        self.w_root.tableView.sortByColumn(3, Qt.SortOrder.AscendingOrder)
        self.w_root.tableView_2.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.w_root.tableView_3.sortByColumn(3, Qt.SortOrder.AscendingOrder)

        self.w_root.action_1.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_1))
        self.w_root.action_2.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_2))
        self.w_root.action_3.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_3))

        update_table_views(self.w_root.tableView, self.w_root.tableView_2, self.w_root.tableView_3)

        self.delete_accept_form = Widgets.DeleteAccept()
        self.edit_record_nir_form = Widgets.EditRecordNir()

        self.w_root.pushButton.clicked.connect(self.open_edit_record_nir)
        self.w_root.pushButton_3.clicked.connect(self.delete_records_nir)
        self.w_root.pushButton_2.clicked.connect(self.add_record_nir_form)

        self.w.show()

    def add_record_nir_form(self):
        self.edit_record_nir_form.clear_form()
        self.edit_record_nir_form.w_root.pushButton_2.setText('Добавить запись')
        self.edit_record_nir_form.w_root.label_2.setText('Добавление записи')

        vuzes = self.vuz_model.get_list_vuzes()

        ## ВУЗ
        self.edit_record_nir_form.w_root.comboBox_2.addItems(vuzes)

        self.edit_record_nir_form.w_root.pushButton_2.disconnect()
        self.edit_record_nir_form.w_root.pushButton_2.clicked.connect(lambda: self.change_add_record(add=True))

        self.edit_record_nir_form.w.show()

    def open_edit_record_nir(self):
        self.edit_record_nir_form.clear_form()

        selected_rows = self.w_root.tableView.selectionModel().selectedRows()

        if len(selected_rows) == 1:
            edit_row = self.nir_model.row_from_index(selected_rows[0])
            vuzes = self.vuz_model.get_list_vuzes()

            values_to_init_in_form = {
                "vuzes": vuzes,
                "current_vuz": edit_row['z2'],
                "reg_nomer": edit_row['rnw'],
                "type_of_nir": edit_row['f1'],
                "head_name": edit_row['f6'],
                "key_grnti": edit_row['f10'],
                "amount_of_funding": edit_row['f18'],
                "name_of_nir": edit_row['f2'],
                "head_position": edit_row['f7'],
            }

            self.edit_record_nir_form.set_vales(values_to_init_in_form)
            # ----------------------------------------------------------
            try:
                self.edit_record_nir_form.w_root.pushButton_2.clicked.disconnect()
            except:
                pass
            self.edit_record_nir_form.w_root.pushButton_2.clicked.connect(
                lambda: self.change_add_record(add=False, changed_codvuz=edit_row['codvuz'],
                                               changed_rnw=edit_row['rnw'], selected_row=selected_rows[0].row()))

            self.edit_record_nir_form.w.show()

    def change_add_record(self, add, changed_codvuz=0, changed_rnw='0', selected_row=None):

        edited_row = self.edit_record_nir_form.get_data()
        if not edited_row['error']:
            edited_row['codvuz'] = self.vuz_model.get_codvuz_from_z2(edited_row['z2'])

            if not add:
                self.nir_model.update_row(edited_row, changed_codvuz, changed_rnw)
                self.edit_record_nir_form.w.close()

            else:
                if not self.nir_model.add_row(edited_row):
                    self.edit_record_nir_form.w_root.label_11.setText('Запись уже существует')
                else:
                    # TODO
                    #  self.w_root.tableView.selectRow()
                    self.edit_record_nir_form.w.close()
            self.fin_vuz_model.recalculate_row([edited_row])
            update_table_views(self.w_root.tableView, self.w_root.tableView_2, self.w_root.tableView_3)
            row_to_select = self.nir_model.get_indexes_of_rows(edited_row)
            self.w_root.tableView.selectRow(row_to_select)
            self.w_root.tableView.scrollTo(self.nir_model.index(row_to_select, 0))

    def delete_records_nir(self):
        def accept_delete(rows_to_delete):
            self.nir_model.delete_rows(rows_to_delete)
            update_table_views(self.w_root.tableView, self.w_root.tableView_2, self.w_root.tableView_3)
            self.fin_vuz_model.recalculate_row(rows_to_delete)
            self.delete_accept_form.w.close()

        rows_to_delete = []
        for index in self.w_root.tableView.selectionModel().selectedRows():
            rows_to_delete.append(self.nir_model.row_from_index(index))
        if rows_to_delete:
            self.delete_accept_form.w.show()
            self.delete_accept_form.w_root.pushButton.clicked.connect(lambda: accept_delete(rows_to_delete))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
