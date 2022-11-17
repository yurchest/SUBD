from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class AnalyzeByVuz(QSqlQueryModel):
    header_data = {'z2': "Наименование \nвуза",
                   "kolvo": "Кол-во \nНИР",
                   "sum": "Плановый объем \nфинансирования",
                   }

    def __init__(self, db, main_app):
        super().__init__()
        self.main_app = main_app
        self.db = db
        self.update()
        self.change_column_name()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self, last_query=f"""SELECT * FROM Tp_nir"""):

        # self.setQuery(f"""SELECT VUZ.codvuz,
        #             COUNT(Tp_nir.codvuz) as kolvo,
        #             COALESCE(sum(Tp_nir.f18), 0) as sum
        #             FROM VUZ LEFT JOIN ({last_query}) as Tp_nir
        #             ON VUZ.codvuz = Tp_nir.codvuz
        #             GROUP BY VUZ.codvuz
        #             """)

        self.setQuery(f"""
                            SELECT Tp_nir.z2,
                            COUNT(Tp_nir.codvuz) as kolvo,
                            COALESCE(sum(Tp_nir.f18), 0) as sum
                            FROM ({last_query}) as Tp_nir
                            GROUP BY Tp_nir.z2
                        """)


