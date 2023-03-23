from PyQt5 import QtCore, QtGui, QtWidgets

class ui_signup(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        # self.setMinimumSize(400,400)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        # sizePolicy.setHorizontalStretch(1)
        # sizePolicy.setVerticalStretch(1)
        # self.setSizePolicy(sizePolicy)

        self.register_page = QtWidgets.QWidget(self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.register_page)
        self.layout.setContentsMargins(0,0,0,0)


        self.register_page.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.register_page.setStyleSheet("#label_create_main\n"
"{\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"#frame_register_main\n"
"{\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 150,200, 235), stop:1 rgba(235, 255, 255, 155));\n"
"}\n"
"\n"
"#edit_signup_id\n"
"{\n"
"    border:none;\n"
"    border-bottom:2px solid rgba(255, 255, 255, 155);\n"
"    color:rgba(50,50,50,250);\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"#edit_signup_nama\n"
"{\n"
"    border:none;\n"
"    border-bottom:2px solid rgba(255, 255, 255, 155);\n"
"    color:rgba(50,50,50,250);\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"#edit_signup_umur\n"
"{\n"
"    border:none;\n"
"    border-bottom:2px solid rgba(255, 255, 255, 155);\n"
"    color:rgba(50,50,50,250);\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"#frame_signup_button QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"\n"
"\n"
"#frame_signup_button QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"#frame_signup_combobox QComboBox{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#frame_signup_combobox QComboBox QAbstractItemView{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 150,200, 235), stop:1 rgba(235, 255, 255, 155));\n"
"}")
        self.register_page.setObjectName("register_page")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.register_page)
        self.horizontalLayout_11.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_register_main = QtWidgets.QFrame(self.register_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_register_main.sizePolicy().hasHeightForWidth())
        self.frame_register_main.setSizePolicy(sizePolicy)
        self.frame_register_main.setMaximumSize(QtCore.QSize(400, 500))
        self.frame_register_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_register_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_register_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_register_main.setObjectName("frame_register_main")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_register_main)
        self.verticalLayout_7.setContentsMargins(25, -1, 25, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_create = QtWidgets.QFrame(self.frame_register_main)
        self.frame_create.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_create.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_create.setObjectName("frame_create")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_create)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_create_main = QtWidgets.QLabel(self.frame_create)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(-1)
        self.label_create_main.setFont(font)
        self.label_create_main.setObjectName("label_create_main")
        self.horizontalLayout_5.addWidget(self.label_create_main)
        self.verticalLayout_7.addWidget(self.frame_create, 0, QtCore.Qt.AlignHCenter)
        self.frame_signup_id = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_id.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_id.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_id.setObjectName("frame_signup_id")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_signup_id)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.edit_signup_id = QtWidgets.QLineEdit(self.frame_signup_id)
        self.edit_signup_id.setObjectName("edit_signup_id")
        self.horizontalLayout_10.addWidget(self.edit_signup_id)
        self.verticalLayout_7.addWidget(self.frame_signup_id)
        self.frame_signup_nama = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_nama.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_nama.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_nama.setObjectName("frame_signup_nama")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_signup_nama)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.edit_signup_nama = QtWidgets.QLineEdit(self.frame_signup_nama)
        self.edit_signup_nama.setObjectName("edit_signup_nama")
        self.horizontalLayout_9.addWidget(self.edit_signup_nama)
        self.verticalLayout_7.addWidget(self.frame_signup_nama)
        self.frame_signup_umur = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_umur.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_umur.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_umur.setObjectName("frame_signup_umur")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_signup_umur)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.edit_signup_umur = QtWidgets.QLineEdit(self.frame_signup_umur)
        self.edit_signup_umur.setObjectName("edit_signup_umur")
        self.horizontalLayout_8.addWidget(self.edit_signup_umur)
        self.verticalLayout_7.addWidget(self.frame_signup_umur)
        self.frame_signup_label = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_label.setObjectName("frame_signup_label")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_signup_label)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_gender = QtWidgets.QLabel(self.frame_signup_label)
        self.label_gender.setObjectName("label_gender")
        self.horizontalLayout_6.addWidget(self.label_gender)
        self.verticalLayout_7.addWidget(self.frame_signup_label)
        self.frame_signup_combobox = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_combobox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_combobox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_combobox.setObjectName("frame_signup_combobox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_signup_combobox)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.combobox_signup_gender = QtWidgets.QComboBox(self.frame_signup_combobox)
        self.combobox_signup_gender.setObjectName("combobox_signup_gender")
        self.combobox_signup_gender.addItem("")
        self.combobox_signup_gender.addItem("")
        self.horizontalLayout_7.addWidget(self.combobox_signup_gender)
        self.verticalLayout_7.addWidget(self.frame_signup_combobox)
        self.frame_signup_button = QtWidgets.QFrame(self.frame_register_main)
        self.frame_signup_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup_button.setObjectName("frame_signup_button")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_signup_button)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.button_signup_sign = QtWidgets.QPushButton(self.frame_signup_button)
        self.button_signup_sign.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_signup_sign.setObjectName("button_signup_sign")
        self.horizontalLayout_13.addWidget(self.button_signup_sign)
        self.verticalLayout_7.addWidget(self.frame_signup_button)
        self.horizontalLayout_11.addWidget(self.frame_register_main)

    def retranslateUi(self, MainWindow, _translate):
        self.edit_signup_id.setPlaceholderText(_translate("MainWindow", "ID"))
        self.edit_signup_nama.setPlaceholderText(_translate("MainWindow", "Nama"))
        self.edit_signup_umur.setPlaceholderText(_translate("MainWindow", "Umur"))
        self.label_gender.setText(_translate("MainWindow", "Jenis Kelamin:"))
        self.combobox_signup_gender.setItemText(0, _translate("MainWindow", "Laki-laki"))
        self.combobox_signup_gender.setItemText(1, _translate("MainWindow", "Perempuan"))
        self.button_signup_sign.setText(_translate("MainWindow", "Register"))
