import sys
import os

from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog
from form import *
from gui_functions import *


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QMainWindow()
        self.w_root = Ui_MainWindow()
        self.w_root.setupUi(self.w)
        if os.path.isfile("Databases/my_bd.db"):
            self.connect_db("Databases/my_bd.db")
        self.w_root.pushButton.clicked.connect(lambda: self.connect_db())
        # with Database() as db:
        #     rows = db.execute("SELECT z2 FROM Tp_fv")

        self.w.show()

    def connect_db(self, db_name=None):
        if db_name is None: db_name = self.get_db_name()
        if db_name:
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(db_name)
            if not self.db.open():
                print('ERROR CONNECTION TO DATABASE')
                self.w_root.statusbar.showMessage("Ошибка подключения к БД ", 2500)
            else:
                self.w_root.statusbar.showMessage("Подключение к базе прошло успешно ", 2500)
                self.set_tables()
                self.w_root.pushButton.setEnabled(False)

    def set_tables(self):
        tables = self.db.tables()
        self.w_root.tabWidget.clear()
        for table in tables:
            globals()['self.w_root.tab_%s' % table] = QtWidgets.QWidget()
            globals()['self.w_root.table_view_%s' % table] = QtWidgets.QTableView()
            globals()['self.w_root.table_view_%s' % table].setSortingEnabled(True)
            self.w_root.tabWidget.addTab(globals()['self.w_root.tab_%s' % table], table)
            table_sql = QSqlTableModel()
            table_sql.setTable(table)
            table_sql.select()
            lay_tableview = QtWidgets.QVBoxLayout(globals()['self.w_root.tab_%s' % table])
            lay_tableview.addWidget(globals()['self.w_root.table_view_%s' % table])
            globals()['self.w_root.table_view_%s' % table].setModel(table_sql)

    def get_db_name(self):
        self.w_root.statusbar.showMessage("Открытие БД ... ", 2500)
        db_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "./", )
        if db_name:
            return db_name


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
