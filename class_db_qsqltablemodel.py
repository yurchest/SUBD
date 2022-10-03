from PyQt6.QtSql import *
from PyQt6.QtCore import Qt

class NirModel(QSqlTableModel):
    header_data = {'codvuz': "Код вуза",
                   "rnw": "регистрационный номер НИР",
                   "f1": "характер  НИР",
                   "z2": "сокращенное наименование вуза",
                   "f6": "руководитель НИР",
                   "f10": "код1 темы по ГРНТИ",
                   "f2": "наименование НИР",
                   "f7": "должность руководителя",
                   "f18": "плановый объем финансирования",
                   "f11": "код2 темы по ГРНТИ",
                   }

    def __init__(self, db):
        super().__init__()
        self.db = db
        if self.db.open():
            print('Success')
        self.setTable("Tp_nir")

        self.select()
