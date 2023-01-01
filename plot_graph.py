import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pyqtgraph as pg

from ui_app import Ui_MainWindow

def initGraph(self):
        self.widget_graph.setBackground('w')
        self.widget_graph.setTitle("Main Graph", color="#F59100", size="13pt")

        styles = {"color": "#F59100", "font-size": "10px"}
        self.widget_graph.setLabel("left", "Range (mm)", **styles)
        self.widget_graph.setLabel("bottom", "Seconds (s)", **styles)
        pen = pg.mkPen(color='k', width=2)

        self.curve = self.widget_graph.plot(pen=pen)
        self.widget_graph.setYRange(0, 1500, padding=0)
        self.widget_graph.showGrid(x=True, y=True)

class PlotGraph(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(PlotGraph, self).__init__(*args, **kwargs)
        self.widget_graph = pg.PlotWidget()
        # array to hold random numbers
        self.array_x = []
        self.array_y = []
        
        initGraph(self)
        # update graph every 1 second
        timer = QtCore.QTimer()
        timer.timeout.connect(self.graphUpdate)
        timer.start(1000)

    # updating the graph
    def graphUpdate(self):
        print("updating graph now")
        x_values, y_values = self.get_new_data()

        # update the curve with the random data
        self.curve.setData(x_values, y_values)

    # generating random data
    def get_new_data(self):
        random_x = 0.01
        random_y = random.randint(600, 1200)
        self.array_x.append(random_x)
        self.array_y.append(random_y)
        return self.array_x, self.array_y

if __name__ == "__main__":
    app = QApplication([])
    window = PlotGraph()
    window.show()
    app.exec_()