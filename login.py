from PyQt5 import QtCore, QtGui

class Login:
    def __init__(self, main_window):
        self.main_window = main_window

        # Setup three buttons to login, register, adn look at database
        self.main_window.ui.button_home_login.clicked.connect(lambda: self.main_window.ui.stackedWidget.setCurrentIndex(1))
        self.main_window.ui.button_home_register.clicked.connect(lambda: self.main_window.ui.stackedWidget.setCurrentIndex(2))
        self.main_window.ui.button_home_database.clicked.connect(lambda: self.main_window.ui.stackedWidget.setCurrentIndex(3))