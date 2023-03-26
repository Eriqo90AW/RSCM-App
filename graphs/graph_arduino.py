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
import numpy.typing as nt

class GraphArduino:
    def __init__(self):
        self.time_recorded  = [] #sumbu X (menyimpan waktu berjalan)\
        self.banyak_sensor=9 # jumlah sensor 9 buah

        #---Inisiasi awal untuk sumbu Y-----
    
        self.arr_average= [] # rata-rata
        #arr_sensor1
        self.arr_sensors={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
         "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
         "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []}
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
        self.penavg = pg.mkPen(color='#eb34e1', width=2) #pink

        self.pens={"pen1": self.pen1, "pen2": self.pen2, "pen3": self.pen3, 
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
            for i in range(1, self.banyak_sensor+1):
                self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i],name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )
            #-----------------------------------
          
        elif self.graph_type == 'average':
            self.curve_avg  = self.plot_widget.plot(self.time_recorded,self.arr_average, name="average", pen=self.penavg)

        # bila hanya salah satu sensor saja yang ditampilkan  
        else:
            for i in range(1, self.banyak_sensor+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i], name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )
    
    # method to pause the graph
    def pauseGraph(self):
        # stop the timer to pause the graph
        self.timer.stop()

    # method to stop the graph
    def stopGraph(self):
        # clear the graph
        self.plot_widget.clear()
    
    def saveGraph(self):
        seluruh_sensor, average= self.arr_sensors,self.arr_average
        
       # for i in range(1,len(seluruh_sensor)+1):
           # seluruh_sensor["arr_sensor%d"%i] =np.asarray(seluruh_sensor["arr_sensor%d"%i])
        #average=np.asarray(average)
        date = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M %p")
        data = {'average': average}
        for i in range(1, len(seluruh_sensor)+1):
            data.update({'sensor%d'%i: seluruh_sensor["arr_sensor%d"%i] })

        path =  "%s.json"%date

        with open("%s"%path,"w") as f:
            json.dump(data, f)  
        with open("%s"%path, 'r') as f:
            data = json.load(f)
        print(data)

        #for i in range(1,len(seluruh_sensor)+1):
            #with open("%s"%path,"a") as f:
             #   json.dump(seluruh_sensor["arr_sensor%d"%i], f)

        # simpan seluruh sensor
            #with open("%s"%path,"a") as f:
                #np.savetxt(f, (seluruh_sensor["arr_sensor%d"%i], ), fmt="%d", delimiter=',', header="sensor%d: "%i) 

        # simpan average array
       # with open("%s"%path,"a") as f:
            #np.savetxt(f, (average, ), fmt="%d", delimiter=',', header="average: ") # simpan average array '''
            
    def readGraph(self):
       # data=saveGraph()
       # self.arr_sensors.update{sensor%d'%i: seluruh_sensor["arr_sensor%d"%i]}
        pass



    # function untuk update waktu terbaru
    def waktu_sinyal(self, waktu): 
        # argument "waktu" berasal dari self.worker.waktu.connect()
        self.current_time +=waktu # delay arduino dijadikan pergerakan grafik sumbu 
        #print("transfer detik:", waktu)
    def min_max(self):
        for i in range (1, self.banyak_sensor+1):
            a= np.max(self.arr_sensors["arr_sensor%d"%i])
            b= np.min(self.arr_sensors["arr_sensor%d"%i])
        return a,b

    # Funtion untuk update grafik tiap waktu  
    def graphUpdate(self, sinyal):
        # argument "sinyal" berasal dari self.worker.update_sinyal.connect()
        self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
        self.update_sensor(sinyal) #agar array sensor tetap ter-update

        # update the graph
        if self.graph_type  == 'main':
            for i in range(1, len(sinyal)+1):
                self.curve["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])

        elif self.graph_type == 'average':
            self.curve_avg.setData(self.time_recorded,self.arr_average)

        else:
            for i in range(1, len(sinyal)+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curve["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])

    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def update_sensor(self, sinyal):
        self.banyak_sensor  = len(sinyal)
        self.arr_average.append(round(np.average(sinyal)) ) #average dua digit desimal

        for i in range(len(sinyal)):
           self.arr_sensors["arr_sensor%d"%(i+1)].append(sinyal[i]) # update tiap sensor (maksimal 9 sensor)

    def array_sensor(self): # memudahkan memanggil array sensor  database
        return self.arr_sensors,self.arr_average
  


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

# Threading Class
class WorkerThread(QtCore.QThread):

    update_sinyal   =pyqtSignal(object) # mengirimkan self.array dari "emit()"
    waktu           =pyqtSignal(float) # mengirimkan delay dari "emit()"
    arduino_data    =serial_arduino() # berasal dari function yang mencari COM PORT

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
            
            self.array  = list(map(int, split_data)) # mengubah array tipe string ke array bilangangrafik_18_02.py
            #print("-----------------------------")
            self.update_sinyal.emit(self.array) #mengirimkan sinyal

            delay  = round(time.time()-c, 3) # selisih waktu
            self.waktu.emit(delay) 
            # ("thread detik:", delay)
    
