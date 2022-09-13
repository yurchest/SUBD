import sys

from PyQt6.QtSql import QSqlTableModel
from PyQt6.QtWidgets import QApplication, QWidget
from form import *
from gui_functions import *
from db_functions import *


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.w = QtWidgets.QMainWindow()
        self.w_root = Ui_MainWindow()
        self.w_root.setupUi(self.w)

        if not connect_db("Databases/my_bd.db"):
            sys.exit(-1)
        table_sql = QSqlTableModel()
        table_sql.setTable("VUZ")
        table_sql.select()
        self.w_root.tableView.setModel(table_sql)

        # with Database() as db:
        #     rows = db.execute("SELECT z2 FROM Tp_fv")

        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
