from PyQt5 import QtCore, QtGui

# from graphs.graph_sim import GraphSim
from graphs.graph_arduino import *

class GraphLogic:
    def __init__(self, main_window):
        self.main_window = main_window
        self.paused = True
        self.currentGraph = "main"
        self.first_time = True

        self.graph = GraphArduino()

        self.main_window.ui.swidget_graph_swgraph.setCurrentIndex(0)
        self.main_window.ui.frame_graph_mgraph.layout().addWidget(self.graph.plot_widget)

        # Connect the buttons to the methods
        self.initButtons()

    # method to connect the buttons to the methods
    def initButtons(self):
        self.main_window.ui.button_graph_save.clicked.connect(lambda: self.saveButton())
        self.main_window.ui.button_graph_start.clicked.connect(lambda: self.startButton())
        self.main_window.ui.button_graph_stop.clicked.connect(lambda: self.stopButton())

        self.main_window.ui.button_graph_main.clicked.connect(lambda: self.mainGraphInit())
        self.main_window.ui.button_graph_average.clicked.connect(lambda: self.averageGraphInit())
        self.main_window.ui.button_graph_load.clicked.connect(lambda: self.loadGraphInit())
        self.main_window.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())

        # self.main_window.ui.button_login_exit.clicked.connect(lambda: self.printData())

    # method to connect the close event to the method (called by login.py)
    def initPatient(self):
        self.main_window.ui.label_graph_id.setText(f"ID : {self.main_window.current_patient['id']}")
        self.main_window.ui.label_graph_name.setText(f"Nama : {capitalize_first_letter(self.main_window.current_patient['nama'])}")
        self.main_window.ui.label_graph_umur.setText(f"Usia : {self.main_window.current_patient['usia']}")
        self.main_window.ui.label_graph_gender.setText(f"Jenis Kelamin : {capitalize_first_letter(self.main_window.current_patient['jenis_kelamin'])}")

    # method to start and pause the graph
    def startButton(self):
        # run the graph if it's the first time
        if self.first_time:
            self.graph.initGraph()
            self.first_time = False
        if self.paused:
            self.graph.clearGraph
            self.graph.startGraph(self.currentGraph)
            self.main_window.ui.button_graph_start.setText("Pause")
            self.paused = False
        elif self.paused == False:
            self.graph.pauseGraph(self.first_time)
            self.main_window.ui.button_graph_start.setText("Start")
            self.paused = True
    
    # method to stop and reset the graph
    def stopButton(self):
        self.graph.pauseGraph(self.first_time)
        self.main_window.ui.button_graph_start.setText("Start")
        self.paused = True
        self.graph.stopGraph(self.first_time)
    
    def saveButton(self):
        self.paused==True
        self.graph.saveGraph()
    
    def mainGraphInit(self):
        self.currentGraph = "main"
        self.main_window.ui.label_graph_main.setText("Main Graph")
        self.graph.clearGraph()
        self.paused = not self.paused
        self.startButton()
        self.main_window.ui.button_graph_average.setStyleSheet("")
        self.main_window.ui.button_graph_main.setStyleSheet("background-color: rgba(61, 80, 95, 100);")

    def averageGraphInit(self):
        self.currentGraph = "average"
        self.main_window.ui.label_graph_main.setText("Average Graph")
        self.graph.clearGraph()
        self.paused = not self.paused
        self.startButton()
        self.main_window.ui.button_graph_main.setStyleSheet("")
        self.main_window.ui.button_graph_average.setStyleSheet("background-color: rgba(61, 80, 95, 100);")
    
    def sensorsGraphInit(self):
        sensor_name = self.main_window.ui.combo_graph_sensors.currentText()
        self.main_window.ui.label_graph_main.setText(sensor_name)
        self.currentGraph = sensor_name
        self.graph.clearGraph()
        self.paused = not self.paused
        self.startButton()
        self.main_window.ui.button_graph_main.setStyleSheet("")
        self.main_window.ui.button_graph_average.setStyleSheet("")
    
    def loadGraphInit(self):
        self.graph.loadGraph()

    def printData(self):
        seluruh_sensor, average= self.graph.array_sensor() 

        print("\nrata-rata:", average, "\n")
        print("size rata-rata: ",average.__sizeof__()," bytes\n")

        for i in range(1,len(seluruh_sensor)+1):
            print("sensor%d:"%i, seluruh_sensor["arr_sensor%d"%i])
            print("sensor%d:"%i, seluruh_sensor["arr_sensor%d"%i].__sizeof__(),"bytes\n")

# utilities functions
def capitalize_first_letter(word):
    if len(word) > 0:
        return word[0].upper() + word[1:]
    else:
        return word
