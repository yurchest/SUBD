from PyQt6.QtSql import *


def connect_db(db_name):
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_name)
    if not db.open():
        print('ERROR CONNECTION TO DATABASE')
        return False
    return db
