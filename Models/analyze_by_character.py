from PyQt6.QtSql import *
from PyQt6.QtCore import Qt


class AnalyzeByCHAR(QSqlQueryModel):
    header_data = {'f1': "Характер \nисследования",
                   "kolvo": "Кол-во \nНИР",
                   "sum": "Плановый объем \nфинансирования",
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

    def update(self, last_query="""SELECT * FROM Tp_nir""", filter_widget=None):

        self.setQuery(f"""
                            WITH my_values(f1, f2) AS (
                                VALUES ('Фундаментальное исследование', 'Ф'), ('Прикладное исследование', 'П'), ('Экспериментальная разработка', 'Р')
                            )
                            SELECT my_values.f1,
                            COUNT(Tp_nir.codvuz) as kolvo,
                            COALESCE(sum(Tp_nir.f18), 0)as sum 
                            FROM my_values LEFT JOIN ({last_query}) as Tp_nir
                            ON my_values.f2 = Tp_nir.f1
                            GROUP BY my_values.f1
                        """)

        query = QSqlQuery(f"""
                            SELECT COUNT(*), SUM(f18) FROM ({last_query})
                            """)
        while query.next():
            amount_of_nirs = query.value(0)
            sum_fin = query.value(1)

        self.main_app.label_20.setText(str(amount_of_nirs))
        self.main_app.label_22.setText(str(sum_fin))

        if filter_widget:
            text = f"Федеральный округ: {filter_widget.w_root.comboBox_2.currentText()}\n" \
                   f"Субъект федерации: {filter_widget.w_root.comboBox_3.currentText()}\n" \
                   f"Город: {filter_widget.w_root.comboBox_4.currentText()}\n" \
                   f"ВУЗ: {filter_widget.w_root.comboBox_5.currentText()}\n" \
                   f"Первые цифры кода ГРНТИ: {filter_widget.w_root.lineEdit.text()}\n"

            self.main_app.textBrowser_4.setText(text)

