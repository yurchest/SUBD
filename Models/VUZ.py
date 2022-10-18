from PyQt6.QtSql import *
from PyQt6.QtCore import Qt

class VuzModel(QSqlTableModel):

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setTable("VUZ")
        self.select()