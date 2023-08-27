from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.id = None
        self.main_window.ui.button_login_login.clicked.connect(self.loginById)
        self.main_window.ui.button_login_sign.clicked.connect(lambda : self.main_window.ui.stackedWidget.setCurrentIndex(2))
        self.main_window.ui.database_page.loginButtonClicked.connect(self.loginById)

    def loginById(self, id = None):
        if id:
            self.id = id
        else:
            self.id = int(self.main_window.ui.edit_login_id_2.text())

        patient = self.main_window.db.getPatient(self.id)
        if patient:
            self.savePatient(patient)
            self.main_window.ui.stackedWidget.setCurrentIndex(4)
        else:
            self.show_popup()
    
    def savePatient(self, patient):
        if isinstance(patient, dict):
            self.main_window.current_patient['id'] = patient['id']
            self.main_window.current_patient['nama'] = patient['nama']
            self.main_window.current_patient['usia'] = patient['usia']
            self.main_window.current_patient['jenis_kelamin'] = patient['jenis_kelamin']
        elif isinstance(patient, list) or isinstance(patient, tuple):
            self.main_window.current_patient['id'] = patient[0]
            self.main_window.current_patient['nama'] = patient[1]
            self.main_window.current_patient['usia'] = patient[2]
            self.main_window.current_patient['jenis_kelamin'] = patient[3]

    def show_popup(self):
        # Create a QMessageBox widget
        message_box = QMessageBox()

        # Set the text and title of the message box
        message_box.setText(f"No patient found with ID: {self.id}")
        message_box.setWindowTitle("Error")

        # Set the icon and buttons of the message box
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the message box and wait for a response
        message_box.exec_()