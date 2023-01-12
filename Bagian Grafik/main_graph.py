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

    def closeEvent(self, event):

        print("asdasdasdas")
        QMessageBox()
        # close window
        event.accept()

    # def closeEvent(self, event):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Question)

    #     # setting message for Message Box
    #     msg.setText("Question")
        
    #     # setting Message box window title
    #     msg.setWindowTitle("Question MessageBox")
        
    #     # declaring buttons on Message Box
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
    #     # start the app
    #     retval = msg.exec_()
    #     if can_exit:
    #         event.accept() # let the window close
    #     else:
    #         event.ignore()
    
    def myExitHandler():
        print("test Bruh")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Simple Graph")
    window.show()
    app.exec_()