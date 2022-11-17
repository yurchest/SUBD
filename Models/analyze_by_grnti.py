from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class AnalyzeByGRNTI(QSqlQueryModel):
    header_data = {'grnti': "Код \nГРНТИ",
                   "kolvo": "Кол-во \nНИР",
                   "sum": "Плановый объем \nфинансирования",
                   "rubrika": "Рубрика",
                   }

    def __init__(self, db, main_app):
        super().__init__()
        self.db = db
        self.main_app = main_app
        self.update()
        self.change_column_name()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self, last_query="""SELECT * FROM Tp_nir"""):

        self.setQuery(f"""
                        SELECT grntirub.codrub as grnti,
                        rubrika,
                        COUNT(Tp_Nir.codvuz) as kolvo,
                        COALESCE(sum(Tp_Nir.f18), 0)as sum 
                        FROM grntirub INNER JOIN ({last_query}) as Tp_nir
                        ON (grntirub.codrub = SUBSTR(Tp_nir.f10, 1, 2)
                        OR grntirub.codrub = SUBSTR(Tp_nir.f10, 10, 2))
                        GROUP BY grntirub.codrub
                        """)

