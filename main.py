import sys
import os

from PyQt6.QtGui import QIntValidator
from dotenv import load_dotenv

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal, QSortFilterProxyModel
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
        self.anylyze_by_vuz = Models.AnalyzeByVuz(self.db, self.w_root)
        self.anylyze_by_grnti = Models.AnalyzeByGRNTI(self.db, self.w_root)
        self.anylyze_by_char = Models.AnalyzeByCHAR(self.db, self.w_root)

        self.w_root.tableView.setModel(self.nir_model)
        self.w_root.tableView_2.setModel(self.fin_vuz_model)
        self.w_root.tableView_3.setModel(self.vuz_model)
        self.w_root.tableView_4.setModel(self.anylyze_by_vuz)
        self.w_root.tableView_9.setModel(self.anylyze_by_grnti)
        self.w_root.tableView_10.setModel(self.anylyze_by_char)

        # self.w_root.tableView.sortByColumn(3, Qt.SortOrder.AscendingOrder)
        self.onNirHeaderClicked(3)
        self.w_root.tableView_2.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.w_root.tableView_3.sortByColumn(3, Qt.SortOrder.AscendingOrder)
        self.w_root.tableView.horizontalHeader().sectionClicked.connect(self.onNirHeaderClicked)

        self.w_root.action_1.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_1))
        self.w_root.action_2.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_2))
        self.w_root.action_3.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_3))

        update_table_views(self.w_root.tableView, self.w_root.tableView_2, self.w_root.tableView_3,
                           self.w_root.tableView_4, self.w_root.tableView_9, self.w_root.tableView_10)

        self.delete_accept_form = Widgets.DeleteAccept()
        self.edit_record_nir_form = Widgets.EditRecordNir()
        self.filter_nir_form = Widgets.FilterNir(self.vuz_model, self.nir_model)

        # Анализ
        self.w_root.action_4.triggered.connect(
            lambda: self.anylyze_by_vuz.update(self.nir_model.query().lastQuery(), self.filter_nir_form))
        self.w_root.action_4.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_4))

        self.w_root.action_5.triggered.connect(
            lambda: self.anylyze_by_grnti.update(self.nir_model.query().lastQuery(), self.filter_nir_form))
        self.w_root.action_5.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_5))

        self.w_root.action_6.triggered.connect(
            lambda: self.anylyze_by_char.update(self.nir_model.query().lastQuery(), self.filter_nir_form))
        self.w_root.action_6.triggered.connect(lambda: self.w_root.stackedWidget.setCurrentWidget(self.w_root.page_11))

        self.w_root.pushButton.clicked.connect(self.open_edit_record_nir)
        self.w_root.pushButton_3.clicked.connect(self.delete_records_nir)
        self.w_root.pushButton_2.clicked.connect(self.add_record_nir_form)
        self.w_root.pushButton_4.clicked.connect(self.open_filter_form)
        self.w_root.pushButton_5.clicked.connect(self.sort_by_codvuz_rnw)
        self.w_root.pushButton_6.clicked.connect(self.nir_model.reset_filters)

        self.w.show()

    def open_filter_form(self):
        # self.filter_nir_form.reset()
        self.filter_nir_form.w.show()

    def add_record_nir_form(self):
        self.edit_record_nir_form.clear_form()
        self.edit_record_nir_form.w_root.pushButton_2.setText('Добавить запись')
        self.edit_record_nir_form.w_root.label_2.setText('Добавление записи')

        vuzes = self.vuz_model.get_list_vuzes_z2()

        ## ВУЗ
        self.edit_record_nir_form.w_root.comboBox_2.addItems(vuzes)

        self.edit_record_nir_form.w_root.pushButton_2.disconnect()
        self.edit_record_nir_form.w_root.pushButton_2.clicked.connect(lambda: self.change_add_record(add=True))

        self.edit_record_nir_form.w.show()

    def open_edit_record_nir(self):
        self.edit_record_nir_form.w_root.pushButton_2.setText('Принять')
        self.edit_record_nir_form.w_root.label_2.setText('Редактирование записи')
        self.edit_record_nir_form.clear_form()

        selected_rows = self.w_root.tableView.selectionModel().selectedRows()

        if len(selected_rows) == 1:
            edit_row = self.nir_model.row_from_index(selected_rows[0])
            vuzes = self.vuz_model.get_list_vuzes_z2()

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
            if not edited_row['f18']:
                edited_row['f18'] = 0

            if not add:
                print(edited_row)
                self.nir_model.update_row(edited_row, changed_codvuz, changed_rnw)
                self.edit_record_nir_form.w.close()

            else:
                if not self.nir_model.add_row(edited_row):
                    self.edit_record_nir_form.w_root.label_11.setText(
                        'НИР с таким номером в данном вузе уже существует')
                else:
                    self.nir_model.reset_filters()
                    self.edit_record_nir_form.w.close()

            self.fin_vuz_model.recalculate_row([edited_row])
            row_to_select = self.nir_model.get_indexes_of_rows(edited_row)
            self.w_root.tableView.selectRow(row_to_select)
            self.w_root.tableView.scrollTo(self.nir_model.index(row_to_select, 0))

    def delete_records_nir(self):
        def accept_delete(rows_to_delete):
            # self.nir_model.delete_rows(rows_to_delete)
            self.nir_model.delete_rows(self.w_root.tableView.selectionModel().selectedRows())
            self.fin_vuz_model.recalculate_row(rows_to_delete)
            self.delete_accept_form.w.close()

        rows_to_delete = []
        for index in self.w_root.tableView.selectionModel().selectedRows():
            rows_to_delete.append(self.nir_model.row_from_index(index))
        if rows_to_delete:
            self.delete_accept_form.w.show()
            self.delete_accept_form.w_root.pushButton.clicked.connect(lambda: accept_delete(rows_to_delete))

    def onNirHeaderClicked(self, index):
        self.w_root.tableView.scrollTo(self.nir_model.index(0, 0))
        if self.nir_model.sortOrder[index] == 'ASC':
            self.nir_model.sortOrder[index] = 'DESC'
            self.w_root.tableView.horizontalHeader().setSortIndicator(index, Qt.SortOrder.AscendingOrder)
        else:
            self.nir_model.sortOrder[index] = 'ASC'
            self.w_root.tableView.horizontalHeader().setSortIndicator(index, Qt.SortOrder.DescendingOrder)

        if index != 0:
            self.w_root.tableView.horizontalHeader().setSortIndicatorShown(True)
            self.nir_model.orderByQuery = f""" ORDER BY {self.nir_model.record().fieldName(index) + ' ' + self.nir_model.sortOrder[index]} """
        else:
            self.nir_model.orderByQuery = f""" ORDER BY codvuz {self.nir_model.sortOrder[index]}, LENGTH(rnw), rnw """

        self.nir_model.update_model()

    def sort_by_codvuz_rnw(self):
        self.w_root.tableView.scrollTo(self.nir_model.index(0, 0))
        self.w_root.tableView.horizontalHeader().setSortIndicator(0, Qt.SortOrder.AscendingOrder)
        self.nir_model.orderByQuery = f""" ORDER BY codvuz, LENGTH(rnw), rnw """
        self.nir_model.update_model()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
