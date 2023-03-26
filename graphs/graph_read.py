import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore
import serial.tools.list_ports
import time
import serial
import numpy as np
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import datetime
import json
import os

class GraphRead:
    def __init__(self, main_window):
        self.main_window = main_window
        self.banyak_sensor=9 # jumlah sensor 9 buah

        #---Inisiasi awal untuk sumbu Y-----
        self.hitung=0
        self.arr_average= [] # rata-rata
        #arr_sensor1
        self.arr_sensors={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
         "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
         "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []}
        self.arr_sensors2={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
         "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
         "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []}
        #------------------------------------------------------------------------
        self.time_recorded = []#sumbu X (menyimpan waktu berjalan)\
        self.time_recorded2 = []#sumbu X (menyimpan waktu berjalan)\
        self.current_time  = 0 # pegerakan awal sumbu X ( Waktu akan di increment pada "def waktu_sinyal()"" ) 
        self.duration      = round(1000) #1000 milisekon/frame per second

        # Create a widget to hold the plot
        self.plot_widget = pg.PlotWidget()

        # Set the title and labels for the plot
        self.plot_widget.setBackground('w') # warna putih
        self.plot_widget.setTitle(" ", color="#F59100", size="2pt")
        self.styles = {"color": "b", "font-size": "10px"}
        self.plot_widget.setLabel("left", "Range (mm)", **self.styles)
        self.plot_widget.setLabel("bottom", "Seconds (s)", **self.styles)

        # Set the y range of the plot
        self.plot_widget.setYRange(0, 700, padding=0)

        # Show the grid lines
        self.plot_widget.showGrid(x=True, y=True)

        # create a pen of different colors to use for the graph
        self.pen1   = pg.mkPen(color='k', width=2) #black
        self.pen2   = pg.mkPen(color='b', width=2) #blue
        self.pen3   = pg.mkPen(color='r', width=2) #red
        self.pen4   = pg.mkPen(color='#eb8934', width=2) #orange
        self.pen5   = pg.mkPen(color='g', width=2) #green
        self.pen6   = pg.mkPen(color='#34ebe8', width=2) #cyan
        self.pen7   = pg.mkPen(color='#8f34eb', width=2) #ungu
        self.pen8   = pg.mkPen(color='#ebd234', width=2) #kuning
        self.pen9   = pg.mkPen(color='#baeb34', width=2) #lime
        self.penavg = pg.mkPen(color='#eb34e1', width=2) #pink

        self.pens={"pen1": self.pen1, "pen2": self.pen2, "pen3": self.pen3, 
        "pen4":self.pen4, "pen5": self.pen5, "pen6": self.pen6, 
        "pen7": self.pen7, "pen8": self.pen8, "pen9": self.pen9}

        #-------------------------------------------------------
        self.curves={} # nanti curve di append ke sini
        self.curves2={}
        #-------------
        # add legend to the graph
        self.plot_widget.addLegend()
        # update graph every second
        self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(self.graphUpdate)
        #self.timer.timeout.connect(self.readGraph) 

        #self.timer.start(self.duration)
    
    # method to start the graph
    def startGraph(self, graph_type):
        self.graph_type = graph_type
        #curve
        if self.graph_type == 'main':
            for i in range(1, self.banyak_sensor+1):
                self.curves.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i][:self.hitung],name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )

            #-----------------------------------
                self.curves2.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded2, self.arr_sensors2["arr_sensor%d"%i][:self.hitung],name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )

        elif self.graph_type == 'average':
            self.curves_avg  = self.plot_widget.plot(self.time_recorded, self.arr_average[:self.hitung], name="average", pen=self.penavg)
            self.curves_avg2=self.plot_widget.plot(self.time_recorded2, self.arr_average2[:self.hitung], name="average", pen=self.penavg)
        # bila hanya salah satu sensor saja yang ditampilkan  
        else:
            for i in range(1, self.banyak_sensor+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curves.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i][:self.hitung], name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )
                

        self.timer.start(self.duration)
    # method to pause the graph
    def pauseGraph(self):
        # stop the timer to pause the graph
        self.timer.stop()

    # method to stop the graph
    def stopGraph(self):
        # clear the graph
        self.plot_widget.clear()
    
    def saveGraph(self):
        print("Clicked Save")
        pass

    def loadGraph(self):
        print("SAVEEE BISAAAAAAAAA")
        a=str(os.path.dirname(__file__))
        print(a)
        filenames, ignore=QFileDialog.getOpenFileNames(self.main_window, 'Open file', a)
        #fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:\\app\\Programming\\python\\rscm_update\\gabungin')
        #self.filename.setText(fname[0])
        self.arr_average2=[]
        print(filenames)
        if filenames:
            read_path=filenames[0]
            if len(filenames)>1:
                read_path2=filenames[1]
                with open(read_path2, 'r') as f:
                    self.data_json2 = json.load(f)
                panjang2 = len(self.data_json2)-1 #karena ada average sehingga di minus 1
                for i in range(1, panjang2+1):
                    self.arr_sensors2['arr_sensor%d'%i]= self.data_json2["arr_sensor%d"%i]
                self.arr_average2=self.data_json2["average"]
  
        panjang =len(self.arr_sensors)-1

        print(read_path)
        with open(read_path, 'r') as f:
            self.data_json = json.load(f)
        panjang = len(self.data_json)-1 #karena ada average sehingga di minus 1
        for i in range(1, panjang+1):
            self.arr_sensors['arr_sensor%d'%i]= self.data_json["arr_sensor%d"%i]
        self.arr_average=self.data_json["average"]

  
        panjang =len(self.arr_sensors)-1


        self.time_recorded=list(np.arange(len(self.arr_average))) # menjadi array untuk sumbu X
        self.time_recorded2=list(np.arange(len(self.arr_average2))) # menjadi array untuk sumbu X
        print(self.time_recorded)
         # update the graph
        if self.graph_type  == 'main':
            for i in range(1, panjang+1):
                self.curves["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])
                self.curves2["curve%d"%i].setData(self.time_recorded2, self.arr_sensors2["arr_sensor%d"%i])

        elif self.graph_type == 'average':
            #self.curves_avg.setData(self.array_time,self.arr_average)
            self.curves_avg.setData(self.time_recorded, self.arr_average)
            self.curves_avg2.setData(self.time_recorded2, self.arr_average2)


        else:
            for i in range(1, panjang+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curves["curve%d"%i].setData(self.time_recorded,self.arr_sensors["arr_sensor%d"%i])

    def graphUpdate(self):

        print("UPDATE")
        panjang =len(self.arr_sensors)-1
        print(10)
        self.current_time +=1
        self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
         # update the graph
        try:
            if self.graph_type  == 'main':
                for i in range(1, panjang+1):
                    self.curves["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])

            elif self.graph_type == 'average':
                #self.curves_avg.setData(self.array_time,self.arr_average)
                self.curves_avg.setData(self.time_recorded, self.arr_average)

            else:
                for i in range(1, panjang+1):
                    if self.graph_type == 'Sensor %d'%i:
                        self.curves["curve%d"%i].setData(self.time_recorded,self.arr_sensors["arr_sensor%d"%i])
        except:
            print("error")
    def array_sensor(self): # memudahkan memanggil array sensor  database
        return self.arr_sensors,self.arr_average
        
  
