from PyQt6.QtWidgets import QAbstractItemView, QTableView

import Models


def update_table_views(nir_table: QTableView, fin_vuz_table: QTableView, vuz_table: QTableView ):
    # nir_table
    nir_table.setSortingEnabled(True)
    change_columns_nir(nir_table)
    resize_columns_nir(nir_table)
    nir_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    # vuz_table
    vuz_table.setSortingEnabled(True)
    change_columns_vuz(vuz_table)
    resize_columns_vuz(vuz_table)
    vuz_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    # fin_vuz_table
    fin_vuz_table.setSortingEnabled(True)
    change_columns_fin_vuz(fin_vuz_table)
    resize_columns_fin_vuz(fin_vuz_table)


def change_columns_nir(nir_table: QTableView):
    nir_table.horizontalHeader().moveSection(3, 0)
    nir_table.horizontalHeader().moveSection(4, 1)
    nir_table.horizontalHeader().moveSection(8, 2)
    nir_table.horizontalHeader().moveSection(6, 3)
    nir_table.horizontalHeader().moveSection(7, 4)
    nir_table.horizontalHeader().moveSection(8, 5)
    nir_table.horizontalHeader().setFixedHeight(60)


def change_columns_vuz(vuz_table: QTableView):
    vuz_table.horizontalHeader().moveSection(3, 0)
    vuz_table.horizontalHeader().moveSection(5, 1)
    vuz_table.horizontalHeader().moveSection(6, 2)
    vuz_table.horizontalHeader().moveSection(8, 3)
    vuz_table.horizontalHeader().moveSection(5, 4)
    vuz_table.horizontalHeader().moveSection(6, 5)
    vuz_table.horizontalHeader().moveSection(7, 6)


def change_columns_fin_vuz(fin_vuz_table: QTableView):
    pass


def resize_columns_fin_vuz(fin_vuz_table: QTableView):
    for i in range(9):
        fin_vuz_table.resizeColumnToContents(i)
        fin_vuz_table.setColumnWidth(i, fin_vuz_table.columnWidth(i) + 20)


def resize_columns_vuz(vuz_table: QTableView):
    for i in range(9):
        vuz_table.resizeColumnToContents(i)
        vuz_table.setColumnWidth(i, vuz_table.columnWidth(i) - 10)
    vuz_table.setColumnWidth(1, 200)
    vuz_table.setColumnWidth(2, 300)


def resize_columns_nir(nir_table):
    for i in range(9):
        nir_table.resizeColumnToContents(i)
        nir_table.setColumnWidth(i, nir_table.columnWidth(i) - 10)
    nir_table.setColumnWidth(6, 200)


def update_models(nir_model: Models.NirModel, vuz_model: Models.VuzModel, fin_vuz_model: Models.FinanceVuzModel):
    nir_model.update()
    vuz_model.update()
    fin_vuz_model.update()
