from PyQt5.QtWidgets import QApplication, QMainWindow

from final_ui import *

from menu import Menu
from home import Home
from login import Login
from register import Register
from ui_database import DatabasePage
from graph_logic import GraphLogic
from database import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_patient = {
            'id': None,
            'nama': None,
            'usia': None,
            'jenis_kelamin': None
        }
        self.db = Database()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu = Menu(self)
        self.home = Home(self)
        self.login = Login(self)
        self.register = Register(self)
        self.graph = GraphLogic(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())