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

    def recalculate_row(self, edited_row):
        query = QSqlQuery(f"""
                SELECT SUM(f18), COUNT(*)
                FROM Tp_nir 
                WHERE codvuz = {edited_row['codvuz']}
        """)
        while query.next():
            sum_f18 = query.value(0)
            count = query.value(1)

        query = QSqlQuery(f"""
                UPDATE Tp_fv
                SET z3 = {sum_f18},
                    numworks = {count}
                WHERE codvuz={edited_row['codvuz']}
        """)
        self.setQuery(query)
        self.update()
        pass
