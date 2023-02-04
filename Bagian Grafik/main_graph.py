from PyQt5.QtWidgets import QApplication, QMainWindow

# import interface ui file
from interface_ui import *

# import the LineGraph class from grafik_numpy.py
from grafik_numpy import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.paused = True
        self.currentGraph = "main"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a new graph widget
        self.graph = Graph(self.ui.label_graph_max, self.ui.label_graph_min)
        
        # Add the widget to the frame inside the stacked widget
        self.ui.frame_graph_mgraph.layout().addWidget(self.graph.plot_widget)

        # Initial graph setup
        self.mainGraphInit()

        # Connect the buttons to the methods
        self.initButtons()

        # Show the widget
        self.show()

    # method to connect the buttons to the methods
    def initButtons(self):
        self.ui.button_graph_start.clicked.connect(lambda: self.startButton())
        self.ui.button_graph_stop.clicked.connect(lambda: self.stopButton())
        self.ui.button_graph_save.clicked.connect(lambda: self.saveButton())

        self.ui.button_graph_main.clicked.connect(lambda: self.mainGraphInit())
        self.ui.button_graph_average.clicked.connect(lambda: self.averageGraphInit())

    # method to start and pause the graph
    def startButton(self):
        if self.paused:
            self.graph.stopGraph()
            self.graph.startGraph(self.currentGraph)
            self.ui.button_graph_start.setText("Pause")
            self.paused = False
        elif self.paused == False:
            self.graph.pauseGraph()
            self.ui.button_graph_start.setText("Start")
            self.paused = True
    
    # method to stop and reset the graph
    def stopButton(self):
        self.graph.pauseGraph()
        self.ui.button_graph_start.setText("Start")
        self.paused = True
        self.graph.stopGraph()

    # method to save the graph
    def saveButton(self):
        self.graph.saveGraph()
    
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

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Real-Time Graph")
    window.show()
    app.exec_()