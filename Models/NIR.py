from typing import Dict

from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


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

    sortOrder = ['ASC'] * 9

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setTable("Tp_nir")
        # self.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.change_column_name()
        self.select()
        self.whereQuery = ''
        self.orderByQuery = ''


    def change_column_name(self):
        for i in range(self.columnCount()):
            self.setHeaderData(i, Qt.Orientation.Horizontal, self.header_data[self.record().fieldName(i)])


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

    def delete_rows(self, rows_to_delete):
        for row in rows_to_delete:
            self.removeRow(row.row())
        self.update_model()
        # for row in rows_to_delete:
        #     QSqlQuery(f"""DELETE FROM TP_nir WHERE codvuz={row['codvuz']} AND rnw='{row['rnw']}'""")
        #     print(self.query().lastQuery())
        #     self.select()

    def update_row(self, edited_row, changed_codvuz, changed_rnw):
        QSqlQuery(f"""
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
        self.update_model()

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
            query = QSqlQuery()
            query.prepare(f"""
                        INSERT INTO Tp_nir(codvuz, rnw, f1, z2, f6, f10, f2, f7, f18)
                        VALUES (?,?,?,?,?,?,?,?,?)
                                """)
            for k in edited_row.keys():
                if k != 'error':
                    query.addBindValue(edited_row[k])
            query.exec()

            self.update_model()
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

    def sort_by_codvuz_rnw(self):
        self.orderByQuery = f""" ORDER BY codvuz, rnw"""
        self.update_model()

    def update_model(self):
        self.select()
        print(self.selectStatement() + self.whereQuery + self.orderByQuery)
        self.setQuery(QSqlQuery(self.selectStatement() + self.whereQuery + self.orderByQuery))

    def reset_filters(self):
        self.whereQuery = ''
        self.update_model()


