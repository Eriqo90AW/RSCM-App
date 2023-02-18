import pyqtgraph as pg
import numpy as np
from PyQt5 import QtCore, QtGui
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
        self.lines[0]   = np.array([0])
        self.lines[1]   = np.array([])
        self.lines[2]   = np.array([])
        self.lines[3]   = np.array([])
        self.lines[4]   = np.array([])
        self.lines[5]   = np.array([])
        self.lines[6]   = np.array([])
        self.lines[7]   = np.array([])
        self.lines[8]   = np.array([])
        self.sensor=np.array([])
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
        self.pen[0]   = pg.mkPen(color='k', width=2) #black
        self.pen[1]   = pg.mkPen(color='b', width=2) #blue
        self.pen[2]   = pg.mkPen(color='r', width=2) #red
        self.pen[3]   = pg.mkPen(color='#eb8934', width=2) #orange
        self.pen[4]   = pg.mkPen(color='g', width=2) #green
        self.pen[5]   = pg.mkPen(color='#34ebe8', width=2) #cyan
        self.pen[6]   = pg.mkPen(color='#8f34eb', width=2) #ungu
        self.pen[7]   = pg.mkPen(color='#ebd234', width=2) #kuning
        self.pen[8]   = pg.mkPen(color='#baeb34', width=2) #lime
        self.penavg   = pg.mkPen(color='#eb34e1', width=2) #pink


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
            for i in range(9):
                self.curve[i] = self.plot_widget.plot(self.time_recorded, self.lines[i], pen=self.pen[i])
            #-----------------------------------
          
        elif self.graph_type == 'average':
            self.curve_avg  = self.plot_widget.plot(self.time_recorded, self.lines_avg, pen=self.penavg)
        else:
            for i in range(9):
                if self.graph_type[i] == 'Sensor %d'%i:
                    self.curve[i] = self.plot_widget.plot(self.time_recorded, self.lines[i], pen=self.pen[i])
        '''
        elif self.graph_type == 'Sensor 1':
            self.curve[0]     = self.plot_widget.plot(self.time_recorded, self.lines[0], pen=self.pen[0])
        elif self.graph_type == 'Sensor 2':
            self.curve[1]     = self.plot_widget.plot(self.time_recorded, self.lines[1], pen=self.pen[1])
        elif self.graph_type == 'Sensor 3':
            self.curve[2]     = self.plot_widget.plot(self.time_recorded, self.lines[2], pen=self.pen[2])
        elif self.graph_type == 'Sensor 4':
            self.curve[3]     = self.plot_widget.plot(self.time_recorded, self.lines[3], pen=self.pen[3])
        elif self.graph_type == 'Sensor ':
            self.curve[4]     = self.plot_widget.plot(self.time_recorded, self.lines[4], pen=self.pen[4])
        elif self.graph_type == 'Sensor 6':
            self.curve[5]     = self.plot_widget.plot(self.time_recorded, self.lines[5], pen=self.pen[5])
        elif self.graph_type == 'Sensor 7':
            self.curve[6]     = self.plot_widget.plot(self.time_recorded, self.lines[6], pen=self.pen[6])
        elif self.graph_type == 'Sensor 8':
            self.curve[7]     = self.plot_widget.plot(self.time_recorded, self.lines[7], pen=self.pen[7])
        elif self.graph_type == 'Sensor 9':
            self.curve[8]     = self.plot_widget.plot(self.time_recorded, self.lines[8], pen=self.pen[8])  '''
    
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
        for i in len(cache):
            self.lines[i]   =cache["sensor%d" %i]

        self.lines_avg  =cache["sensoravg"]

        # update the graph
        if self.graph_type  == 'main':
            for i in len(sinyal):
                self.curve[i].SetData(self.time_recorded, self.lines[i])
                ''''
            self.curve1.setData(self.time_recorded, self.lines_1)
            self.curve2.setData(self.time_recorded, self.lines_2)
            self.curve3.setData(self.time_recorded, self.lines_3)
            self.curve4.setData(self.time_recorded, self.lines_4)
            self.curve5.setData(self.time_recorded, self.lines_5)
            self.curve6.setData(self.time_recorded, self.lines_6)
            self.curve7.setData(self.time_recorded, self.lines_7)
            self.curve8.setData(self.time_recorded, self.lines_8)
            self.curve9.setData(self.time_recorded, self.lines_9)'''

        elif self.graph_type == 'average':
            self.curve_avg.setData(self.time_recorded, self.lines_avg)
        else:
            for i in range(9):
                if self.graph_type[i] == 'Sensor %d'%i:
                    self.curve[i] = self.plot_widget.plot(self.time_recorded, self.lines[i], pen=self.pen[i])
        '''' 
        elif self.graph_type == 'Sensor 1':
            self.curve1.setData(self.time_recorded, self.lines_1)
        elif self.graph_type == 'Sensor 2':
            self.curve2.setData(self.time_recorded, self.lines_2)
        elif self.graph_type == 'Sensor 3':
            self.curve3.setData(self.time_recorded, self.lines_3)
        elif self.graph_type == 'Sensor 4':
            self.curve4.setData(self.time_recorded, self.lines_4)
        elif self.graph_type == 'Sensor 5':
            self.curve5.setData(self.time_recorded, self.lines_5)
        elif self.graph_type == 'Sensor 6':
            self.curve6.setData(self.time_recorded, self.lines_6)
        elif self.graph_type == 'Sensor 7':
            self.curve7.setData(self.time_recorded, self.lines_7)
        elif self.graph_type == 'Sensor 8':
            self.curve8.setData(self.time_recorded, self.lines_8)
        elif self.graph_type == 'Sensor 9':
            self.curve9.setData(self.time_recorded, self.lines_9)'''


    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def dic_sensor(self, sinyal):
        # total ada 9 sensor seharusnya
        sensor1     =np.append(self.lines[1], sinyal[0])
        sensor2     =np.append(self.lines[2], sinyal[1])
        sensor3     =np.append(self.lines[3], sinyal[2]) 
        sensor4     =np.append(self.lines[4], sinyal[3]) 
        sensor5     =np.append(self.lines[5], sinyal[4]) 
        sensor6     =np.append(self.lines[6], sinyal[5])
        sensor7     =np.append(self.lines[7], sinyal[6])
        sensor8     =np.append(self.lines[8], sinyal[7])
        sensor9     =np.append(self.lines[9], sinyal[8])
        sensoravg   =np.append(self.lines_avg, round(np.average(sinyal[:]), 2) ) #average dua digit desimal
        ''''
        i=0

        for h in len(sinyal):
            self.sensor[h][i]   =np.append(self.lines[i], sinyal[0+i])
            i += 1
        
        sensoravg   =np.append(self.lines_avg, round(np.average(sinyal[:]), 2) ) #average dua digit desimal
        '''
        #print("transfer sensor:",sinyal[:])
        cache={ "sensor1": sensor1, 
                "sensor2": sensor2,
                "sensor3": sensor3, 
                "sensor4": sensor4,
                "sensor5": sensor5,
                "sensor6": sensor6,
                "sensor7": sensor7,
                "sensor8": sensor8,
                "sensor9": sensor9,
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
            c     = round(time.time(),3)# waktu sebelum mulai
            data_paket  = self.arduino_data.readline() # membaca output arduino
            #b' = bytes ;\r\n =newline berasal dari println

            data_paket  = data_paket.decode("utf-8").strip('\r\n')  # agar menghilangkan dummy simbol
            #data_paket  = data_paket.replace(":", '')
            data_paket  = data_paket.replace("Out of range", '600') # out of range diganti dengan 500
            data_paket  = data_paket.replace("8191", '600') 
            split_data  = data_paket.split(" ") # pemisah antar bilangan dengan spasi
            
            self.array  = list(map(int, split_data)) # mengubah array tipe string ke array bilangan
            print("-----------------------------")
            print("thread sensor:",self.array)
            self.update_sinyal.emit(self.array) #mengirimkan sinyal

            d      = round(time.time(), 3) # waktu sesudah membaca arduino
            delay  = round(d-c, 3) # selisih waktu
            self.waktu.emit(delay) 
            #print("thread detik:", delay)
    
