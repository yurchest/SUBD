from PyQt6.QtCore import Qt
from PyQt6.QtSql import *


class FinanceVuzModel(QSqlTableModel):
    header_data = {'codvuz': "Код \nвуза",
                   "z2": "Сокращенное \nнаим. вуза",
                   "z3": "Плановый объем \nфинансирования",
                   "z18": "Фактический объем \nфинансирования",
                   "numworks": "Количество НИР \nпо плану",
                   }

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setTable("Tp_fv")
        self.change_column_name()
        self.select()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self):
        query = QSqlQuery("SELECT * FROM Tp_fv")
        self.setQuery(query)
