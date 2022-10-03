import sys
import os
from database_sqlalchemy import session

from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlRelationalTableModel
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QTableView, QHeaderView
from form import *
from ListClasses import VuzList
from database_sqlalchemy import VUZ
from PyQt6.QtCore import Qt
from class_db_qsqltablemodel import NirModel
from settings import DB_URL


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QMainWindow()
        self.w_root = Ui_MainWindow()
        self.w_root.setupUi(self.w)

        self.connect_db(DB_URL)

        nirModel = NirModel(self.db)
        self.w_root.tableView.setModel(nirModel)
        self.w_root.tableView.horizontalHeader().moveSection(0, 1)

        self.w.show()

    def connect_db(self, db_name=None):
        if os.path.isfile(DB_URL):
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(db_name)
            if not self.db.open():
                print('ERROR CONNECTION TO DATABASE')
                self.w_root.statusbar.showMessage("Ошибка подключения к БД ", 2500)
            else:
                self.w_root.statusbar.showMessage("Подключение к базе прошло успешно ", 2500)
        else:
            self.w_root.statusbar.showMessage(f"Базы данных {DB_URL} не существует", 2500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
