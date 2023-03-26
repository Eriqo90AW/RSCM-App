from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class Database:
    def __init__(self, main_window):
        self.main_window = main_window
        self.updateTable()

    def addRow(self, rowNumber, id, nama, usia, jenis_kelamin):
        if id > 20:
            self.main_window.ui.table_database_data.insertRow(1)
        self.main_window.ui.table_database_data.setItem (rowNumber, 0, QTableWidgetItem (str(id)))
        self.main_window.ui.table_database_data.setItem (rowNumber, 1, QTableWidgetItem (str(nama)))
        self.main_window.ui.table_database_data.setItem (rowNumber, 2, QTableWidgetItem (str(usia)))
        self.main_window.ui.table_database_data.setItem (rowNumber, 3, QTableWidgetItem (str(jenis_kelamin)))
    
    def updateTable(self):
        data = self.main_window.setup_db.getAllPatient()
        i = 0
        for row in data:
            self.addRow(i, row[0], row[1], row[2], row[3])
            i += 1