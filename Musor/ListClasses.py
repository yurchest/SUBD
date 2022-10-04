from __future__ import absolute_import, unicode_literals, print_function

from PyQt6.QtCore import QAbstractTableModel, QVariant, Qt, QSize
from numpy import unicode

from database_sqlalchemy import VUZ


class VuzList(QAbstractTableModel):

    def __init__(self, session, query, columns):
        super(VuzList, self).__init__()
        self.session = session

        self.session = session
        self.fields = columns
        self.query = query

        self.results = None
        self.count = None
        self.sort = None
        self.filter = None

        self.refresh()

    def headerData(self, col, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return QVariant(self.fields[col][0])

        if role == Qt.ItemDataRole.DisplayRole:
            return col + 1
        return QVariant()


    def get_all(self):
        return self.session.query(VUZ).all()

    def refresh(self):
        self.results = self.session.query(self.query).all()
        self.count = self.session.query(self.query).count()

    def rowCount(self, parent):
        return self.count or 0

    def columnCount(self, parent):
        return len(self.fields)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = self.results[index.row()]
            name = self.fields[index.column()][2]
            return unicode(getattr(row, name))

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return int(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)

        elif role == Qt.ItemDataRole.SizeHintRole:
            self.setC

        else:
            return QVariant()

    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
