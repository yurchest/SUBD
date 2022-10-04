import sys
import os
from dotenv import load_dotenv

from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView
from UI.py_ui.form import *
from Models.NIR import NirModel

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
        self.w_root = Ui_MainWindow()
        self.w_root.setupUi(self.w)
        print(os.environ.get('DB_URL'))
        self.db = connect_db(os.getenv('DB_URL'))

        nir_model = NirModel(self.db)
        self.w_root.tableView.setModel(nir_model)
        self.init_tableview_nir()

        self.w.show()

    def init_tableview_nir(self):
        self.w_root.tableView.setSortingEnabled(True)
        self.w_root.tableView.horizontalHeader().moveSection(0, 1)
        self.resize_columns_nir()
        self.w_root.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def resize_columns_nir(self):
        ### NIR TABLE
        for i in [0, 1, 2, 3, 4, 5, 7, 8]:
            self.w_root.tableView.resizeColumnToContents(i)
        self.w_root.tableView.setColumnWidth(6, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
