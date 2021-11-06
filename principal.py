from sqlite3 import Error
from PyQt5 import QtWidgets
import sys
from qtpy import uic
import sqlite3
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)




class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.tela2 = uic.loadUi('visualizar.ui', self)
        self.tela = uic.loadUi('formulario.ui', self)
        self.tela.show()
        self.button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.salvar_dados)

<<<<<<< HEAD
        self.buttonv = self.findChild(QtWidgets.QPushButton, 'pushButton_pag_visual')
        self.buttonv.clicked.connect(self.listar)

=======
>>>>>>> fa157ca (Initial commit)
        self.input = self.findChild(QtWidgets.QLineEdit,'lineEdit_nome')
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_valor')
        self.input3 = self.findChild(QtWidgets.QDateEdit, 'dateEdit')

        self.buttonvo = self.findChild(QtWidgets.QPushButton, 'pushButton_v')
        self.buttonvo.clicked.connect(self.voltar)


<<<<<<< HEAD

    # função que faz conexao com banco de dados
    # def create_connection(db_file):
    #     banco = None
    #     try:
    #         banco = sqlite3.connect(db_file)
    #         print(sqlite3.version)
    #     except Error as e:
    #         print(e)
    #     finally:
    #         if banco:
    #             banco.close()
    #
    #

    # def add_values(self):
    #     self.count = self.count + 1  # this is incrementing counter
    #     self.tableWidget_2.insertRow(self.count)
    #     self.tableWidget_2.setRowCount(self.count)
    #     # these are the items in the database
    #     item = [column1, column2, column3]
    #     # here we are adding 3 columns from the db table to the tablewidget
    #     for i in range(3):
    #         self.tableWidget_2.setItem(self.count - 1, i, QTableWidgetItem(item[i]))

=======
>>>>>>> fa157ca (Initial commit)
    def salvar_dados(self):
        nome = self.input.text()
        valor= self.input2.text()
        data = self.input3.text()
        try:
            banco = sqlite3.connect('banco_cadastro.sqlite3 ')
            cursor = banco.cursor()

            cursor.execute("Create TABLE IF NOT EXISTS dados(nome text, valor numeric, data date)")
            cursor.execute("INSERT INTO dados VALUES ('"+nome+"' ,'"+valor+"','"+data+"')")
            banco.commit()
            banco.close()

<<<<<<< HEAD


            self.input.setText("")
            self.input2.setText("")



            print("dados inseridos")
            # valor1 = (self.input.text())
            resultado = float(valor) + 8.45
            resultado2 = float(valor) + 9.32
            datamundo = str(data)
            print('Ole o olá')
            print("Agora sim o resultado : ",resultado , " e " ,resultado2, datamundo)



=======
            self.input.setText("")
            self.input2.setText("")

>>>>>>> fa157ca (Initial commit)
        except sqlite3.Error as erro:
            print("Aconteceu alguma coisa",  erro)


<<<<<<< HEAD
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
            for j in range(0,3):
                self.tela2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        banco1.close()

        # def load_initial_data(self):
        #     # where c is the cursor
        #     self.c.execute('''SELECT * FROM table ''')
        #     rows = self.c.fetchall()
        #
        #     for row in rows:
        #         inx = rows.index(row)
        #         self.tableWidget_2.insertRow(inx)
        #         # add more if there is more columns in the database.
        #         self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))
        #         self.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row[2]))
        #         self.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row[3]))

    def voltar(self):

        # valor = (self.input.text())
        # resultado = int(valor) + 8
        # print('Ole o olá')
        # print("Agora sim o resultado : ",resultado)


        self.tela2.show()




app = QtWidgets.QApplication(sys.argv)

window = Ui()
window.show()
app.exec_()

=======
#
# app = QtWidgets.QApplication(sys.argv)
#
# window = Ui()
# window.show()
# app.exec_()
#
>>>>>>> fa157ca (Initial commit)


