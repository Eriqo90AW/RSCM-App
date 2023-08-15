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
from PyQt5.QtCore import QCoreApplication

class GraphArduino:
    def __init__(self, parent):
        self.parent = parent
        self.mode = "normal"
        self.testing = False
        self.counter = 0
        self.disconnected = False
        self.maxValue = 700
        self.targetScore = 300
        self.graph_type = "main"
        self.banyak_sensor=9 # jumlah sensor 9 buah
        self.time_recorded  = [] #sumbu X (menyimpan waktu berjalan)\

        #---Inisiasi awal untuk sumbu Y-----
        self.arr_target = [] # target
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
        self.plot_widget.setYRange(0, self.maxValue)

        self.plot_widget.keyPressEvent = self.handleKeyPressEvent

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

        self.pentarget = pg.mkPen(color='#a9a9a9', width=1, style=Qt.DashLine) #gray dotted

        self.pens={"pen1": self.pen1, "pen2": self.pen2, "pen3": self.pen3, 
        "pen4":self.pen4, "pen5": self.pen5, "pen6": self.pen6, 
        "pen7": self.pen7, "pen8": self.pen8, "pen9": self.pen9}

        #-------------------------------------------------------
        self.curve={} # nanti curve di append ke sini
        #-------------
        self.plot_widget.addLegend() # add legend to the graph
        self.plot_widget.getViewBox().setMouseEnabled(x=True, y=True) # enable zooming and panning
           
    
    # method untuk menginisialisasi grafik
    def initGraph(self):
        #dari class WorkerThread()
        self.worker=WorkerThread()
        if(self.worker.getArduinoData() == None):
            self.parent.first_time = True
        else:
            print("Initiated")
            self.worker.start()
            self.worker.update_sinyal.connect(self.graphUpdate) # dipassingkan dengan nama "sinyal"
            self.worker.waktu.connect(self.waktu_sinyal) # dipasingkan dengan nama "waktu"
            self.parent.first_time = False


    # method to start the graph
    def startGraph(self, graph_type):
        # to restart the graph after pausing
        if self.worker.running == False:
            self.worker.running = True
            self.worker.start()
            self.worker.update_sinyal.connect(self.graphUpdate)
            self.worker.waktu.connect(self.waktu_sinyal)
            self.disconnected = False

        self.graph_type = graph_type

        # plot target
        self.curve_target = self.plot_widget.plot(self.time_recorded,self.arr_target, name="Target", pen=self.pentarget)

        #curve
        if self.graph_type == 'main':
            for i in range(1, self.banyak_sensor+1):
                self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i],name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )
            #-----------------------------------
          
        elif self.graph_type == 'average':
            self.curve_avg  = self.plot_widget.plot(self.time_recorded,self.arr_average, name="Average", pen=self.penavg)

        # bila hanya salah satu sensor saja yang ditampilkan  
        else:
            for i in range(1, self.banyak_sensor+1):
                if self.graph_type == 'Sensor %d'%i:
                    self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i], name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )

    # method to clear the graph
    def clearGraph(self):
        self.plot_widget.clear()

    # method to pause the graph
    def pauseGraph(self, first_time):
        if first_time:
            pass
        else:
            self.worker.running = False

    # method to stop the graph
    def stopGraph(self, first_time):
        if first_time:
            pass
        else:
            # Set a flag to indicate that disconnection is happening
            self.disconnected = True
            # Disconnect the signals
            self.worker.update_sinyal.disconnect(self.graphUpdate)
            self.worker.waktu.disconnect(self.waktu_sinyal)

            self.worker.running = False
            self.plot_widget.clear()
            print("after disconnecting")
            # reset all the arrays
            self.time_recorded  = [] #sumbu X (menyimpan waktu berjalan)\
            self.arr_average= [] # rata-rata
            self.arr_sensors={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
            "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
            "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []} #array untuk menyimpan data sensor
            self.current_time  = 0 # pegerakan awal sumbu X ( Waktu akan di increment pada "def waktu_sinyal()"" ) 
            self.curve={} # nanti curve di append ke sini
            
    
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
        # print("transfer detik:", waktu)

    def max_min_avg(self, sensor_num=0):
        if not self.parent.isReset():
            if self.graph_type == 'main':
                for i in range (1, self.banyak_sensor+1):
                    max= np.max(self.arr_sensors["arr_sensor%d"%i])
                    min= np.min(self.arr_sensors["arr_sensor%d"%i])
                avg = round(np.average(self.arr_average))
                self.parent.statsUpdate(max, min, avg)
                return
            elif self.graph_type == 'average':
                max= np.max(self.arr_average)
                min= np.min(self.arr_average)
                avg = round(np.average(self.arr_average))
                self.parent.statsUpdate(max, min, avg)
                return
            else:
                for i in range(1, self.banyak_sensor+1):
                    if self.graph_type == 'Sensor %d'%i:
                        max= np.max(self.arr_sensors["arr_sensor%d"%i])
                        min= np.min(self.arr_sensors["arr_sensor%d"%i])
                        avg = round(np.average(self.arr_sensors["arr_sensor%d"%i]))
                        self.parent.statsUpdate(max, min, avg)
                        self.curve["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])
                        return

        else:
            self.parent.statsClear()

    # Funtion untuk update grafik tiap waktu  
    def graphUpdate(self, sinyal):
        if not self.disconnected:
            # argument "sinyal" berasal dari self.worker.update_sinyal.connect()
            self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
            self.update_sensor(sinyal) #agar array sensor tetap ter-update

            # update target
            self.curve_target.setData(self.time_recorded,self.arr_target)

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

            if self.mode == "normal":
                self.plot_widget.setXRange(0, self.time_recorded[-1])
            elif self.mode == "follow":
                self.plot_widget.setXRange(self.time_recorded[-1] - 5, self.time_recorded[-1] + 1)
            elif self.mode == "default":
                self.plot_widget.setXRange(self.time_recorded[-1] - 10, self.time_recorded[-1] + 4)
            self.max_min_avg() # agar stats label tetap ter-update

    # Function untuk menyimpan array "update_sinyal" dari Class WorkerThread
    def update_sensor(self, sinyal):
        self.banyak_sensor  = len(sinyal)
        self.arr_average.append(round(np.average(sinyal)) ) #average dua digit desimal
        self.arr_target.append(self.targetScore) # update target (maksimal 9 sensor

        for i in range(len(sinyal)):
           self.arr_sensors["arr_sensor%d"%(i+1)].append(sinyal[i]) # update tiap sensor (maksimal 9 sensor)

    def array_sensor(self): # memudahkan memanggil array sensor  database
        return self.arr_sensors,self.arr_average
    
    def changeMode(self):
        if self.mode == "normal":
            self.mode = "follow"
        elif self.mode == "follow":
            self.mode = "default"
        elif self.mode == "default":
            self.mode = "normal"

    def handleKeyPressEvent(self, ev):
        if ev.key() == pg.QtCore.Qt.Key_Space:
            self.changeMode()
        # elif ev.key() == pg.QtCore.Qt.Key_Plus and ev.modifiers() == pg.QtCore.Qt.ControlModifier:
        #     # Handle Ctrl + +: Zoom in
        #     self.plot_widget.plotItem.getViewBox().scaleBy((0.5, 1))
        # elif ev.key() == pg.QtCore.Qt.Key_Minus and ev.modifiers() == pg.QtCore.Qt.ControlModifier:
        #     # Handle Ctrl + -: Zoom out
        #     self.plot_widget.plotItem.getViewBox().scaleBy((2, 1))
  


# Mendeteksi COM port  Arduino secara otomatis
def serial_arduino():
    # Create a QMessageBox widget
    dialog = QMessageBox()

    # Set the text and title of the message box
    dialog.setWindowTitle("Searching...")
    dialog.setText(f"Mencari COM PORT...")

    # Set the icon and buttons of the message box
    dialog.setIcon(QMessageBox.Information)
    dialog.setStandardButtons(QMessageBox.NoButton)

    # Show the message box and wait for a response
    dialog.show()
    QCoreApplication.processEvents()

    # mencari COM port secara otomatis dengan percobaan sebanyak 5 kali
    for i in range(1):
        for coba_port in range(1, 11): #mencari COM port dari 0-10 (default
            try:
                data_serial =serial.Serial('com%d'%coba_port, 115200) 
                print("Tersambung pada COM PORT:", coba_port)
                break #  berhenti ketika ketemu nomor com port yang benar
            except:
                time.sleep(0.2)
                print("Mencari COM PORT...")
                continue #increment bila nomor com port tidak sesuai
        else:
            time.sleep(0.2)
            continue
        dialog.close
        break
    else:
        print("COM PORT tidak terdeteksi")
        dialog.close
        show_popup()
        return

    time.sleep(1) # untuk loading 1 second agar tidak error
    data_serial.flushInput() #default
    data_serial.setDTR(True) #default
    return data_serial # dipassingkan ke class WorkerThread

def show_popup():
    # Create a QMessageBox widget
    message_box = QMessageBox()

    # Set the text and title of the message box
    message_box.setText(f"COM PORT tidak terdeteksi")
    message_box.setWindowTitle("Error")

    # Set the icon and buttons of the message box
    message_box.setIcon(QMessageBox.Information)
    message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # Show the message box and wait for a response
    message_box.exec_()

# Threading Class
class WorkerThread(QtCore.QThread):

    update_sinyal   =pyqtSignal(object) # mengirimkan self.array dari "emit()"
    waktu           =pyqtSignal(float) # mengirimkan delay dari "emit()"
    # arduino_data    =serial_arduino() # berasal dari function yang mencari COM PORT

    def __init__(self):
        super().__init__()
        self.running = True
        # self.update_sinyal   =pyqtSignal(object) # mengirimkan self.array dari "emit()"
        # self.waktu           =pyqtSignal(float) # mengirimkan delay dari "emit()"
        self.arduino_data    =None
        try:
            self.arduino_data    =serial_arduino() # berasal dari function yang mencari COM PORT
            self.running = False
        except:
            self.arduino_data = None
            self.running = False

    def getArduinoData(self):
        return self.arduino_data
  # Function which is executed by the thread (must be named 'run')
    def run(self):
        print("Thread Started")
        # Reading data from serial port
        while self.running: # default
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
    
