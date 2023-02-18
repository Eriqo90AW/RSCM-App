from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
# import interface ui file
from interface_ui import *

# import the LineGraph class from grafik_numpy.py
from grafik_18_02 import *

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

        # Connect the closeEvent signal to the closewindow method
        self.closeEvent = self.closewindow # dari def closewindow(self, event):

        # Show the widget
        self.show()

    # method to connect the buttons to the methods
    def initButtons(self):
        self.ui.button_graph_save.clicked.connect(lambda: self.saveButton())
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
    
    def saveButton(self):
        self.graph.saveGraph()
        self.ui.button_graph_save.setText("Save")
    
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


    #function nyoba ketika program ditutup
    def closewindow(self, event):
        #mengambil nilai dari def array_sensor(self) pada class Graph
        seluruh_sensor, average= self.graph.array_sensor() 
        #for i in range(1,len(seluruh_sensor)+1):
            #seluruh_sensor["sensor%d"%i] =np.asarray(seluruh_sensor["sensor%d"%i])
       # average=np.asarray(average)

        print("\nrata-rata:", average, "\n")
        print("size rata-rata: ",average.__sizeof__()," bytes\n")

        for i in range(1,len(seluruh_sensor)+1):
            print("sensor%d:"%i, seluruh_sensor["sensor%d"%i])
            print("sensor%d:"%i, seluruh_sensor["sensor%d"%i].__sizeof__(),"bytes\n")
        # simpan seluruh sensor
          #  with open("simpan1.txt","a") as f:
               # np.savetxt(f, (seluruh_sensor["sensor%d"%i], ), fmt="%d", delimiter=',', header="sensor%d: "%i) 
        # simpan average array
       # with open("simpan1.txt","a") as f:
           # np.savetxt(f, (average, ), fmt="%d", delimiter=',', header="average: ") # simpan average array
                
        # Call the default implementation of the closeEvent to actually close the window
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Simple Graph")
    window.show()
    sys.exit(app.exec_())
