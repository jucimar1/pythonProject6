import sys
from principal import Ui
from secundario import Ui_Visualizar
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = Tela()
    sys.exit(app.exec_())
