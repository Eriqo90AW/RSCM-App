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
        self.lines_avg = np.array([]) # rata-rata
        #-------------------------------------
        
        self.current_time  = 0 # pegerakan awal sumbu X ( Waktu akan di increment pada "def waktu_sinyal()"" ) 
        self.duration      = round(1000) #1000 milisekon/frame per second
        #self.step         = 1 #0.0174533 # 1 derajat = 0.0174533 radian

        # Create a widget to hold the plot
        self.plot_widget = pg.PlotWidget()

        # Set the title and labels for the plot
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle(" ", color="#F59100", size="2pt")
        self.styles = {"color": "#F59100", "font-size": "10px"}
        self.plot_widget.setLabel("left", "Range (cm)", **self.styles)
        self.plot_widget.setLabel("bottom", "Seconds (s)", **self.styles)

        # Set the y range of the plot
        self.plot_widget.setYRange(0, 550, padding=0)

        # Show the grid lines
        self.plot_widget.showGrid(x=True, y=True)

        # create a pen of different colors to use for the graph
        self.pen1   = pg.mkPen(color='k', width=2) #black
        self.pen2   = pg.mkPen(color='b', width=2) #blue
        self.pen3   = pg.mkPen(color='r', width=2) #red
        self.pen4   = pg.mkPen(color='y', width=2) #yellow
        self.pen5   = pg.mkPen(color='g', width=2) #green
        self.pen6   = pg.mkPen(color='#34ebe8', width=2) #cyan
        self.penavg = pg.mkPen(color='#eb34e1', width=4) #pink

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
            self.curve1     = self.plot_widget.plot(self.time_recorded, self.lines_1, pen=self.pen1)
            self.curve2     = self.plot_widget.plot(self.time_recorded, self.lines_2, pen=self.pen2)
            self.curve3     = self.plot_widget.plot(self.time_recorded, self.lines_3, pen=self.pen3)
            self.curve4     = self.plot_widget.plot(self.time_recorded, self.lines_4, pen=self.pen4)
            self.curve5     = self.plot_widget.plot(self.time_recorded, self.lines_5, pen=self.pen5)
            self.curve6     = self.plot_widget.plot(self.time_recorded, self.lines_6, pen=self.pen6)
        elif self.graph_type == 'average':
            self.curve_avg  = self.plot_widget.plot(self.time_recorded, self.lines_avg, pen=self.penavg)
        
        # start the timer to update the graph
        #self.timer.start()
        #self.timer.setInterval(self.duration)
    
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

    #@pyqtSlot(object)

    # Funtion untuk update grafik tiap waktu  
    def graphUpdate(self, sinyal):
        # argument "sinyal" berasal dari self.worker.update_sinyal.connect()
        self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
        
        # dari dictionary sensor 
        cache           =self.dic_sensor(sinyal) 
        self.lines_1    =cache["sensor1"]
        self.lines_2    =cache["sensor2"]
        self.lines_3    =cache["sensor3"]
        self.lines_4    =cache["sensor4"]
        self.lines_5    =cache["sensor5"]
        self.lines_6    =cache["sensor6"]
        self.lines_avg  =cache["sensoravg"]

        # update the graph
        if self.graph_type == 'main':
            self.curve1.setData(self.time_recorded, self.lines_1)
            self.curve2.setData(self.time_recorded, self.lines_2)
            self.curve3.setData(self.time_recorded, self.lines_3)
            self.curve4.setData(self.time_recorded, self.lines_4)
            self.curve5.setData(self.time_recorded, self.lines_5)
            self.curve6.setData(self.time_recorded, self.lines_6)
        elif self.graph_type == 'average':
            self.curve_avg.setData(self.time_recorded, self.lines_avg)


    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def dic_sensor(self, sinyal):
        # total ada 9 sensor seharusnya
        sensor1     =np.append(self.lines_1, sinyal[0])
        sensor2     =np.append(self.lines_2, sinyal[1])
        sensor3     =np.append(self.lines_3, sinyal[2]) 
        sensor4     =np.append(self.lines_4, sinyal[3]) 
        sensor5     =np.append(self.lines_5, sinyal[4]) 
        sensor6     =np.append(self.lines_6, sinyal[5])
        sensoravg   =np.append(self.lines_avg, round(np.average(sinyal[:]), 2) ) #average dua digit desimal
        
        print("transfer sensor:",sinyal[:])
        
        cache={ "sensor1": sensor1, 
                "sensor2": sensor2,
                "sensor3": sensor3, 
                "sensor4": sensor4,
                "sensor5": sensor5,
                "sensor6": sensor6,
                "sensoravg": sensoravg  }    

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
            c     = time.time( )# waktu sebelum mulai
            data_paket  = self.arduino_data.readline() # membaca output arduino
            #b' = bytes ;\r\n =newline berasal dari println

            data_paket  = data_paket.decode("utf-8").strip('\r\n')  # agar menghilangkan dummy simbol
            data_paket  = data_paket.replace("Out of range", '500') # out of range diganti dengan 500
            data_paket  = data_paket.replace("8191", '500') 
            split_data  = data_paket.split(" ") # pemisah antar bilangan dengan spasi
            
            self.array  = list(map(int, split_data)) # mengubah array tipe string ke array bilangan
            print("-----------------------------")
            print("thread sensor:",self.array)
            self.update_sinyal.emit(self.array) #mengirimkan sinyal

            d      = time.time() # waktu sesudah membaca arduino
            delay  = d-c # selisih waktu
            self.waktu.emit(delay) 
            print("thread detik:", delay)
    
