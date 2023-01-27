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


# main class 
class LineGraph:
    def __init__(self):
        self.time_recorded  = [] # koordinat sumbu x 
       
        # inisiasi awal untuk plot sumbu Y (total ada 9 harusnya)
        self.lines_1 = np.array([])
        self.lines_2 = np.array([])
        self.lines_3 = np.array([])
        self.lines_4 = np.array([])
        self.lines_5 = np.array([])
  
        self.current_time   = 0
        self.step           = 1
        self.duration       = 1000 
        self.lower_bound    = 0
        self.upper_bound    = 5

        # Create a widget to hold the plot
        self.plot_widget = pg.PlotWidget()

        # Set the title and labels for the plot
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("Main Graph", color="#F59100", size="13pt")
        self.styles = {"color": "#F59100", "font-size": "10px"}
        self.plot_widget.setLabel("left", "Range (mm)", **self.styles)
        self.plot_widget.setLabel("bottom", "Seconds (s)", **self.styles)

        # Set the y range of the plot
        self.plot_widget.setYRange(0, 200, padding=0)

        # Show the grid lines
        self.plot_widget.showGrid(x=True, y=True)

        # create a pen of different colors to use for the graph (total ada 9 harusnya)
        self.pen1   = pg.mkPen(color='k', width=2)
        self.pen2   = pg.mkPen(color='b', width=2)
        self.pen3   = pg.mkPen(color='r', width=2)
        self.pen4   = pg.mkPen(color='y', width=2)
        self.pen5   = pg.mkPen(color='g', width=2)

        #curve (total ada 9 harusnya)
        self.curve1     = self.plot_widget.plot(self.time_recorded, self.lines_1, pen=self.pen1)
        self.curve2     = self.plot_widget.plot(self.time_recorded, self.lines_2, pen=self.pen2)
        self.curve3     = self.plot_widget.plot(self.time_recorded, self.lines_3, pen=self.pen3)
        self.curve4     = self.plot_widget.plot(self.time_recorded, self.lines_4, pen=self.pen4)
        self.curve5     = self.plot_widget.plot(self.time_recorded, self.lines_5, pen=self.pen5)
        
        #dari class WorkerThread()
        self.worker=WorkerThread()
        self.worker.start()
        self.worker.update_sinyal.connect(self.graphUpdate) # dipasingkan dengan nama "sinyal"

        # update graph every 1 second
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.graphUpdate) 
        #self.timer.start()  
        self.timer.setInterval(self.duration)

    pyqtSlot(float)
    # Funtion untuk update grafik tiap waktu  
    def graphUpdate(self, sinyal):
        # argument "sinyal" berasal dari self.worker.update_sinyal

        a= time.time()# waktu sebelum plot
        self.time_recorded.append(self.current_time)
        self.current_time += self.step

        # dari dictionary 
        cache           =self.dic_sensor(sinyal) 
        self.lines_1    =cache["sensor1"]
        self.lines_2    =cache["sensor2"]
        self.lines_3    =cache["sensor3"]
        self.lines_4    =cache["sensor4"]
        self.lines_5    =cache["sensor5"]

        # update the graph (total ada 9 harusnya)
        self.curve1.setData(self.time_recorded, self.lines_1)
        self.curve2.setData(self.time_recorded, self.lines_2)
        #self.curve3.setData(self.time_recorded, self.lines_3)
        #self.curve4.setData(self.time_recorded, self.lines_4)
        #self.curve5.setData(self.time_recorded, self.lines_5)
        
        b= time.time() # waktu sesudah plot
        print("delay: "+str(1000*(b-a))+"ms") # hitung delay tiap update plot

    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def dic_sensor(self, sinyal):
        # total ada 9 sensor seharusnya
        sensor1 =np.append(self.lines_1, sinyal[0])
        sensor2 =np.append(self.lines_2, sinyal[1])
        sensor3 =np.append(self.lines_3, 2) # belum selesai
        sensor4 =np.append(self.lines_4, 3) # belum selesai
        sensor5 =np.append(self.lines_5, 4) # belum selesai
        
        cache={ "sensor1": sensor1, 
                "sensor2": sensor2,
                "sensor3": sensor3, 
                "sensor4": sensor4,
                "sensor5": sensor5 }    
        
        print(str(cache["sensor1"]))
        return cache # dipasssingkan ke function graphUpdate
    

# Threading Class
class WorkerThread(QtCore.QThread):
    update_sinyal = pyqtSignal(object) # mengirimkan array dari "emit()"
    arduino_data=serial_arduino() # berasal dari functio untuk mencari COM PORT

  # Function which is executed by the thread (must be named 'run')
    def run(self):
        print("thread started")
        # Reading data from serial port
        while True: # default
          if self.arduino_data.inWaiting: # default
            data_paket=self.arduino_data.readline() # membaca output arduino
            #b' = bytes ;\r\n =newline berasal dari println
            data_paket= data_paket.decode("utf-8").strip('\r\n')  # agar menghilangkan dummy simbol
            data_paket =data_paket.replace("Out of range", '8191') # out of range diganti dengan 8191
            split_data= data_paket.split(" ") # pemisah antar bilangan dengan spasi
            self.array=list(map(int, split_data)) # mengubah array tipe string ke array bilangan
            print("array:",self.array)
            self.update_sinyal.emit(self.array) #mengirimkan sinyal
