from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Login:
    def __init__(self, main_window):
        self.main_window = main_window
        self.id = None
        self.main_window.ui.button_login_login.clicked.connect(self.readInput)
        
    def readInput(self):
        id = self.main_window.ui.edit_login_id_2.text()
        self.loginById(id)

    def loginById(self, id):
        self.id = id
        try:
            patient = self.main_window.setup_db.login(id)
            self.savePatient(patient)
            self.main_window.graph.initPatient()
            self.main_window.ui.stackedWidget.setCurrentIndex(4)
        except:
            self.show_popup()
    
    def savePatient(self, patient):
        self.main_window.current_patient['id'] = patient['id']
        self.main_window.current_patient['nama'] = patient['nama']
        self.main_window.current_patient['usia'] = patient['usia']
        self.main_window.current_patient['jenis_kelamin'] = patient['jenis_kelamin']

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