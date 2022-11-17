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

    def update(self, last_query="""SELECT * FROM Tp_nir""", filter_widget=None):

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

        query = QSqlQuery(f"""
                            SELECT COUNT(*), SUM(f18) FROM ({last_query})
                            """)
        while query.next():
            amount_of_nirs = query.value(0)
            sum_fin = query.value(1)

        self.main_app.label_16.setText(str(amount_of_nirs))
        self.main_app.label_18.setText(str(sum_fin))

        if filter_widget:
            text = f"Федеральный округ: {filter_widget.w_root.comboBox_2.currentText()}\n" \
                   f"Субъект федерации: {filter_widget.w_root.comboBox_3.currentText()}\n" \
                   f"Город: {filter_widget.w_root.comboBox_4.currentText()}\n" \
                   f"ВУЗ: {filter_widget.w_root.comboBox_5.currentText()}\n" \
                   f"Первые цифры кода ГРНТИ: {filter_widget.w_root.lineEdit.text()}\n"

            self.main_app.textBrowser_3.setText(text)

