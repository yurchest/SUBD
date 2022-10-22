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

    def get_list_vuzes_z2(self) -> dict:
        query = QSqlQuery()
        query.exec("SELECT z2 FROM VUZ")
        vuzes = []
        while query.next():
            vuzes.append(query.value(0))
        return vuzes

    def get_codvuz_from_z2(self, z2):
        query = QSqlQuery(f"SELECT codvuz FROM VUZ WHERE z2='{z2}'")
        while query.next():
            result = query.value(0)
        return result

    def get_distinct_data(self, data_to_filter):
        for k in data_to_filter.keys():
            if not data_to_filter[k]:
                data_to_filter[k] = ''
        data = \
            {
                'codvuz': [],
                "z1": [],
                "z1full": [],
                "z2": [],
                "region": [],
                "city": [],
                "status": [],
                "obl": [],
                "oblname": [],
                "gr_ved": [],
                "prof": [],
            }

        query_in = f"""SELECT * FROM VUZ 
                        WHERE region LIKE '{data_to_filter['region']}%'
                        AND z2 LIKE '{data_to_filter['z2']}%'
                        AND city LIKE '{data_to_filter['city']}%'
                        AND oblname LIKE '{data_to_filter['oblname']}%'
                        """

        for i, k in enumerate(data.keys()):
            query = QSqlQuery(f"""SELECT DISTINCT {k} FROM ({query_in})""")
            while query.next():
                data[k].append(query.value(0))
        return data
