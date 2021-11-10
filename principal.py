from sqlite3 import Error
from PyQt5 import QtWidgets
import sys
from qtpy import uic
import sqlite3

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.tela2 = uic.loadUi('visualizar.ui', self)
        self.tela = uic.loadUi('formulario.ui', self)
        self.tela.show()
        self.button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.salvar_dados)
        self.buttonv = self.findChild(QtWidgets.QPushButton, 'pushButton_dados')
        self.buttonv.clicked.connect(self.listar)

        self.input = self.findChild(QtWidgets.QLineEdit,'lineEdit_nome')
        self.input2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_valor')
        self.input3 = self.findChild(QtWidgets.QDateEdit, 'dateEdit')

        self.buttonvo = self.findChild(QtWidgets.QPushButton, 'pushButton_v')
        self.buttonvo.clicked.connect(self.voltar)






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




            self.input.setText("")
            self.input2.setText("")



            self.input.setText("")
            self.input2.setText("")


        except sqlite3.Error as erro:
            print("Aconteceu alguma coisa",  erro)



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





