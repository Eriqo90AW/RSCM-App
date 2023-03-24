from PyQt5.QtWidgets import QApplication, QMainWindow

from final_ui import *

from menu import Menu
from home import Home
from setup_db import SetupDB
from login import Login
from register import Register

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_patient = {
            'id': None,
            'nama': None,
            'usia': None,
            'jenis_kelamin': None
        }

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu = Menu(self)
        self.home = Home(self)
        self.setup_db = SetupDB('db/patient.db')
        self.login = Login(self)
        self.register = Register(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())