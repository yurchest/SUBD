from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class AnalyzeByVuz(QSqlQueryModel):
    header_data = {'codvuz': "Код \nвуза",
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

    def update(self, last_query=f"""SELECT * FROM Tp_nir""", filter_widget=None):

        self.setQuery(f"""SELECT VUZ.codvuz,
                    COUNT(Tp_nir.codvuz) as kolvo,
                    COALESCE(sum(Tp_nir.f18), 0)as sum 
                    FROM VUZ LEFT JOIN ({last_query}) as Tp_nir
                    ON VUZ.codvuz = Tp_nir.codvuz
                    GROUP BY VUZ.codvuz
                    """)

        query = QSqlQuery(f"""
                            SELECT COUNT(*), SUM(f18) FROM ({last_query})
                            """)
        while query.next():
            amount_of_nirs = query.value(0)
            sum_fin = query.value(1)

        self.main_app.label_9.setText(str(amount_of_nirs))
        self.main_app.label_10.setText(str(sum_fin))

        if filter_widget:
            text = f"Федеральный округ: {filter_widget.w_root.comboBox_2.currentText()}\n" \
                   f"Субъект федерации: {filter_widget.w_root.comboBox_3.currentText()}\n" \
                   f"Город: {filter_widget.w_root.comboBox_4.currentText()}\n" \
                   f"ВУЗ: {filter_widget.w_root.comboBox_5.currentText()}\n" \
                   f"Первые цифры кода ГРНТИ: {filter_widget.w_root.lineEdit.text()}\n"

            self.main_app.textBrowser.setText(text)
