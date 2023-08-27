from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from database import Patient

class Register:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.ui.button_signup_sign.clicked.connect(self.registerPatient)

    def registerPatient(self):
        id = int(self.main_window.ui.edit_signup_id.text())
        if self.main_window.db.isPresent(Patient(id)):
            self.show_popup("ID already registered")
            return
        nama = self.main_window.ui.edit_signup_nama.text()
        usia = int(self.main_window.ui.edit_signup_umur.text())
        jenis_kelamin = self.main_window.ui.combobox_signup_gender.currentText()
        self.main_window.db.addPatient(Patient(id, nama, usia, jenis_kelamin))
        self.main_window.ui.stackedWidget.setCurrentIndex(1)

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