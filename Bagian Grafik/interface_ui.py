# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class AlignedDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignedDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.winmenu_graph = QtWidgets.QWidget(MainWindow)
        self.winmenu_graph.setStyleSheet("*\n"
"{\n"
"color: #fff;\n"
"font-family: \'Trebuchet MS\';\n"
"font-size: 16px;\n"
"border: nine;\n"
"background: none;\n"
"}\n"
"#frame_graph_gbframe QComboBox\n"
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
        self.winmenu_graph.setObjectName("winmenu_graph")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.winmenu_graph)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_graph_left = QtWidgets.QWidget(self.winmenu_graph)
        self.frame_graph_left.setObjectName("frame_graph_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_graph_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_graph_tframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_tframe.setMinimumSize(QtCore.QSize(200, 80))
        self.frame_graph_tframe.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_graph_tframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_tframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_tframe.setObjectName("frame_graph_tframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_graph_tframe)
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_graph_ticon = QtWidgets.QLabel(self.frame_graph_tframe)
        self.label_graph_ticon.setMinimumSize(QtCore.QSize(40, 40))
        self.label_graph_ticon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_graph_ticon.setText("")
        self.label_graph_ticon.setPixmap(QtGui.QPixmap(":/icons/icons/bar-chart-icon.svg"))
        self.label_graph_ticon.setScaledContents(True)
        self.label_graph_ticon.setObjectName("label_graph_ticon")
        self.horizontalLayout_2.addWidget(self.label_graph_ticon, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_graph_tlabel = QtWidgets.QLabel(self.frame_graph_tframe)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_graph_tlabel.setFont(font)
        self.label_graph_tlabel.setObjectName("label_graph_tlabel")
        self.horizontalLayout_2.addWidget(self.label_graph_tlabel, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_graph_tframe)
        self.frame_graph_gbframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_gbframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_gbframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_gbframe.setObjectName("frame_graph_gbframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_graph_gbframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_graph_main = QtWidgets.QPushButton(self.frame_graph_gbframe)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.button_graph_main.setFont(font)
        icon = QtGui.QIcon.fromTheme("SP_ArrowBack")
        self.button_graph_main.setIcon(icon)
        self.button_graph_main.setObjectName("button_graph_main")
        self.verticalLayout_2.addWidget(self.button_graph_main)
        self.button_graph_average = QtWidgets.QPushButton(self.frame_graph_gbframe)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.button_graph_average.setFont(font)
        self.button_graph_average.setObjectName("button_graph_average")
        self.verticalLayout_2.addWidget(self.button_graph_average)
        self.combo_graph_sensors = QtWidgets.QComboBox(self.frame_graph_gbframe)
        self.combo_graph_sensors.setStyleSheet("QComboBox QAbstractItemView { background-color: rgba(33, 43, 51, 100);}\n QComboBox {text-align: center;};")
        self.combo_graph_sensors.setItemDelegate(AlignedDelegate(self.combo_graph_sensors))
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
        self.verticalLayout_2.addWidget(self.combo_graph_sensors)
        self.verticalLayout.addWidget(self.frame_graph_gbframe, 0, QtCore.Qt.AlignTop)
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
        self.pushButton = QtWidgets.QPushButton(self.frame_graph_sframe)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/engine-gears-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_13.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_graph_sframe)
        self.frame_graph_crlframe = QtWidgets.QFrame(self.frame_graph_left)
        self.frame_graph_crlframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_crlframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_crlframe.setObjectName("frame_graph_crlframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_graph_crlframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_graph_crllabel2 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel2.setObjectName("frame_graph_crllabel2")
        self.verticalLayout_3.addWidget(self.frame_graph_crllabel2)
        self.frame_graph_crllabel1 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel1.setObjectName("frame_graph_crllabel1")
        self.verticalLayout_3.addWidget(self.frame_graph_crllabel1)
        self.frame_graph_crllabel3 = QtWidgets.QLabel(self.frame_graph_crlframe)
        self.frame_graph_crllabel3.setObjectName("frame_graph_crllabel3")
        self.verticalLayout_3.addWidget(self.frame_graph_crllabel3)
        self.verticalLayout.addWidget(self.frame_graph_crlframe, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_graph_left)
        self.frame_graph_right = QtWidgets.QFrame(self.winmenu_graph)
        self.frame_graph_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_right.setObjectName("frame_graph_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_graph_right)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_graph_head = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_head.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_graph_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_head.setObjectName("frame_graph_head")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_graph_head)
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_graph_menu = QtWidgets.QFrame(self.frame_graph_head)
        self.frame_graph_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_menu.setObjectName("frame_graph_menu")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_graph_menu)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_graph_menu = QtWidgets.QPushButton(self.frame_graph_menu)
        self.button_graph_menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/menu-bar-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_graph_menu.setIcon(icon1)
        self.button_graph_menu.setIconSize(QtCore.QSize(30, 30))
        self.button_graph_menu.setObjectName("button_graph_menu")
        self.horizontalLayout_5.addWidget(self.button_graph_menu)
        self.label_graph_menu = QtWidgets.QLabel(self.frame_graph_menu)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_menu.setFont(font)
        self.label_graph_menu.setObjectName("label_graph_menu")
        self.horizontalLayout_5.addWidget(self.label_graph_menu)
        self.horizontalLayout_4.addWidget(self.frame_graph_menu, 0, QtCore.Qt.AlignLeft)
        self.frame_graph_dash = QtWidgets.QFrame(self.frame_graph_head)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.frame_graph_dash.setFont(font)
        self.frame_graph_dash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_dash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_dash.setObjectName("frame_graph_dash")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_graph_dash)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_graph_dash = QtWidgets.QLabel(self.frame_graph_dash)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_dash.setFont(font)
        self.label_graph_dash.setObjectName("label_graph_dash")
        self.horizontalLayout_6.addWidget(self.label_graph_dash)
        self.horizontalLayout_4.addWidget(self.frame_graph_dash, 0, QtCore.Qt.AlignHCenter)
        self.frame_graph_nav = QtWidgets.QFrame(self.frame_graph_head)
        self.frame_graph_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_nav.setObjectName("frame_graph_nav")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_graph_nav)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_graph_minimize = QtWidgets.QPushButton(self.frame_graph_nav)
        self.button_graph_minimize.setMinimumSize(QtCore.QSize(30, 30))
        self.button_graph_minimize.setMaximumSize(QtCore.QSize(30, 30))
        self.button_graph_minimize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/minus-sign-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_graph_minimize.setIcon(icon2)
        self.button_graph_minimize.setObjectName("button_graph_minimize")
        self.horizontalLayout_7.addWidget(self.button_graph_minimize)
        self.button_graph_expand = QtWidgets.QPushButton(self.frame_graph_nav)
        self.button_graph_expand.setMinimumSize(QtCore.QSize(30, 30))
        self.button_graph_expand.setMaximumSize(QtCore.QSize(30, 30))
        self.button_graph_expand.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/aspect-ratio-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_graph_expand.setIcon(icon3)
        self.button_graph_expand.setObjectName("button_graph_expand")
        self.horizontalLayout_7.addWidget(self.button_graph_expand)
        self.button_graph_close = QtWidgets.QPushButton(self.frame_graph_nav)
        self.button_graph_close.setMinimumSize(QtCore.QSize(30, 30))
        self.button_graph_close.setMaximumSize(QtCore.QSize(30, 30))
        self.button_graph_close.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/close-window-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_graph_close.setIcon(icon4)
        self.button_graph_close.setObjectName("button_graph_close")
        self.horizontalLayout_7.addWidget(self.button_graph_close)
        self.horizontalLayout_4.addWidget(self.frame_graph_nav, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame_graph_head, 0, QtCore.Qt.AlignTop)
        self.frame_graph_swframe = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_swframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_swframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_swframe.setObjectName("frame_graph_swframe")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_graph_swframe)
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.swidget_graph_swgraph = QtWidgets.QStackedWidget(self.frame_graph_swframe)
        self.swidget_graph_swgraph.setObjectName("swidget_graph_swgraph")
        self.widget_main_graph = QtWidgets.QWidget()
        self.widget_main_graph.setObjectName("widget_main_graph")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_main_graph)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_graph_mlabel = QtWidgets.QFrame(self.widget_main_graph)
        self.frame_graph_mlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_mlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_mlabel.setObjectName("frame_graph_mlabel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_graph_mlabel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_graph_main = QtWidgets.QLabel(self.frame_graph_mlabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_main.setFont(font)
        self.label_graph_main.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_main.setObjectName("label_graph_main")
        self.verticalLayout_6.addWidget(self.label_graph_main, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_graph_mlabel, 0, QtCore.Qt.AlignTop)
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
        self.verticalLayout_5.addWidget(self.frame_graph_mgraph)
        self.swidget_graph_swgraph.addWidget(self.widget_main_graph)
        self.widget_average_graph = QtWidgets.QWidget()
        self.widget_average_graph.setObjectName("widget_average_graph")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_average_graph)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_graph_avglabel = QtWidgets.QFrame(self.widget_average_graph)
        self.frame_graph_avglabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_avglabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_avglabel.setObjectName("frame_graph_avglabel")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_graph_avglabel)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_graph_average = QtWidgets.QLabel(self.frame_graph_avglabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_average.setFont(font)
        self.label_graph_average.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_average.setObjectName("label_graph_average")
        self.verticalLayout_7.addWidget(self.label_graph_average, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_8.addWidget(self.frame_graph_avglabel)
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
        self.verticalLayout_8.addWidget(self.frame_graph_avggraph)
        self.swidget_graph_swgraph.addWidget(self.widget_average_graph)
        self.widget_sensors_graph = QtWidgets.QWidget()
        self.widget_sensors_graph.setObjectName("widget_sensors_graph")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_sensors_graph)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_graph_slabel = QtWidgets.QFrame(self.widget_sensors_graph)
        self.frame_graph_slabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_slabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_slabel.setObjectName("frame_graph_slabel")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_graph_slabel)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_graph_sensor = QtWidgets.QLabel(self.frame_graph_slabel)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_graph_sensor.setFont(font)
        self.label_graph_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_graph_sensor.setObjectName("label_graph_sensor")
        self.verticalLayout_9.addWidget(self.label_graph_sensor, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_graph_slabel)
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
        self.verticalLayout_10.addWidget(self.frame_graph_sgraph)
        self.swidget_graph_swgraph.addWidget(self.widget_sensors_graph)
        self.horizontalLayout_10.addWidget(self.swidget_graph_swgraph)
        self.verticalLayout_4.addWidget(self.frame_graph_swframe)
        self.frame_graph_util = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_util.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_util.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_util.setObjectName("frame_graph_util")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_graph_util)
        self.horizontalLayout_17.setContentsMargins(-1, 0, 11, 5)
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.button_graph_start = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_start.setObjectName("button_graph_start")
        self.horizontalLayout_17.addWidget(self.button_graph_start)
        self.button_graph_stop = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_stop.setObjectName("button_graph_stop")
        self.horizontalLayout_17.addWidget(self.button_graph_stop)
        self.button_graph_save = QtWidgets.QPushButton(self.frame_graph_util)
        self.button_graph_save.setObjectName("button_graph_save")
        self.horizontalLayout_17.addWidget(self.button_graph_save)
        self.verticalLayout_4.addWidget(self.frame_graph_util)
        self.frame_graph_info = QtWidgets.QFrame(self.frame_graph_right)
        self.frame_graph_info.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_graph_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_info.setObjectName("frame_graph_info")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_graph_info)
        self.horizontalLayout_8.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_graph_inleft = QtWidgets.QFrame(self.frame_graph_info)
        self.frame_graph_inleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_inleft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_inleft.setObjectName("frame_graph_inleft")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_graph_inleft)
        self.verticalLayout_11.setContentsMargins(15, 10, 10, 10)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_graph_id = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_id.setObjectName("label_graph_id")
        self.verticalLayout_11.addWidget(self.label_graph_id)
        self.label_graph_name = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_name.setObjectName("label_graph_name")
        self.verticalLayout_11.addWidget(self.label_graph_name)
        self.label_graph_gender = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_gender.setObjectName("label_graph_gender")
        self.verticalLayout_11.addWidget(self.label_graph_gender)
        self.label_graph_umur = QtWidgets.QLabel(self.frame_graph_inleft)
        self.label_graph_umur.setObjectName("label_graph_umur")
        self.verticalLayout_11.addWidget(self.label_graph_umur)
        self.horizontalLayout_8.addWidget(self.frame_graph_inleft, 0, QtCore.Qt.AlignVCenter)
        self.frame_graph_inright = QtWidgets.QFrame(self.frame_graph_info)
        self.frame_graph_inright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph_inright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_graph_inright.setObjectName("frame_graph_inright")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_graph_inright)
        self.verticalLayout_12.setContentsMargins(15, 10, 10, 10)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_graph_max = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_max.setObjectName("label_graph_max")
        self.verticalLayout_12.addWidget(self.label_graph_max)
        self.label_graph_min = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_min.setObjectName("label_graph_min")
        self.verticalLayout_12.addWidget(self.label_graph_min)
        self.label_graph_avg = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_avg.setObjectName("label_graph_avg")
        self.verticalLayout_12.addWidget(self.label_graph_avg)
        self.label_graph_rate = QtWidgets.QLabel(self.frame_graph_inright)
        self.label_graph_rate.setObjectName("label_graph_rate")
        self.verticalLayout_12.addWidget(self.label_graph_rate)
        self.horizontalLayout_8.addWidget(self.frame_graph_inright)
        self.verticalLayout_4.addWidget(self.frame_graph_info, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame_graph_right)
        MainWindow.setCentralWidget(self.winmenu_graph)

        self.retranslateUi(MainWindow)
        self.swidget_graph_swgraph.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton.setText(_translate("MainWindow", "  Settings"))
        self.frame_graph_crllabel2.setText(_translate("MainWindow", "Surface Gating App"))
        self.frame_graph_crllabel1.setText(_translate("MainWindow", "For Education Purposes Only"))
        self.frame_graph_crllabel3.setText(_translate("MainWindow", "All Rights Reserved"))
        self.label_graph_menu.setText(_translate("MainWindow", "MENU"))
        self.label_graph_dash.setText(_translate("MainWindow", "DASHBOARD"))
        self.label_graph_main.setText(_translate("MainWindow", "Main Graph"))
        self.label_graph_average.setText(_translate("MainWindow", "Average Graph"))
        self.label_graph_sensor.setText(_translate("MainWindow", "Sensor Graph"))
        self.button_graph_start.setText(_translate("MainWindow", "Start"))
        self.button_graph_stop.setText(_translate("MainWindow", "Stop"))
        self.button_graph_save.setText(_translate("MainWindow", "Save"))
        self.label_graph_id.setText(_translate("MainWindow", "ID : 1"))
        self.label_graph_name.setText(_translate("MainWindow", "Name : Username"))
        self.label_graph_gender.setText(_translate("MainWindow", "Gender : Laki-laki"))
        self.label_graph_umur.setText(_translate("MainWindow", "Umur : 20"))
        self.label_graph_max.setText(_translate("MainWindow", "Max : 0 cm"))
        self.label_graph_min.setText(_translate("MainWindow", "Min : 0 cm"))
        self.label_graph_avg.setText(_translate("MainWindow", "Average : 0 cm"))
        self.label_graph_rate.setText(_translate("MainWindow", "Rate : 0 cm/s"))
import resources_rc
