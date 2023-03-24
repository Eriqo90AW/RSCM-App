from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Register:
    def __init__(self, main_window):
        self.main_window = main_window
        self.currentId = self.main_window.setup_db.getLastId() + 1
        print(self.currentId)
        self.main_window.ui.edit_signup_id.setText(f"ID: {self.currentId}")
        self.jenis_kelamin = None
        self.usia = None
        self.jenis_kelamin = None
        self.main_window.ui.button_signup_sign.clicked.connect(self.readInput)
        
    def readInput(self):
        nama = self.main_window.ui.edit_signup_nama.text()
        usia = self.main_window.ui.edit_signup_umur.text()
        jenis_kelamin = self.main_window.ui.combobox_signup_gender.currentText()

        self.registerPatient(nama, usia, jenis_kelamin)

    def registerPatient(self, nama, usia, jenis_kelamin):
        self.nama = nama
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        patient = self.main_window.setup_db.register(nama, usia, jenis_kelamin)
        if patient:
            self.show_popup(f"Successfully registered patient with ID: {self.currentId}")
            self.main_window.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.show_popup("Failed to register patient")

    def show_popup(self, message):
        # Create a QMessageBox widget
        message_box = QMessageBox()

        # Set the text and title of the message box
        message_box.setText(message)
        message_box.setWindowTitle("Register Patient")

        # Set the icon and buttons of the message box
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the message box and wait for a response
        message_box.exec_()