# Form implementation generated from reading ui file 'UI/uis/form.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1566, 964)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1661, 941))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.tableView = QtWidgets.QTableView(self.page_1)
        self.tableView.setGeometry(QtCore.QRect(10, 140, 1551, 681))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 840, 641, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(570, 90, 251, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 880, 121, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_23 = QtWidgets.QLabel(self.page_1)
        self.label_23.setGeometry(QtCore.QRect(290, 10, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableView_2 = QtWidgets.QTableView(self.page_2)
        self.tableView_2.setGeometry(QtCore.QRect(10, 110, 1551, 771))
        self.tableView_2.setObjectName("tableView_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableView_3 = QtWidgets.QTableView(self.page_3)
        self.tableView_3.setGeometry(QtCore.QRect(10, 110, 1551, 791))
        self.tableView_3.setObjectName("tableView_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser.setGeometry(QtCore.QRect(300, 40, 311, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.tableView_4 = QtWidgets.QTableView(self.page_4)
        self.tableView_4.setGeometry(QtCore.QRect(20, 260, 591, 511))
        self.tableView_4.setObjectName("tableView_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(20, 820, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(20, 870, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(230, 820, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(420, 870, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_24 = QtWidgets.QLabel(self.page_4)
        self.label_24.setGeometry(QtCore.QRect(660, 210, 731, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.tableView_11 = QtWidgets.QTableView(self.page_4)
        self.tableView_11.setGeometry(QtCore.QRect(660, 260, 871, 511))
        self.tableView_11.setObjectName("tableView_11")
        self.line = QtWidgets.QFrame(self.page_4)
        self.line.setGeometry(QtCore.QRect(620, 20, 20, 791))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_25 = QtWidgets.QLabel(self.page_4)
        self.label_25.setGeometry(QtCore.QRect(660, 0, 681, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.tableView_12 = QtWidgets.QTableView(self.page_4)
        self.tableView_12.setGeometry(QtCore.QRect(660, 40, 661, 141))
        self.tableView_12.setObjectName("tableView_12")
        self.line_2 = QtWidgets.QFrame(self.page_4)
        self.line_2.setGeometry(QtCore.QRect(610, 200, 941, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.page_4)
        self.line_5.setGeometry(QtCore.QRect(0, 200, 631, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.page_4)
        self.line_6.setGeometry(QtCore.QRect(10, 810, 1531, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 780, 151, 26))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_14.setGeometry(QtCore.QRect(1350, 150, 151, 26))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_15.setGeometry(QtCore.QRect(1380, 780, 151, 26))
        self.pushButton_15.setObjectName("pushButton_15")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tableView_9 = QtWidgets.QTableView(self.page_5)
        self.tableView_9.setGeometry(QtCore.QRect(20, 190, 851, 521))
        self.tableView_9.setObjectName("tableView_9")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(300, 70, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_12 = QtWidgets.QLabel(self.page_5)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 731, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(20, 720, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.page_5)
        self.label_16.setGeometry(QtCore.QRect(230, 720, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(20, 770, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(420, 770, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_5)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_14 = QtWidgets.QLabel(self.page_11)
        self.label_14.setGeometry(QtCore.QRect(20, 90, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_11)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 681, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tableView_10 = QtWidgets.QTableView(self.page_11)
        self.tableView_10.setGeometry(QtCore.QRect(20, 230, 661, 141))
        self.tableView_10.setObjectName("tableView_10")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_11)
        self.textBrowser_4.setGeometry(QtCore.QRect(300, 100, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_19 = QtWidgets.QLabel(self.page_11)
        self.label_19.setGeometry(QtCore.QRect(20, 400, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_11)
        self.label_20.setGeometry(QtCore.QRect(230, 400, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_11)
        self.label_21.setGeometry(QtCore.QRect(20, 450, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_11)
        self.label_22.setGeometry(QtCore.QRect(420, 450, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.page_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1566, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_1 = QtGui.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action_1)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.action_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Редактирование"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_4.setText(_translate("MainWindow", "Фильтровать"))
        self.pushButton_5.setText(_translate("MainWindow", "Сортировка"))
        self.label_2.setText(_translate("MainWindow", "Данные по НИР"))
        self.pushButton_6.setText(_translate("MainWindow", "Сбросить фильтры"))
        self.label_23.setText(_translate("MainWindow", "Управление научными исследованиями по тематическому плану"))
        self.label_3.setText(_translate("MainWindow", "Данные по Финансированию Вузов"))
        self.label_4.setText(_translate("MainWindow", "Данные по Вузам"))
        self.label_5.setText(_translate("MainWindow", "Анализ распределения НИР по Вузам"))
        self.label_6.setText(_translate("MainWindow", "Применяемые фильтры:"))
        self.label_7.setText(_translate("MainWindow", "Общее кол-во НИР :"))
        self.label_8.setText(_translate("MainWindow", "Суммарный объем финансирования :"))
        self.label_24.setText(_translate("MainWindow", "Анализ распределения НИР по рубрикам ГРНТИ"))
        self.label_25.setText(_translate("MainWindow", "Анализ распределения НИР по характеру НИР"))
        self.pushButton_13.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton_14.setText(_translate("MainWindow", "Сохранить в файл"))
        self.pushButton_15.setText(_translate("MainWindow", "Сохранить в файл"))
        self.label_12.setText(_translate("MainWindow", "Анализ распределения НИР по рубрикам ГРНТИ"))
        self.label_13.setText(_translate("MainWindow", "Применяемые фильтры:"))
        self.label_11.setText(_translate("MainWindow", "Общее кол-во НИР :"))
        self.label_17.setText(_translate("MainWindow", "Суммарный объем финансирования :"))
        self.label_14.setText(_translate("MainWindow", "Применяемые фильтры:"))
        self.label_15.setText(_translate("MainWindow", "Анализ распределения НИР по характеру НИР"))
        self.label_19.setText(_translate("MainWindow", "Общее кол-во НИР :"))
        self.label_21.setText(_translate("MainWindow", "Суммарный объем финансирования :"))
        self.menu.setTitle(_translate("MainWindow", "Данные"))
        self.menu_2.setTitle(_translate("MainWindow", "Анализ"))
        self.action_1.setText(_translate("MainWindow", "НИР"))
        self.action_2.setText(_translate("MainWindow", "Финансирование вузов"))
        self.action_3.setText(_translate("MainWindow", "Вузы"))
        self.action_4.setText(_translate("MainWindow", "По Вузам"))
        self.action_5.setText(_translate("MainWindow", "По рубрикам ГРНТИ"))
        self.action_6.setText(_translate("MainWindow", "По характеру НИР"))
        self.action_7.setText(_translate("MainWindow", "Анализ распределения НИР"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
