from sqlite3 import Error
from PyQt5 import QtWidgets
import sys
from qtpy import uic
import sqlite3
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)


class Ui_Visualizar(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Visualizar, self).__init__()
        self.tela2 = uic.loadUi('visualizar.ui', self)

        self.tela2.show()
        self.buttonv = self.findChild(QtWidgets.QPushButton, 'pushButton_pag_visual')
        self.buttonv.clicked.connect(self.listar)

    def listar(self):
        self.tela2 = uic.loadUi('visualizar.ui', self)
        self.tela2.show()
        banco1 = sqlite3.connect('banco_cadastro.sqlite3 ')
        cursor = banco1.cursor()

        cursor.execute("SELECT * FROM dados ;")
        dados_lidos = cursor.fetchall()
        self.tela2.tableWidget.setRowCount(len(dados_lidos))
        self.tela2.tableWidget.setColumnCount(3)
        print("foi contado quantidade")

        for i in range(0, len(dados_lidos)):
            for j in range(0, 3):
                self.tela2.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
                banco1.close()


