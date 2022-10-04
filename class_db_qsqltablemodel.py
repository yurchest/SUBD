from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class NirModel(QSqlTableModel):
    header_data = {'codvuz': "Код вуза",
                   "rnw": "Регистрационный номер НИР",
                   "f1": "Характер  НИР",
                   "z2": "Сокращенное наименование вуза",
                   "f6": "Руководитель НИР",
                   "f10": "Код темы по ГРНТИ",
                   "f2": "Наименование НИР",
                   "f7": "Должность руководителя",
                   "f18": "Плановый объем финансирования",
                   }

    def __init__(self, db):
        super().__init__()
        self.db = db
        if self.db.open():
            print('Success')
        self.setTable("Tp_nir")
        self.change_column_name()

        self.select()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

