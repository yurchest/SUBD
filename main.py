import sys
import os
from database_sqlalchemy import session

from PyQt6.QtSql import QSqlTableModel, QSqlDatabase, QSqlRelationalTableModel
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QTableView, QHeaderView, QMessageBox
from form import *
from ListClasses import VuzList
from database_sqlalchemy import VUZ
from PyQt6.QtCore import Qt
from class_db_qsqltablemodel import NirModel
from settings import DB_URL


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

        self.db = connect_db(DB_URL)

        nirModel = NirModel(self.db)
        self.w_root.tableView.setModel(nirModel)
        self.w_root.tableView.horizontalHeader().moveSection(0, 1)
        self.w_root.tableView.resizeColumnsToContents()

        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
