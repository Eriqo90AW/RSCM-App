from PyQt5.QtWidgets import QApplication, QMainWindow

# import interface ui file
from interface import *

# import the LineGraph class from grafik_numpy.py
from grafik_numpy import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a new graph widget
        self.main_graph = LineGraph()
        
        # Add the widget to the frame inside the stacked widget
        self.ui.frame_16.layout().addWidget(self.main_graph.plot_widget)

        # Show the widget
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Simple Graph")
    window.show()
    app.exec_()