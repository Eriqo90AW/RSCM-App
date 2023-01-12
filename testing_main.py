import pyqtgraph as pg
import random
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# import the LineGraph class from testing_line_graph.py
# from testing_line_graph import LineGraph

from main_ui import *

class MainWindow(Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.buttonInit()
        self.stackedWidget.setCurrentIndex(0)

        # # create an instance of the LineGraph class
        # self.line_graph = LineGraph()
        
        # # add the plot widget to the main window
        # self.setCentralWidget(self.line_graph.plot_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("test Bruh")
    window.show()
    app.exec_()
