from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class AnalyzeByVuz(QSqlQueryModel):
    header_data = {'codvuz': "Код \nвуза",
                   "rnw": "Регистрационный \nномер НИР",
                   "f1": "Характер  \nНИР",
                   "z2": "Сокращенное \nнаим. вуза",
                   "f6": "Руководитель НИР",
                   "f10": "Код темы по ГРНТИ",
                   "f2": "Наименование НИР",
                   "f7": "Должность \nруководителя",
                   "f18": "Плановый объем \nфинансирования",
                   }

    def __init__(self, db):
        super().__init__()
        self.db = db
        # self.update()
        # self.change_column_name()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self, last_query):
        print(last_query)
        self.setQuery(f"""SELECT codvuz,COUNT(*), sum(f18)
                        FROM ({last_query})
                        GROUP BY codvuz""")
