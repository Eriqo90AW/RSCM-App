from PyQt5 import QtCore, QtGui, QtWidgets
class ui_graph(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
     
        self.graph_page = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.graph_page)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.graph_page.setStyleSheet("#frame_graph_gbframe QComboBox\n"
"{\n"
"text-align: center;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#frame_graph_gbframe QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"#winmenu_graph\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.48, stop:0 rgba(0, 100,180, 200), stop:1 rgba(0, 100, 115, 123));\n"
"}\n"
"#frame_graph_head, #frame_graph_tframe\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 150,200, 235), stop:1 rgba(235, 255, 255, 155));\n"
"border-radius: 5px;\n"
"font-size: 14px;\n"
"}\n"
"#frame_graph_left, #widget_main_graph, #widget_average_graph, #widget_sensors_graph, #frame_graph_inleft, #frame_graph_inright\n"
"{\n"
"background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"#label_graph_tlabel\n"
"{\n"
"    font-family: \'Segoe UI\';\n"
"    font-size: 24px;\n"
"}\n"
"#frame_graph_inleft QLabel\n"
"{\n"
"font-size: 14px;\n"
"}\n"
"#frame_graph_inright QLabel\n"
"{\n"
"font-size: 14px;\n"
"}\n"
"#frame_graph_gbframe QPushButton\n"
"{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#frame_graph_gbframe QPushButton:hover\n"
"{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(120, 157, 186);\n"
"}\n"
"#frame_graph_sframe QPushButton\n"
"{\n"
"    padding: 12px;\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 150,200, 235), stop:1 rgba(235, 255, 255, 155));\n"
"}\n"
"#frame_graph_sframe QPushButton:hover\n"
"{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"#frame_graph_head QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"#frame_graph_head QPushButton:hover\n"
"{\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"#frame_graph_menu QPushButton:hover\n"
"{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"#frame_graph_util QPushButton\n"
"{\n"
"font-size: 13px;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"#frame_graph_util QPushButton:hover\n"
"{\n"
"    border-radius: 5px;\n"
"    background-color: rgba(61, 80, 95, 100)\n"
"}")
        self.graph_page.setObjectName("graph_page")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.graph_page)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame = QtWidgets.QFrame(self.graph_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.frame_graph_left = QtWidgets.QWidget(self.frame)
        self.frame_graph_left.setObjectName("frame_graph_left")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_graph_left)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_graph_tframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_tframe.setMinimumSize(QtCore.QSize(200, 80))
        self.frame_graph_tframe.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_graph_tframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_tframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_tframe.setObjectName("frame_graph_tframe")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_graph_tframe)
        self.horizontalLayout_21.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_graph_ticon = QtWidgets.QLabel(self.frame_graph_tframe)
        self.label_graph_ticon.setMinimumSize(QtCore.QSize(40, 40))
        self.label_graph_ticon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_graph_ticon.setText("")
        self.label_graph_ticon.setPixmap(QtGui.QPixmap(":/icons/icons/bar-chart-icon.svg"))
        self.label_graph_ticon.setScaledContents(True)
        self.label_graph_ticon.setObjectName("label_graph_ticon")
        self.horizontalLayout_21.addWidget(self.label_graph_ticon, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_graph_tlabel = QtWidgets.QLabel(self.frame_graph_tframe)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_graph_tlabel.setFont(font)
        self.label_graph_tlabel.setObjectName("label_graph_tlabel")
        self.horizontalLayout_21.addWidget(self.label_graph_tlabel, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_9.addWidget(self.frame_graph_tframe)
        self.frame_graph_gbframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_gbframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_gbframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_gbframe.setObjectName("frame_graph_gbframe")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_graph_gbframe)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.button_graph_main = QtWidgets.QPushButton(self.frame_graph_gbframe)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.button_graph_main.setFont(font)
        icon = QtGui.QIcon.fromTheme("SP_ArrowBack")
        self.button_graph_main.setIcon(icon)
        self.button_graph_main.setObjectName("button_graph_main")
        self.verticalLayout_10.addWidget(self.button_graph_main)
        self.button_graph_average = QtWidgets.QPushButton(self.frame_graph_gbframe)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.button_graph_average.setFont(font)
        self.button_graph_average.setObjectName("button_graph_average")
        self.verticalLayout_10.addWidget(self.button_graph_average)
        self.combo_graph_sensors = QtWidgets.QComboBox(self.frame_graph_gbframe)
        self.combo_graph_sensors.setStyleSheet("QComboBox QAbstractItemView::item:hover {\n"
"    background-color: black;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    color: black;\n"
"}\n"
"QComboBox {\n"
"    text-align: center;\n"
"}\n"
"")
        self.combo_graph_sensors.setEditable(False)
        self.combo_graph_sensors.setObjectName("combo_graph_sensors")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.combo_graph_sensors.addItem("")
        self.verticalLayout_10.addWidget(self.combo_graph_sensors)
        self.verticalLayout_9.addWidget(self.frame_graph_gbframe, 0, QtCore.Qt.AlignTop)
        self.frame_graph_sframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_sframe.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_graph_sframe.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_graph_sframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_sframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_sframe.setObjectName("frame_graph_sframe")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_graph_sframe)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_graph_sframe)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/engine-gears-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_13.addWidget(self.pushButton_2)
        self.verticalLayout_9.addWidget(self.frame_graph_sframe)
        self.frame_graph_crlframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_crlframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_crlframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_crlframe.setObjectName("frame_graph_crlframe")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_graph_crlframe)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_graph_crllabel2 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel2.setObjectName("frame_graph_crllabel2")
        self.verticalLayout_11.addWidget(self.frame_graph_crllabel2)
        self.frame_graph_crllabel1 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel1.setObjectName("frame_graph_crllabel1")
        self.verticalLayout_11.addWidget(self.frame_graph_crllabel1)
        self.frame_graph_crllabel3 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel3.setObjectName("frame_graph_crllabel3")
        self.verticalLayout_11.addWidget(self.frame_graph_crllabel3)
        self.verticalLayout_9.addWidget(self.frame_graph_crlframe, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_29.addWidget(self.frame_graph_left)
        self.frame_graph_right = QtWidgets.QFrame(self.frame)
        self.frame_graph_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_right.setObjectName("frame_graph_right")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_graph_right)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_graph_swframe = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_swframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_swframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_swframe.setObjectName("frame_graph_swframe")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_graph_swframe)
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.swidget_graph_swgraph = QtWidgets.QStackedWidget(self.frame_graph_swframe)
        self.swidget_graph_swgraph.setObjectName("swidget_graph_swgraph")
        self.widget_main_graph = QtWidgets.QWidget()
        self.widget_main_graph.setObjectName("widget_main_graph")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_main_graph)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_graph_mlabel = QtWidgets.QFrame(self.widget_main_graph)
        self.frame_graph_mlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_mlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_mlabel.setObjectName("frame_graph_mlabel")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_graph_mlabel)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_graph_main = QtWidgets.QLabel(self.frame_graph_mlabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_main.setFont(font)
        self.label_graph_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_main.setObjectName("label_graph_main")
        self.verticalLayout_15.addWidget(self.label_graph_main, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_14.addWidget(self.frame_graph_mlabel, 0, QtCore.Qt.AlignTop)
        self.frame_graph_mgraph = QtWidgets.QFrame(self.widget_main_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graph_mgraph.sizePolicy().hasHeightForWidth())
        self.frame_graph_mgraph.setSizePolicy(sizePolicy)
        self.frame_graph_mgraph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_mgraph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_mgraph.setObjectName("frame_graph_mgraph")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_graph_mgraph)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_14.addWidget(self.frame_graph_mgraph)
        self.swidget_graph_swgraph.addWidget(self.widget_main_graph)
        self.widget_average_graph = QtWidgets.QWidget()
        self.widget_average_graph.setObjectName("widget_average_graph")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_average_graph)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_graph_avglabel = QtWidgets.QFrame(self.widget_average_graph)
        self.frame_graph_avglabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_avglabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_avglabel.setObjectName("frame_graph_avglabel")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_graph_avglabel)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_graph_average = QtWidgets.QLabel(self.frame_graph_avglabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_average.setFont(font)
        self.label_graph_average.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_average.setObjectName("label_graph_average")
        self.verticalLayout_17.addWidget(self.label_graph_average, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_16.addWidget(self.frame_graph_avglabel)
        self.frame_graph_avggraph = QtWidgets.QFrame(self.widget_average_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graph_avggraph.sizePolicy().hasHeightForWidth())
        self.frame_graph_avggraph.setSizePolicy(sizePolicy)
        self.frame_graph_avggraph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_avggraph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_avggraph.setObjectName("frame_graph_avggraph")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_graph_avggraph)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_16.addWidget(self.frame_graph_avggraph)
        self.swidget_graph_swgraph.addWidget(self.widget_average_graph)
        self.widget_sensors_graph = QtWidgets.QWidget()
        self.widget_sensors_graph.setObjectName("widget_sensors_graph")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_sensors_graph)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_graph_slabel = QtWidgets.QFrame(self.widget_sensors_graph)
        self.frame_graph_slabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_slabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_slabel.setObjectName("frame_graph_slabel")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_graph_slabel)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_graph_sensor = QtWidgets.QLabel(self.frame_graph_slabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_sensor.setFont(font)
        self.label_graph_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_sensor.setObjectName("label_graph_sensor")
        self.verticalLayout_19.addWidget(self.label_graph_sensor, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_18.addWidget(self.frame_graph_slabel)
        self.frame_graph_sgraph = QtWidgets.QFrame(self.widget_sensors_graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_graph_sgraph.sizePolicy().hasHeightForWidth())
        self.frame_graph_sgraph.setSizePolicy(sizePolicy)
        self.frame_graph_sgraph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_sgraph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_sgraph.setObjectName("frame_graph_sgraph")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_graph_sgraph)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_18.addWidget(self.frame_graph_sgraph)
        self.swidget_graph_swgraph.addWidget(self.widget_sensors_graph)
        self.horizontalLayout_26.addWidget(self.swidget_graph_swgraph)
        self.verticalLayout_12.addWidget(self.frame_graph_swframe)
        self.frame_graph_util = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_util.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_util.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_util.setObjectName("frame_graph_util")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_graph_util)
        self.horizontalLayout_27.setContentsMargins(-1, 0, 11, 5)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.button_graph_start = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_start.setObjectName("button_graph_start")
        self.horizontalLayout_27.addWidget(self.button_graph_start)
        self.button_graph_stop = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_stop.setObjectName("button_graph_stop")
        self.horizontalLayout_27.addWidget(self.button_graph_stop)
        self.button_graph_save = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_save.setObjectName("button_graph_save")
        self.horizontalLayout_27.addWidget(self.button_graph_save)
        self.verticalLayout_12.addWidget(self.frame_graph_util)
        self.frame_graph_info = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_info.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_graph_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_info.setObjectName("frame_graph_info")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_graph_info)
        self.horizontalLayout_28.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.frame_graph_inleft = QtWidgets.QFrame(self.frame_graph_info)
        self.frame_graph_inleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_inleft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_inleft.setObjectName("frame_graph_inleft")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_graph_inleft)
        self.verticalLayout_20.setContentsMargins(15, 10, 10, 10)
        self.verticalLayout_20.setSpacing(4)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_graph_id = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_id.setObjectName("label_graph_id")
        self.verticalLayout_20.addWidget(self.label_graph_id)
        self.label_graph_name = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_name.setObjectName("label_graph_name")
        self.verticalLayout_20.addWidget(self.label_graph_name)
        self.label_graph_gender = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_gender.setObjectName("label_graph_gender")
        self.verticalLayout_20.addWidget(self.label_graph_gender)
        self.label_graph_umur = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_umur.setObjectName("label_graph_umur")
        self.verticalLayout_20.addWidget(self.label_graph_umur)
        self.horizontalLayout_28.addWidget(self.frame_graph_inleft, 0, QtCore.Qt.AlignVCenter)
        self.frame_graph_inright = QtWidgets.QFrame(self.frame_graph_info)
        self.frame_graph_inright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_inright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_inright.setObjectName("frame_graph_inright")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_graph_inright)
        self.verticalLayout_21.setContentsMargins(15, 10, 10, 10)
        self.verticalLayout_21.setSpacing(4)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_graph_max = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_max.setObjectName("label_graph_max")
        self.verticalLayout_21.addWidget(self.label_graph_max)
        self.label_graph_min = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_min.setObjectName("label_graph_min")
        self.verticalLayout_21.addWidget(self.label_graph_min)
        self.label_graph_avg = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_avg.setObjectName("label_graph_avg")
        self.verticalLayout_21.addWidget(self.label_graph_avg)
        self.horizontalLayout_28.addWidget(self.frame_graph_inright)
        self.verticalLayout_12.addWidget(self.frame_graph_info, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_29.addWidget(self.frame_graph_right)
        self.horizontalLayout_20.addWidget(self.frame)

    def retranslateUi(self, MainWindow, _translate):
        self.label_graph_tlabel.setText(_translate("MainWindow", "PLOT GRAPH"))
        self.button_graph_main.setText(_translate("MainWindow", "Main Graph"))
        self.button_graph_average.setText(_translate("MainWindow", "Average Graph"))
        self.combo_graph_sensors.setCurrentText(_translate("MainWindow", "Sensors Graph"))
        self.combo_graph_sensors.setItemText(0, _translate("MainWindow", "Sensors Graph"))
        self.combo_graph_sensors.setItemText(1, _translate("MainWindow", "Sensor 1"))
        self.combo_graph_sensors.setItemText(2, _translate("MainWindow", "Sensor 2"))
        self.combo_graph_sensors.setItemText(3, _translate("MainWindow", "Sensor 3"))
        self.combo_graph_sensors.setItemText(4, _translate("MainWindow", "Sensor 4"))
        self.combo_graph_sensors.setItemText(5, _translate("MainWindow", "Sensor 5"))
        self.combo_graph_sensors.setItemText(6, _translate("MainWindow", "Sensor 6"))
        self.combo_graph_sensors.setItemText(7, _translate("MainWindow", "Sensor 7"))
        self.combo_graph_sensors.setItemText(8, _translate("MainWindow", "Sensor 8"))
        self.combo_graph_sensors.setItemText(9, _translate("MainWindow", "Sensor 9"))
        self.pushButton_2.setText(_translate("MainWindow", " Load Graph"))
        self.frame_graph_crllabel2.setText(_translate("MainWindow", "Surface Gating App"))
        self.frame_graph_crllabel1.setText(_translate("MainWindow", "For Education Purposes Only"))
        self.frame_graph_crllabel3.setText(_translate("MainWindow", "All Rights Reserved"))
        self.label_graph_main.setText(_translate("MainWindow", "Main Graph"))
        self.label_graph_average.setText(_translate("MainWindow", "Average Graph"))
        self.label_graph_sensor.setText(_translate("MainWindow", "Sensor Graph"))
        self.button_graph_start.setText(_translate("MainWindow", "Start"))
        self.button_graph_stop.setText(_translate("MainWindow", "Reset"))
        self.button_graph_save.setText(_translate("MainWindow", "Save"))
        self.label_graph_id.setText(_translate("MainWindow", "ID : 1"))
        self.label_graph_name.setText(_translate("MainWindow", "Nama : Username"))
        self.label_graph_gender.setText(_translate("MainWindow", "Jenis Kelamin : Laki-laki"))
        self.label_graph_umur.setText(_translate("MainWindow", "Usia : 20"))
        self.label_graph_max.setText(_translate("MainWindow", "Max : 100 mm"))
        self.label_graph_min.setText(_translate("MainWindow", "Min : 2 mm"))
        self.label_graph_avg.setText(_translate("MainWindow", "Average : 51 mm"))


    