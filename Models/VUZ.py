from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class VuzModel(QSqlTableModel):
    header_data = {'codvuz': "Код \nвуза",
                   "z1": "Наименование \nвуза ",
                   "z1full": "Полное \nнаименование вуза ",
                   "z2": "Сокращенное \nнаименование",
                   "region": "Федеральный \nокруг",
                   "city": "Город",
                   "status": "Статус",
                   "obl": "Код субъекта \nфедерации",
                   "oblname": "Субъект \nфедерации",
                   "gr_ved": "gr_ved",
                   "prof": "prof",
                   }

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setTable("VUZ")
        self.change_column_name()
        self.select()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self):
        query = QSqlQuery("SELECT * FROM VUZ")
        self.setQuery(query)

    def get_list_vuzes(self) -> list:
        query = QSqlQuery()
        query.exec("SELECT * FROM VUZ")
        vuzes = []
        while query.next():
            vuzes.append(query.value(3))
        return vuzes

    def get_codvuz_from_z2(self, z2):
        query = QSqlQuery(f"SELECT codvuz FROM VUZ WHERE z2='{z2}'")
        while query.next():
            result = query.value(0)
        return result
