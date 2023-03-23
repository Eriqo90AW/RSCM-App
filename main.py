from PyQt5.QtWidgets import QApplication, QMainWindow

from final_ui import *

from menu import Menu
from home import Home

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.menu = Menu(self)
        self.home = Home(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())