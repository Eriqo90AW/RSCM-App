import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore

class LineGraph:
    def __init__(self):
        self.time_recorded  = np.array([0]) #koordinat sumbu x
        self.lines_1        = np.array([0])#sinus
        self.lines_2        = np.array([1]) #cosinus
        self.lines_3        = np.array([0])# mutlak sinus
        self.lines_avg      = (self.lines_1+self.lines_2 +self.lines_3)/3 #rata-rata
        self.current_time   = 0
        self.step           = 0.0174533 # 1 derajat = 0.0174533 radian
        self.duration       = round(1000/60) #1000 milisekon/frame per second
        self.lower_bound    = 0
        self.upper_bound    = 5

        # Create a widget to hold the plot
        self.plot_widget = pg.PlotWidget()

        # Set the title and labels for the plot
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle(" ", color="#F59100", size="2pt")
        self.styles = {"color": "#F59100", "font-size": "10px"}
        self.plot_widget.setLabel("left", "Range (mm)", **self.styles)
        self.plot_widget.setLabel("bottom", "Seconds (s)", **self.styles)

        # Set the y range of the plot
        self.plot_widget.setYRange(-1.2, 1.2, padding=0)

        # Show the grid lines
        self.plot_widget.showGrid(x=True, y=True)

        # create a pen of different colors to use for the graph
        self.pen1 = pg.mkPen(color='k', width=2)
        self.pen2 = pg.mkPen(color='r', width=2)
        self.pen3 = pg.mkPen(color='g', width=2)
        self.pen4 = pg.mkPen(color='b', width=2)
    
        #curve
        self.curve1     = self.plot_widget.plot(self.time_recorded, self.lines_1, pen=self.pen1)
        self.curve2     = self.plot_widget.plot(self.time_recorded, self.lines_2, pen=self.pen2)
        self.curve3     = self.plot_widget.plot(self.time_recorded, self.lines_3, pen=self.pen3)
        self.curve_avg  = self.plot_widget.plot(self.time_recorded, self.lines_avg, pen=self.pen4)
        
        # update graph every 1 second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.graphUpdate)
        self.timer.start(self.duration)
        
    # method to update the graph
    def graphUpdate(self):
        # append new random number to the list
        self.time_recorded  = np.append(self.time_recorded, self.current_time)
        self.current_time   +=self.step
        self.lines_1        =np.append(self.lines_1,    (np.sin(self.current_time))) #sinus
        self.lines_2        =np.append(self.lines_2,    (np.cos(self.current_time))) #cosinus
        self.lines_3        =np.append(self.lines_3,    np.absolute(np.sin(self.current_time)) ) # mutlak sinus
        self.lines_avg      =np.append(self.lines_avg,  (self.lines_1[-1]+self.lines_2[-1] +self.lines_3[-1])/3) #rata-rata

        # update the graph
        self.curve1.setData(self.time_recorded, self.lines_1)
        self.curve2.setData(self.time_recorded, self.lines_2)
        self.curve3.setData(self.time_recorded, self.lines_3)
        self.curve_avg.setData(self.time_recorded, self.lines_avg)