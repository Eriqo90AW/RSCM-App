import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore
import serial.tools.list_ports
import time
import serial
import sys
import numpy as np
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *

# Mendeteksi COM port  Arduino secara otomatis
def serial_arduino():
    coba_port=0 #dummy variabel untuk COM port
    while True : 
        try:
            data_serial =serial.Serial('com%d'%coba_port, 115200) 
            print("Tersambung pada COM PORT:", coba_port)
            break #  berhenti ketika ketemu nomor com port yang benar
        except:
            coba_port +=1 #increment bila nomor com port tidak sesuai

    time.sleep(1) # untuk loading 1 second agar tidak error
    data_serial.flushInput() #default
    data_serial.setDTR(True) #default
    return data_serial # dipassingkan ke class WorkerThread


class Graph():
    def __init__(self):
        self.time_recorded  = [] #sumbu X (menyimpan waktu berjalan)
        #---Inisiasi awal untuk sumbu Y-----
        self.lines_1   = np.array([])
        self.lines_2   = np.array([])
        self.lines_3   = np.array([])
        self.lines_4   = np.array([])
        self.lines_5   = np.array([])
        self.lines_6   = np.array([])
        self.lines_7   = np.array([])
        self.lines_8   = np.array([])
        self.lines_9   = np.array([])
        self.lines_avg = np.array([]) # rata-rata
        
        self.sensor={"sensor1": self.lines_1, "sensor2": self.lines_2, "sensor3": self.lines_3,
         "sensor4": self.lines_4, "sensor5": self.lines_5, "sensor6": self.lines_6, 
         "sensor7": self.lines_7,"sensor8": self.lines_8, "sensor9": self.lines_9}
        #------------------------------------------------------------------------
        
        self.current_time  = 0 # pegerakan awal sumbu X ( Waktu akan di increment pada "def waktu_sinyal()"" ) 
        self.duration      = round(1000) #1000 milisekon/frame per second

        # Create a widget to hold the plot
        self.plot_widget = pg.PlotWidget()

        # Set the title and labels for the plot
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle(" ", color="#F59100", size="2pt")
        self.styles = {"color": "#F59100", "font-size": "10px"}
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
        self.penavg   = pg.mkPen(color='#eb34e1', width=2) #pink

        self.pen={"pen1": self.pen1, "pen2": self.pen2, "pen3": self.pen3, 
        "pen4":self.pen4, "pen5": self.pen5, "pen6": self.pen6, 
        "pen7": self.pen7, "pen8": self.pen8, "pen9": self.pen9}

        #-------------------------------------------------------
        self.curve={} # nanti curve di append ke sini
        #-------------
        # add legend to the graph
        self.plot_widget.addLegend()

        #dari class WorkerThread()
        self.worker=WorkerThread()
        self.worker.start()
        self.worker.update_sinyal.connect(self.graphUpdate) # dipassingkan dengan nama "sinyal"
        self.worker.waktu.connect(self.waktu_sinyal) # dipasingkan dengan nama "waktu"

        # update graph every 1 second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.graphUpdate) 
        self.timer.start(self.duration)
    
    # method to start the graph
    def startGraph(self, graph_type):
        self.graph_type = graph_type
        #curve
        if self.graph_type == 'main':
            for i in range(1, 10):
                self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.sensor["sensor%d"%i],name="Sensor %d"%i, pen=self.pen["pen%d"%i])} )
            #-----------------------------------
          
        elif self.graph_type == 'average':
            self.curve_avg  = self.plot_widget.plot(self.time_recorded, self.lines_avg, name="Average", pen=self.penavg)

        # bila hanya salah satu sensor saja yang ditampilkan  
        else:
            for i in range(1, 10):
                if self.graph_type == 'Sensor %d'%i:
                    self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.sensor["sensor%d"%i], name="Sensor %d"%i, pen=self.pen["pen%d"%i])} )
    
    # method to pause the graph
    def pauseGraph(self):
        # stop the timer to pause the graph
        self.timer.stop()

    # method to stop the graph
    def stopGraph(self):
        # clear the graph
        self.plot_widget.clear()

    # function untuk update waktu terbaru
    def waktu_sinyal(self, waktu): 
        # argument "waktu" berasal dari self.worker.waktu.connect()
        self.current_time +=waktu # delay arduino dijadikan pergerakan grafik sumbu 
        print("transfer detik:", waktu)
    def nilai_max(self):
        a= np.max(self.sensor["sensor1"])
        print("nilai max:", a)

    # Funtion untuk update grafik tiap waktu  
    def graphUpdate(self, sinyal):
        # argument "sinyal" berasal dari self.worker.update_sinyal.connect()
        self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
        
        # dari dictionary sensor 
        cache           =self.dic_sensor(sinyal) 
        #for i in range(1, len(sinyal)+1):
            #self.sensor["sensor%d"%i]=cache["sensor%d" %i]

        #self.lines_avg  =cache["sensoravg"]

        # update the graph
        if self.graph_type  == 'main':
            for i in range(1, len(sinyal)+1):
                self.curve["curve%d"%i].setData(self.time_recorded, self.sensor["sensor%d"%i])

        elif self.graph_type == 'average':
            self.curve_avg.setData(self.time_recorded, self.lines_avg)

        else:
            for i in range(1, len(sinyal)+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curve["curve%d"%i].setData(self.time_recorded, self.sensor["sensor%d"%i])
                    #print(i)
        self.nilai_max()
    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def dic_sensor(self, sinyal):
        # total ada 9 sensor seharusnya
        cache ={}
        for i in range(len(sinyal)):
            cache.update({"sensor%d"%(i+1): np.append(self.sensor["sensor%d"%(i+1)] , sinyal[i])})
            self.sensor["sensor%d"%(i+1)]= np.append(self.sensor["sensor%d"%(i+1)] , sinyal[i])
        print(cache)

        #sensoravg   =np.append(self.lines_avg, round(np.average(sinyal[:]), 2) ) #average dua digit desimal
        #cache.update({"sensoravg": sensoravg} )
        self.lines_avg  =np.append(self.lines_avg, round(np.average(sinyal[:]), 2) ) #average dua digit desimal
        return cache # dipasssingkan ke function graphUpdate

 
        

# Threading Class
class WorkerThread(QtCore.QThread):

    update_sinyal = pyqtSignal(object) # mengirimkan self.array dari "emit()"
    waktu=pyqtSignal(float) # mengirimkan delay dari "emit()"
    arduino_data=serial_arduino() # berasal dari function yang mencari COM PORT

  # Function which is executed by the thread (must be named 'run')
    def run(self):
        print("thread started")
        # Reading data from serial port
        while True: # default
          if self.arduino_data.inWaiting: # default
            c     = time.time()# waktu sebelum mulai
            data_paket  = self.arduino_data.readline() # membaca output arduino
            #b' = bytes ;\r\n =newline berasal dari println

            data_paket  = data_paket.decode("utf-8").strip('\r\n')  # agar menghilangkan dummy simbol
            #data_paket  = data_paket.replace(":", '')
            data_paket  = data_paket.replace("Out of range", '600') # out of range diganti dengan 500
            data_paket  = data_paket.replace("8191", '600') 
            split_data  = data_paket.split(" ") # pemisah antar bilangan dengan spasi
            
            self.array  = list(map(int, split_data)) # mengubah array tipe string ke array bilangan
            #print("-----------------------------")
            #print("thread sensor:",self.array)
            self.update_sinyal.emit(self.array) #mengirimkan sinyal

            delay  = round(time.time()-c, 3) # selisih waktu
            self.waktu.emit(delay) 
            #print("thread detik:", delay)
    
