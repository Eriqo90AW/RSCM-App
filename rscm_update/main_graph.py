from PyQt5.QtWidgets import QApplication, QMainWindow

# import interface ui file
from interface_ui import *

# import the LineGraph class from grafik_numpy.py
from grafik_14_02 import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.paused = True
        self.currentGraph = "main"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a new graph widget
        self.graph = Graph()
        
        # Add the widget to the frame inside the stacked widget
        self.ui.frame_graph_mgraph.layout().addWidget(self.graph.plot_widget)

        # Initial graph setup
        self.mainGraphInit()
        #self.stopButton()

        # Connect the buttons to the methods
        self.initButtons()

        # Show the widget
        self.show()

    # method to connect the buttons to the methods
    def initButtons(self):
        self.ui.button_graph_start.clicked.connect(lambda: self.startButton())
        self.ui.button_graph_stop.clicked.connect(lambda: self.stopButton())
        self.ui.button_graph_main.clicked.connect(lambda: self.mainGraphInit())
        self.ui.button_graph_average.clicked.connect(lambda: self.averageGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())
        self.ui.combo_graph_sensors.currentIndexChanged.connect(lambda: self.sensorsGraphInit())

    # method to start and pause the graph
    def startButton(self):
        if self.paused:
            self.graph.stopGraph()
            self.graph.startGraph(self.currentGraph)
            self.ui.button_graph_start.setText("Pause")
            self.paused =  False
        elif self.paused == False:
            self.graph.pauseGraph()
            self.ui.button_graph_start.setText("Start")
            self.paused = True
    
    #method to stop and reset the graph
    def stopButton(self):
        self.graph.pauseGraph()
        self.ui.button_graph_start.setText("Start")
        self.paused = True
        self.graph.stopGraph()
    
    def mainGraphInit(self):
        self.currentGraph = "main"
        self.graph.stopGraph()
        self.paused = not self.paused
        self.startButton()
        self.ui.button_graph_average.setStyleSheet("")
        self.ui.button_graph_main.setStyleSheet("background-color: rgba(61, 80, 95, 100);")

    def averageGraphInit(self):
        self.currentGraph = "average"
        self.graph.stopGraph()
        self.paused = not self.paused
        self.startButton()
        self.ui.button_graph_main.setStyleSheet("")
        self.ui.button_graph_average.setStyleSheet("background-color: rgba(61, 80, 95, 100);")
    def sensorsGraphInit(self):
        sensor_name = self.ui.combo_graph_sensors.currentText()
        self.currentGraph = sensor_name
        self.graph.stopGraph()
        self.paused = not self.paused
        self.startButton()
        self.ui.button_graph_main.setStyleSheet("")
        self.ui.button_graph_average.setStyleSheet("")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Simple Graph")
    window.show()
    app.exec_()