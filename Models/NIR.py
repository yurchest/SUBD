from typing import Dict

from PyQt6.QtSql import *
from PyQt6.QtCore import Qt, QSortFilterProxyModel


class NirModel(QSqlTableModel):
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
        self.setTable("Tp_nir")
        self.change_column_name()
        self.select()

    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])

    def update(self):
        query = QSqlQuery("SELECT * FROM Tp_nir")
        self.setQuery(query)

    def row_from_index(self, index) -> Dict:
        return {'codvuz': self.data(self.index(index.row(), 0)),
                'rnw': self.data(self.index(index.row(), 1)),
                'f1': self.data(self.index(index.row(), 2)),
                'z2': self.data(self.index(index.row(), 3)),
                'f6': self.data(self.index(index.row(), 4)),
                'f10': self.data(self.index(index.row(), 5)),
                'f2': self.data(self.index(index.row(), 6)),
                'f7': self.data(self.index(index.row(), 7)),
                'f18': self.data(self.index(index.row(), 8)),
                }

    def get_all(self):
        query = QSqlQuery("SELECT * FROM Tp_nir")
        self.setQuery(query)

    def delete_rows(self, rows_to_delete):
        for row in rows_to_delete:
            query = QSqlQuery(f"""DELETE FROM TP_nir WHERE codvuz={row['codvuz']} AND rnw='{row['rnw']}'""")
            self.setQuery(query)
            self.update()

    def update_row(self, edited_row, changed_codvuz, changed_rnw):
        query = QSqlQuery(f"""
                                UPDATE Tp_nir 
                                SET codvuz={edited_row['codvuz']},
                                    rnw='{edited_row['rnw']}',
                                    f1='{edited_row['f1']}',
                                    z2='{edited_row['z2']}',
                                    f6='{edited_row['f6']}',
                                    f10='{edited_row['f10']}',
                                    f2='{edited_row['f2']}',
                                    f7='{edited_row['f7']}',
                                    f18={edited_row['f18']}
                                WHERE codvuz={changed_codvuz} AND rnw='{changed_rnw}';
                        """)
        self.setQuery(query)
        self.update()

    def add_row(self, edited_row) -> bool:
        query = QSqlQuery(f"""
                    SELECT COUNT(*) FROM Tp_nir WHERE codvuz={edited_row['codvuz']} AND rnw='{edited_row['rnw']}'
                                """)
        while query.next():
            value = query.value(0)

        if value != 0:
            return False

        else:
            for k in edited_row.keys():
                if edited_row[k] == '':
                    edited_row[k] = None
            print(edited_row)
            query = QSqlQuery()
            query.prepare(f"""
                        INSERT INTO Tp_nir(codvuz, rnw, f1, z2, f6, f10, f2, f7, f18)
                        VALUES (?,?,?,?,?,?,?,?,?)
                                """)
            for k in edited_row.keys():
                if k != 'error':
                    query.addBindValue(edited_row[k])
            query.exec()

            self.setQuery(query)
            self.update()
            return True

    def get_indexes_of_rows(self, row):
        while self.canFetchMore():
            self.fetchMore()
        selected_rows = []
        for i in range(self.rowCount()):
            if row['codvuz'] == self.data(self.index(i, 0)) and row['rnw'] == self.data(self.index(i, 1)):
                selected_rows.append(i)
        if len(selected_rows) == 1:
            return selected_rows[0]
        else:
            return 0
