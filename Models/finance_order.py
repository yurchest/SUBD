from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class FinanceOrder(QSqlQueryModel):
    header_data = {
        "z2": "ВУЗ",
        "z5": "Фактический \nобъем",
    }

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_update()
        self.change_column_name()


    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self, percent):
        if percent:
            self.setQuery(f"""
                            WITH temp as (SELECT z2, CAST(ROUND(z3*({float(percent) / 100})) AS INTEGER) as z5 FROM Tp_fv)
                            SELECT z2, z5 from temp
                            Union All
                            SELECT 'Итого', SUM(z5)
                            FROM temp
                            """)


    def init_update(self):
        self.setQuery(f"""
                        SELECT z2, z18 as z5 FROM Tp_fv
                        Union all
                        SELECT 'Итого', SUM(z18)
                        FROM Tp_fv
                        """)

