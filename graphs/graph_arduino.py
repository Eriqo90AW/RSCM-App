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
import os

class GraphArduino:
    def __init__(self, parent):
        self.parent = parent
        self.mode = "normal"
        self.testing = False
        self.counter = 0
        self.disconnected = False
        self.max_value = 700
        self.target_score = 300
        self.load_mode = False
        self.worker = None
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
        self.plot_widget.setYRange(0, self.max_value)

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
        # create an instance of class WorkerThread
        self.worker = WorkerThread()

        if self.load_mode == True:
            self.worker.read_mode = "load"
        else:
            self.worker.read_mode = "arduino"
            arduino_data, read_mode = self.worker.getArduinoData() # get data from WorkerThread instance

            if(arduino_data == None and read_mode == "arduino"):  # if the COM port is not detected
                self.parent.first_time = True
                return
        
        print("Initiated")
        self.worker.start()
        self.worker.update_sinyal.connect(self.graphUpdate)
        self.worker.waktu.connect(self.waktu_sinyal)
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
    def pauseGraph(self):
        if self.parent.first_time:
            pass
        else:
            self.worker.running = False

    # method to stop the graph
    def stopGraph(self):
        if self.parent.first_time:
            return
        if self.worker.finish_load:
            self.load_mode = False

            # Reset start button to normal
            self.parent.is_loading = False
            self.parent.main_window.ui.button_graph_start.setText("Start")
            self.parent.paused = True

            self.worker.finish_load = False
            self.parent.first_time = True
            self.plot_widget.clear()
            self.arrayReset()
            # return

        if self.worker.running:
            # Set a flag to indicate that disconnection is happening
            self.disconnected = True
            # Disconnect the signals
            self.worker.update_sinyal.disconnect(self.graphUpdate)
            self.worker.waktu.disconnect(self.waktu_sinyal)

            self.worker.running = False
            self.plot_widget.clear()
            
            self.arrayReset()
            
    def arrayReset(self):
        # reset all the arrays
        self.time_recorded  = [] #sumbu X (menyimpan waktu berjalan)\
        self.arr_average= [] # rata-rata
        self.arr_target = [] # target
        self.arr_sensors={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
        "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
        "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []} #array untuk menyimpan data sensor
        self.current_time  = 0 # pegerakan awal sumbu X ( Waktu akan di increment pada "def waktu_sinyal()"" ) 
        self.curve={} # nanti curve di append ke sini

    def saveGraph(self):
        if len(self.arr_average) != 0:
            print("Saving Graph...")
            self.pauseGraph()
            self.parent.main_window.ui.button_graph_start.setText("Start")
            self.parent.paused = True # simulating pressing the pause button

            seluruh_sensor, average= self.arr_sensors,self.arr_average
            user = self.parent.user

            date = datetime.datetime.now().strftime("%H.%M_%d-%m-%Y")
            final_format = f"{user}_{date}"

            data = {'time_recorded': self.time_recorded}

            for i in range(1, len(seluruh_sensor)+1):
                data.update({'sensor%d'%i: seluruh_sensor["arr_sensor%d"%i] })

            # Construct the path to the "archive" folder
            archive_folder = os.path.join(os.path.dirname(__file__), "..", "archive")
            os.makedirs(archive_folder, exist_ok=True)  # Create the folder if it doesn't exist

            # Construct the full path for the JSON file inside the "archive" folder
            file_name = f"{final_format}.json"
            json_path = os.path.join(archive_folder, file_name)

            with open(json_path, "w") as f:
                json.dump(data, f, indent=4)
            
            show_popup("Saved Successfully", "Saving")

    
    def loadGraph(self):
        if self.worker != None:
            self.parent.stopButton()
        current_directory = os.path.join(os.path.dirname(__file__), "..", "archive")
        filenames, ignore=QFileDialog.getOpenFileNames(self.parent.main_window, 'Open file', current_directory)
        if filenames:
            # Create a QMessageBox widget
            dialog = QMessageBox()

            # Set the text and title of the message box
            dialog.setWindowTitle("Loading...")
            dialog.setText(f"Loading Data...")

            # Set the icon and buttons of the message box
            dialog.setIcon(QMessageBox.Information)
            dialog.setStandardButtons(QMessageBox.NoButton)

            # Show the message box and wait for a response
            dialog.show()
            QCoreApplication.processEvents()

            self.load_mode = True
            self.parent.is_loading = True
            if self.worker != None:
                self.worker.read_mode = "load"
                data = self.readGraph(*filenames)
                self.worker.setLoadedData(data)
                self.arrayReset()
                self.startGraph(self.parent.currentGraph)
            else:
                self.initGraph()
                self.startGraph(self.parent.currentGraph)
                data = self.readGraph(*filenames)
                self.worker.setLoadedData(data)
            self.parent.main_window.ui.button_graph_start.setText("Pause")
            self.parent.paused = False
            dialog.close()
        

    def readGraph(self, filename):
        with open(filename, "r") as f:
            json_string = f.read()

        # Parse the JSON string using json.loads()
        data = json.loads(json_string)
        return data
       

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
        self.arr_target.append(self.target_score) # update target (maksimal 9 sensor

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
    for i in range(1):######
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
        show_popup("COM PORT tidak terdeteksi", "Error")
        return

    time.sleep(1) # untuk loading 1 second agar tidak error
    data_serial.flushInput() #default
    data_serial.setDTR(True) #default
    return data_serial # dipassingkan ke class WorkerThread

def show_popup(message, title):
    # Create a QMessageBox widget
    message_box = QMessageBox()

    # Set the text and title of the message box
    message_box.setText(f"{message}")
    message_box.setWindowTitle(f"{title}")

    # Set the icon and buttons of the message box
    message_box.setIcon(QMessageBox.Information)
    message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # Show the message box and wait for a response
    message_box.exec_()

# Threading Class
class WorkerThread(QtCore.QThread):

    update_sinyal   =pyqtSignal(object) # mengirimkan self.array dari "emit()"
    waktu           =pyqtSignal(float) # mengirimkan delay dari "emit()"

    def __init__(self):
        super().__init__()
        self.running = False
        self.read_mode = "arduino"
        self.finish_load = False
        self.arduino_data = None
        self.loaded_data = None
        self.array = []
        self.banyak_sensor = 9

        # get data from arduino
        # self.getArduinoData()

    def getArduinoData(self):
        if self.read_mode == "arduino":
            try:
                self.arduino_data = serial_arduino() # berasal dari function yang mencari COM PORT
            except:
                self.arduino_data = None
        else:
            self.arduino_data = None
        return self.arduino_data, self.read_mode
    
    def setLoadedData(self, data):
        self.loaded_data = data

  # Function which is executed by the thread (must be named 'run')
    def run(self):
        print("Thread Started")
        # Reading data from serial port
        while self.running: # default
            if self.read_mode == "arduino":
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
            else:
                if self.loaded_data != None:
                    for time_index in range(len(self.loaded_data["time_recorded"])):
                        self.array = []
                        for no_sensor in range(1, self.banyak_sensor+1):
                            self.array.append(self.loaded_data[f"sensor{no_sensor}"][time_index])
                        self.update_sinyal.emit(self.array)
                        time.sleep(0.05)
                        if time_index == len(self.loaded_data["time_recorded"])-1:
                            self.waktu.emit(0)
                        else:
                            self.waktu.emit((self.loaded_data["time_recorded"][time_index + 1] - self.loaded_data["time_recorded"][time_index])/2)
                    self.finish_load = True
                    # self.update_sinyal.emit(self.array)
                    return
            

    
