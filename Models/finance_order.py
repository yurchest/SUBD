from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class FinanceOrder(QSqlQueryModel):
    header_data = {
        "z2": "ВУЗ",
        "z3": "Фактический объем",
    }

    def __init__(self, db):
        super().__init__()
        self.db = db

    def update(self, percent):
        if percent:
            self.setQuery(f"""
                            SELECT z2, CAST(ROUND(z3*({float(percent)/100})) AS INTEGER) as z3 FROM Tp_fv
                            """)



