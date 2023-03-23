from PyQt5 import QtCore, QtGui, QtWidgets

class ui_database(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database_page = QtWidgets.QWidget(self)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.database_page)
        self.main_layout.setContentsMargins(0,0,0,0)

        self.database_page.setStyleSheet("#frame_database_menu\n"
"{\n"
"    border-radius: 10px;\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 150,200, 235), stop:1 rgba(235, 255, 255, 155));*/\n"
"}\n"
"\n"
"QLineEdit"
"{\n"
"   background-color: white;\n"
"   color: 0x0;\n"
"}\n"
"#frame_button_back QPushButton{\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#frame_button_back QPushButton:hover\n"
"{\n"
"border-radius: 10px;\n"
"background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"#frame_button_delete QPushButton{\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#frame_button_delete QPushButton:hover\n"
"{\n"
"border-radius: 10px;\n"
"background-color: rgb(120, 157, 186);\n"
"}\n"
""
"font-color = #000000\n"
"")
        self.database_page.setObjectName("database_page")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.database_page)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_table = QtWidgets.QFrame(self.database_page)
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_table)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_database_data = QtWidgets.QTableWidget(self.frame_table)
        self.table_database_data.setFrameShape(QtWidgets.QFrame.VLine)
        self.table_database_data.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_database_data.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table_database_data.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_database_data.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_database_data.setAutoScroll(True)
        self.table_database_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_database_data.setAlternatingRowColors(True)
        self.table_database_data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_database_data.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_database_data.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_database_data.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_database_data.setRowCount(4)
        self.table_database_data.setObjectName("table_database_data")
        self.table_database_data.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_database_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_database_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_database_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_database_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_database_data.setHorizontalHeaderItem(4, item)
        self.table_database_data.horizontalHeader().setCascadingSectionResizes(False)
        self.table_database_data.horizontalHeader().setMinimumSectionSize(39)
        self.table_database_data.horizontalHeader().setSortIndicatorShown(True)
        self.table_database_data.horizontalHeader().setStretchLastSection(True)
        self.table_database_data.verticalHeader().setVisible(False)
        self.table_database_data.verticalHeader().setCascadingSectionResizes(False)
        self.table_database_data.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.table_database_data)
        self.frame_database_menu = QtWidgets.QFrame(self.frame_table)
        self.frame_database_menu.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_database_menu.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_database_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_database_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_database_menu.setObjectName("frame_database_menu")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_database_menu)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(11)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_database_left = QtWidgets.QFrame(self.frame_database_menu)
        self.frame_database_left.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_database_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_database_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_database_left.setObjectName("frame_database_left")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_database_left)
        self.verticalLayout_6.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_database_id = QtWidgets.QFrame(self.frame_database_left)
        self.frame_database_id.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_database_id.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_database_id.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_database_id.setObjectName("frame_database_id")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_database_id)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_database_id = QtWidgets.QLabel(self.frame_database_id)
        self.label_database_id.setObjectName("label_database_id")
        self.horizontalLayout_16.addWidget(self.label_database_id)
        self.edit_database_id = QtWidgets.QLineEdit(self.frame_database_id)
        self.edit_database_id.setMaximumSize(QtCore.QSize(200, 16777215))
        self.edit_database_id.setObjectName("edit_database_id")
        self.horizontalLayout_16.addWidget(self.edit_database_id)
        self.verticalLayout_6.addWidget(self.frame_database_id)
        self.frame_button_back = QtWidgets.QFrame(self.frame_database_left)
        self.frame_button_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_back.setObjectName("frame_button_back")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_button_back)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.button_database_back = QtWidgets.QPushButton(self.frame_button_back)
        self.button_database_back.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_database_back.setObjectName("button_database_back")
        self.horizontalLayout_17.addWidget(self.button_database_back)
        self.verticalLayout_6.addWidget(self.frame_button_back)
        self.horizontalLayout_15.addWidget(self.frame_database_left)
        self.frame_database_right = QtWidgets.QFrame(self.frame_database_menu)
        self.frame_database_right.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_database_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_database_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_database_right.setObjectName("frame_database_right")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_database_right)
        self.verticalLayout_8.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_database_nama = QtWidgets.QFrame(self.frame_database_right)
        self.frame_database_nama.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_database_nama.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_database_nama.setObjectName("frame_database_nama")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_database_nama)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_database_nama = QtWidgets.QLabel(self.frame_database_nama)
        self.label_database_nama.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_database_nama.setObjectName("label_database_nama")
        self.horizontalLayout_18.addWidget(self.label_database_nama)
        self.edit_database_nama = QtWidgets.QLineEdit(self.frame_database_nama)
        self.edit_database_nama.setMaximumSize(QtCore.QSize(200, 16777215))
        self.edit_database_nama.setObjectName("edit_database_nama")
        self.horizontalLayout_18.addWidget(self.edit_database_nama)
        self.verticalLayout_8.addWidget(self.frame_database_nama)
        self.frame_button_delete = QtWidgets.QFrame(self.frame_database_right)
        self.frame_button_delete.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_delete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_delete.setObjectName("frame_button_delete")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_button_delete)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.button_database_delete = QtWidgets.QPushButton(self.frame_button_delete)
        self.button_database_delete.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_database_delete.setObjectName("button_database_delete")
        self.horizontalLayout_19.addWidget(self.button_database_delete)
        self.verticalLayout_8.addWidget(self.frame_button_delete)
        self.horizontalLayout_15.addWidget(self.frame_database_right)
        self.verticalLayout_3.addWidget(self.frame_database_menu, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_14.addWidget(self.frame_table)

    def retranslateUi(self, MainWindow, _translate):
        self.table_database_data.setSortingEnabled(True)
        item = self.table_database_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_database_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.table_database_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Usia"))
        item = self.table_database_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Jenis Kelamin"))
        self.label_database_id.setText(_translate("MainWindow", "ID"))
        self.button_database_back.setText(_translate("MainWindow", "Back"))
        self.label_database_nama.setText(_translate("MainWindow", "Nama"))
        self.button_database_delete.setText(_translate("MainWindow", "Delete"))
