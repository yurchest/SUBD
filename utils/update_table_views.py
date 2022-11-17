from PyQt6.QtWidgets import QAbstractItemView, QTableView

import Models


def update_table_views(nir_table: QTableView, fin_vuz_table: QTableView, vuz_table: QTableView, analyze_vuz,
                       analyze_grnti, analyze_char):
    nir_table.verticalHeader().setVisible(False)

    # nir_table
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

    # analyze_vuz.verticalHeader().setVisible(False)
    # analyze_grnti.verticalHeader().setVisible(False)
    analyze_char.verticalHeader().setVisible(False)
    resize_columns_analyze_vuz(analyze_vuz)
    resize_columns_analyze_grnti(analyze_grnti)
    resize_columns_analyze_char(analyze_char)



def resize_columns_analyze_vuz(analyze_vuz: QTableView):
    for i in range(4):
        analyze_vuz.resizeColumnToContents(i)
        analyze_vuz.setColumnWidth(i, analyze_vuz.columnWidth(i) + 50)


def resize_columns_analyze_grnti(analyze_grnti: QTableView):
    for i in range(4):
        analyze_grnti.resizeColumnToContents(i)
        analyze_grnti.setColumnWidth(i, analyze_grnti.columnWidth(i) + 50)
    analyze_grnti.setColumnWidth(1, 400)


def resize_columns_analyze_char(analyze_char: QTableView):
    for i in range(4):
        analyze_char.resizeColumnToContents(i)
        analyze_char.setColumnWidth(i, analyze_char.columnWidth(i) + 50)


def change_columns_nir(nir_table: QTableView):
    nir_table.horizontalHeader().moveSection(3, 0)
    nir_table.horizontalHeader().moveSection(2, 1)
    nir_table.horizontalHeader().moveSection(4, 2)
    nir_table.horizontalHeader().moveSection(5, 3)
    nir_table.horizontalHeader().moveSection(8, 4)
    # nir_table.horizontalHeader().moveSection(8, 5)
    # nir_table.horizontalHeader().setFixedHeight(60)
    pass


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
        # vuz_table.setColumnWidth(i, vuz_table.columnWidth(i) - 10)
    vuz_table.setColumnWidth(1, 200)
    vuz_table.setColumnWidth(2, 300)


def resize_columns_nir(nir_table):
    for i in range(9):
        nir_table.resizeColumnToContents(i)
        nir_table.setColumnWidth(i, nir_table.columnWidth(i) - 5)
    nir_table.setColumnWidth(6, 200)
