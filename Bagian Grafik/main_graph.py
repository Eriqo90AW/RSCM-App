from PyQt5.QtWidgets import QApplication, QMainWindow

# import interface ui file
from interface_ui import *

# import the LineGraph class from grafik_numpy.py
from grafik_numpy import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.paused = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a new graph widget
        self.main_graph = LineGraph(self.ui.label_graph_max, self.ui.label_graph_min)
        
        # Add the widget to the frame inside the stacked widget
        self.ui.frame_graph_mgraph.layout().addWidget(self.main_graph.plot_widget)

        # Set the initial text for the labels
        self.ui.label_graph_max.setText("Max : 0 mm")
        self.ui.label_graph_min.setText("Min : 0 mm")

        # Connect the buttons to the methods
        self.initButtons()

        # Show the widget
        self.show()

    # method to connect the buttons to the methods
    def initButtons(self):
        self.ui.button_graph_start.clicked.connect(lambda: self.startButton())
        self.ui.button_graph_stop.clicked.connect(lambda: self.stopButton())

    # method to start and pause the graph
    def startButton(self):
        if not self.paused:
            self.main_graph.startGraph()
            self.ui.button_graph_start.setText("Pause")
            self.paused = True
        elif self.paused:
            self.main_graph.pauseGraph()
            self.ui.button_graph_start.setText("Start")
            self.paused = False
    
    #method to stop and reset the graph
    def stopButton(self):
        self.main_graph.pauseGraph()
        self.ui.button_graph_start.setText("Start")
        self.paused = False
        self.main_graph.stopGraph()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Simple Graph")
    window.show()
    app.exec_()