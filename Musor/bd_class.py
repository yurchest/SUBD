import sqlite3


class Database():
    instance = None
    __DB_LOCATION = "Databases/my_bd.db"

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(Database)
            return cls.instance
        return cls.instance

    def __init__(self, db_location=None):
        try:
            if db_location is not None:
                self.connection = sqlite3.connect(db_location)
            else:
                self.connection = sqlite3.connect(self.__DB_LOCATION)
            self.cur = self.connection.cursor()
            print("SUCCESSFULLY CONNECTED TO DATABASE")
        except sqlite3.Error as error:
            print('ERROR CONNECTION TO DATABASE\nError: %s' % (str(error)))

    def execute(self, sql):
        try:
            self.cur.execute(sql)
        except Exception as error:
            print('Query Failed: %s\nError: %s' % (sql, str(error)))

    def executemany(self, sql, data):
        try:
            self.cur.executemany(sql, data)
        except Exception as error:
            print('Query Failed: %s\nError: %s' % (sql, str(error)))

    def fetchall(self, sql):
        rows = []
        self.execute(sql)
        rows = self.cur.fetchall()
        return rows

    def commit(self):
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        if self.connection is not None:
            self.connection.close()

    def __del__(self):
        if self.connection is not None:
            self.cur.close()
            self.connection.close()
