from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database, Patient
import sys
import os
import numpy as np
from datetime import datetime

class EditButtons(QtWidgets.QWidget):
    buttonsPressed = QtCore.pyqtSignal(str, int)

    def __init__(self, *args, **kwargs):
        self.row = kwargs.pop("row")
        self.col = kwargs.pop("col")
        self.cell = kwargs.pop("cell")
        self.buttonMethod = kwargs.pop("buttonMethod", None)
        super(EditButtons, self).__init__(*args, **kwargs)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.buttons = []
        button = QtWidgets.QPushButton("Select")
        button.clicked.connect(self.buttonClicked)
        button.setObjectName("select")
        self.buttons.append(button)
        button = QtWidgets.QPushButton("Edit")
        button.clicked.connect(self.buttonClicked)
        button.setObjectName("edit")
        self.buttons.append(button)
        button = QtWidgets.QPushButton("Delete")
        button.clicked.connect(self.buttonClicked)
        button.setObjectName("delete")
        self.buttons.append(button)

        for button in self.buttons:
            self.layout.addWidget(button)
        if self.buttonMethod:
            self.buttonsPressed.connect(self.buttonMethod)

    def buttonClicked(self):
        button = self.sender()
        if button:
            id = self.cell.text()
            name = button.objectName()
            self.buttonsPressed.emit(name, int(id))

    def updateParam(self, row, col, cell):
        self.row = row
        self.col = col
        self.cell = cell

class PatientItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        if option.state and QtWidgets.QStyle.State_Selected:
            painter.fillRect(option.rect, QtGui.QBrush(QtGui.QColor(200, 200, 200, 50)))

        return super(PatientItemDelegate, self).paint(painter, option, index)                          

class PatientTable(QtWidgets.QTableWidget):
    newButton = QtCore.pyqtSignal()
    _id = []

    def __init__(self, *args, **kwargs):
        super(PatientTable, self).__init__(*args, **kwargs)
        self.database = Database()

        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["ID", "Name", "Age", "Gender", " "])
        self.setWordWrap(True)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.verticalHeader().setVisible(False)
        self.setItemDelegate(PatientItemDelegate(self))

        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setSortingEnabled(True)
        self.setStyleSheet("QTableWidget::item:selected {color: rgba(0,0,0,200); background-color: rgba(0,0,0,50); }")

        self.buttons = EditButtons(row = 0, col = 4, cell = self.item(0, 0))
        self.buttons.setObjectName("editButtons")
        self.newButton.emit()

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Usia"))
        item = self.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Jenis Kelamin"))

    def selectionChanged(self, *args, **kwargs):
        item = self.currentItem()
        if item:
            row = item.row()
            lastrow = self.buttons.row
            if row == lastrow:
                return
            
            self.setCellWidget(lastrow, 4, QtWidgets.QWidget())
            self.buttons = EditButtons(row = row, col = 4, cell = self.item(row, 0))
            self.setCellWidget(row, 4, self.buttons)
            self.newButton.emit()
            self.selectRow(row)


    def addRow(self, data):
        id = data[0]
        if id in self._id:
            return
        self._id.append(id)
        row = self.rowCount()
        self.setRowCount(row + 1)
        if isinstance(data, list) or isinstance(data, tuple):
            for col, item in enumerate(data):
                if isinstance(item, int):
                    qitem = QtWidgets.QTableWidgetItem()
                    qitem.setData(QtCore.Qt.EditRole, item)
                    self.setItem(row, col, qitem)
                    continue
                self.setItem(row, col, QtWidgets.QTableWidgetItem(item))
            self.setItem(row, 4, QtWidgets.QTableWidgetItem(""))
        elif isinstance(data, dict):
            for col, item in enumerate(data.__dict__.values()):
                if isinstance(item, int):
                    qitem = QtWidgets.QTableWidgetItem()
                    qitem.setData(QtCore.Qt.EditRole, item)
                    self.setItem(row, col, qitem)
                    continue
                self.setItem(row, col, QtWidgets.QTableWidgetItem(str(item)))
            self.setItem(row, 4, QtWidgets.QTableWidgetItem(""))

    def loadDatabase(self):
        datas = self.database.getAllPatients()
        if datas:
            for data in datas:
                self.addRow(data)

class DatabasePage(QtWidgets.QFrame):
    loginButtonClicked = QtCore.pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(DatabasePage, self).__init__(*args, **kwargs)
        self.table = PatientTable()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.table.loadDatabase()

        self.table.newButton.connect(self.newButton)

        self.parent().currentChanged.connect(self.changed)

    def changed(self):
        if self.parent().currentWidget() == self:
            self.table.loadDatabase()

    def newButton(self):
        self.table.buttons.buttonsPressed.connect(self.buttonPressed)

    def buttonPressed(self, name, id):
        if name == "delete":
            self.table.removeRow(self.table.buttons.row)
            self.table.database.deletePatient(id)
        elif name == "select":
            self.loginButtonClicked.emit(id)
        elif name == "edit":
            item = self.table.selectedItems()
            if item:
                data = [_.text() for _ in item][:-1]
                self.table.database.updatePatient(data)