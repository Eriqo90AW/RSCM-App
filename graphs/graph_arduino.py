from PyQt5 import QtCore
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import pyqtgraph as pg
import serial.tools.list_ports
import serial
import numpy as np
import datetime
import time
import json
import os

class GraphArduino:
    def __init__(self, parent):
        self.parent = parent
        self.mode = "normal"
        self.counter = 0
        self.disconnected = False
        self.load_mode = False
        self.worker = None
        self.graph_type = "main"
        self.max_value = 700 # change this to change the max value of the y axis
        self.target_score = 300 # change this to change the target score
        self.banyak_sensor = 9 # change this to change the number of sensors

        self.time_recorded  = [] # initialize the array for the x axis (time)
        #---Inisiasi awal untuk sumbu Y-----
        self.arr_target = [] # target
        self.arr_average= [] # rata-rata
        self.arr_sensors={"arr_sensor1": [], "arr_sensor2": [], "arr_sensor3": [],
         "arr_sensor4": [], "arr_sensor5": [], "arr_sensor6":[], 
         "arr_sensor7": [],"arr_sensor8": [], "arr_sensor9": []}
        
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

        self.curve={} # nanti curve di append ke sini

        self.plot_widget.addLegend() # add legend to the graph
        self.plot_widget.getViewBox().setMouseEnabled(x=True, y=True) # enable zooming and panning
           
    
    # method to initialize the graph
    def initGraph(self):
        # create an instance of class WorkerThread
        self.worker = WorkerThread()

        # get data from loaded data
        if self.load_mode == True:
            self.worker.read_mode = "load"

        # get data from arduino
        else:
            self.worker.read_mode = "arduino"
            arduino_data, read_mode = self.worker.getArduinoData() # get data from WorkerThread instance

            if(arduino_data == None and read_mode == "arduino"):  # if the COM port is not detected
                self.parent.first_time = True
                self.worker = None
                return
        
        print("Initiated")
        self.worker.start()
        self.worker.update_sinyal.connect(self.graphUpdate)
        self.parent.first_time = False
        self.worker.is_paused = True

    # method to start the graph
    def startGraph(self, graph_type):
        if self.worker == None:
            self.initGraph()
            self.startGraph(graph_type)
            return
        if self.worker.finish_load:
            self.worker.read_mode = "arduino"
            if self.worker.arduino_data == None:  # if the COM port is not detected
                arduino_data, read_mode = self.worker.getArduinoData() # get data from WorkerThread instance
                if(arduino_data == None and read_mode == "arduino"):  # if the COM port is not detected
                    return

        # to resume the graph after pausing
        if self.worker.is_paused:
            self.worker.resume()
            self.disconnected = False

        self.graph_type = graph_type

        # plot target
        self.curve_target = self.plot_widget.plot(self.time_recorded,self.arr_target, name="Target", pen=self.pentarget)

        #curve
        if self.graph_type == 'main':
            for i in range(1, self.banyak_sensor+1):
                self.curve.update( {"curve%d"%i: self.plot_widget.plot(self.time_recorded, self.arr_sensors["arr_sensor%d"%i],name="Sensor %d"%i, pen=self.pens["pen%d"%i])} )
          
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
            self.worker.pause()

    # method to stop the graph
    def stopGraph(self):
        if self.parent.first_time:
            return
        if self.load_mode == True and self.worker.finish_load == False:
            self.parent.paused = False
            self.parent.reset = False
            self.parent.main_window.ui.button_graph_start.setText("Load can't be paused")
            self.parent.main_window.ui.button_graph_stop.setText("Reset After Loading")
            return

        if self.load_mode and self.worker.finish_load:
            self.load_mode = False

            # Reset start button to normal
            self.parent.is_loading = False
            self.parent.main_window.ui.button_graph_start.setText("Start")
            self.parent.main_window.ui.button_graph_stop.setText("Reset")
            self.parent.paused = True

            # Set a flag to indicate that disconnection is happening
            self.disconnected = True
            self.worker.pause()

        if self.worker != None and self.worker.is_paused == False:
            # Set a flag to indicate that disconnection is happening
            self.disconnected = True
            self.worker.pause()

        self.clearGraph()    
        self.arrayReset()
    
    # method to reset all the arrays
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

    # method to save the graph
    def saveGraph(self):
        if len(self.arr_average) != 0:
            print("Saving Graph...")

            seluruh_sensor = self.arr_sensors
            user = self.parent.user

            date = datetime.datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
            final_format = f"{user}_{date}"

            data = {'time_recorded': self.time_recorded}

            for i in range(1, self.banyak_sensor+1):
                data.update({f'sensor{i}': seluruh_sensor[f"arr_sensor{i}"] })

            # Construct the path to the "archive" folder
            archive_folder = os.path.join(os.path.dirname(__file__), "..", "archive")
            os.makedirs(archive_folder, exist_ok=True)  # Create the folder if it doesn't exist

            # Construct the full path for the JSON file inside the "archive" folder
            file_name = f"{final_format}.json"
            json_path = os.path.join(archive_folder, file_name)

            with open(json_path, "w") as f:
                json.dump(data, f, indent=4)
            
            show_popup("Saved Successfully", "Saving")

    # method to load the graph    
    def loadGraph(self):
        # prevent loading while loading
        if self.load_mode == True:
            return
        # flag to indicate it is not the first time loading
        if self.parent.first_time:
            self.parent.first_time = False
        # if there is a graph running, stop it
        if self.worker != None:
            self.parent.stopButton()
            self.parent.reset = False
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
            # case when the graph has been initialized
            if self.worker != None:
                self.worker.finish_load = False
                self.worker.read_mode = "load"
                data, time = self.readGraph(*filenames)
                self.worker.setLoadedData(data, time)
                self.arrayReset()
                self.startGraph(self.parent.currentGraph)
            # case when the graph has not been initialized
            else:
                self.initGraph()
                data, time = self.readGraph(*filenames)
                self.worker.setLoadedData(data, time)
                self.startGraph(self.parent.currentGraph)
            self.parent.main_window.ui.button_graph_start.setText("Pause")
            self.parent.paused = False
            dialog.close()
        
    # method to read the graph from a JSON file
    def readGraph(self, filename):
        data = None
        with open(filename, "r") as f:
            json_string = f.read()

        # Parse the JSON string using json.loads()
        data = json.loads(json_string)

        # initialize local variables
        banyak_sensor = 0
        sensor_array = []
        time_array = []

        # Find the number of sensors
        for key in data:
            if key != "time_recorded":
                banyak_sensor += 1

        # Parse data into sensor array and time array
        for time_index, _ in enumerate(data["time_recorded"]):
            temp = []
            for no_sensor in range(1, banyak_sensor+1):
                temp.append(data[f"sensor{no_sensor}"][time_index])
            if time_index == 0:
                time_array.append(0)
            else:
                time_array.append(data["time_recorded"][time_index] - data["time_recorded"][time_index - 1])
            sensor_array.append(temp)

        return sensor_array, time_array

    # method to calculate the max, min, and average of the graph
    def max_min_avg(self):
        if not self.parent.reset:
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

    # method to update all the arrays
    def update_sensor(self, sinyal):
        self.arr_average.append(round(np.average(sinyal)) ) #average dua digit desimal
        self.arr_target.append(self.target_score) # update target

        for i in range(1, self.banyak_sensor+1):
           self.arr_sensors[f"arr_sensor{i}"].append(sinyal[i-1]) # update tiap sensor

    # method to update the graph (looping)
    def graphUpdate(self, sinyal, delay):
        self.current_time += delay # delay arduino dijadikan pergerakan grafik sumbu
        if not self.disconnected:
            self.time_recorded.append(self.current_time) # menjadi array untuk sumbu X
            self.update_sensor(sinyal) #agar array sensor tetap ter-update

            # update target
            self.curve_target.setData(self.time_recorded,self.arr_target)

            # update the graph
            if self.graph_type  == 'main':
                for i in range(1, self.banyak_sensor+1):
                    self.curve["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])

            elif self.graph_type == 'average':
                self.curve_avg.setData(self.time_recorded,self.arr_average)

            else:
                for i in range(1, self.banyak_sensor+1):
                    if self.graph_type == 'Sensor %d'%i:
                        self.curve["curve%d"%i].setData(self.time_recorded, self.arr_sensors["arr_sensor%d"%i])

            if self.mode == "normal":
                self.plot_widget.setXRange(0, self.time_recorded[-1])
            elif self.mode == "follow":
                self.plot_widget.setXRange(self.time_recorded[-1] - 5, self.time_recorded[-1] + 1)
            elif self.mode == "default":
                self.plot_widget.setXRange(self.time_recorded[-1] - 10, self.time_recorded[-1] + 4)
            self.max_min_avg() # agar stats label tetap ter-update

    # method to change the mode of the graph
    def changeMode(self):
        if self.mode == "normal":
            self.mode = "follow"
        elif self.mode == "follow":
            self.mode = "default"
        elif self.mode == "default":
            self.mode = "normal"

    # method to handle key press event
    def handleKeyPressEvent(self, ev):
        if ev.key() == pg.QtCore.Qt.Key_Space:
            self.changeMode()


# function to find the COM port
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
        show_popup("COM PORT tidak terdeteksi", "Error")
        return

    time.sleep(1) # untuk loading 1 second agar tidak error
    data_serial.flushInput() #default
    data_serial.setDTR(True) #default
    return data_serial # dipassingkan ke class WorkerThread

# function to show a popup
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

    update_sinyal = pyqtSignal(object, float) # mengirimkan self.array dari "emit()"
    paused = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False
        self.read_mode = "arduino"
        self.finish_load = False
        self.arduino_data = None
        self.loaded_sensors = None
        self.loaded_time = None
        self.array = []
        self.banyak_sensor = 9
        self.mutex = QMutex()
        self.is_paused = False

    # method to get data from arduino
    def getArduinoData(self):
        if self.read_mode == "arduino":
            try:
                self.arduino_data = serial_arduino() # berasal dari function yang mencari COM PORT
            except:
                self.arduino_data = None
        else:
            self.arduino_data = None
        return self.arduino_data, self.read_mode
    
    # method to set the loaded data
    def setLoadedData(self, sensor_array, time_array):
        # save the data as an iterator
        self.loaded_sensors = iter(sensor_array)
        self.loaded_time = iter(time_array)

    # method which is executed by the thread (must be named 'run')
    def run(self):
        print("Thread Started")
        # Reading data from serial port
        while True: # default
            with QMutexLocker(self.mutex):
                while self.is_paused:
                    self.paused.emit()
                    self.mutex.unlock()
                    time.sleep(1)  # Sleep while paused
                    self.mutex.lock()

            if self.read_mode == "arduino":
                if self.arduino_data.inWaiting: # default
                    start = time.perf_counter()# waktu sebelum mulai
                    data_paket  = self.arduino_data.readline() # membaca output arduino

                    data_paket  = data_paket.decode("utf-8").strip('\r\n')  # agar menghilangkan dummy simbol
                    data_paket  = data_paket.replace("Out of range", '600') # out of range diganti dengan 500
                    data_paket  = data_paket.replace("8191", '600') 
                    split_data  = data_paket.split(" ") # pemisah antar bilangan dengan spasi
                    
                    self.array  = list(map(int, split_data)) # mengubah array tipe string ke array bilangangrafik_18_02.py
                    end  = time.perf_counter() # waktu setelah selesai
                    delay = end - start # delay
                    print(f"Delay: {delay}")
                    self.update_sinyal.emit(self.array, delay) #mengirimkan sinyal

            # Reading data from loaded file
            else:
                if self.loaded_time != None:
                    try:
                        cur_sensors = next(self.loaded_sensors)
                        cur_time = next(self.loaded_time)
                        print(f"Delay: {cur_time}")
                        time.sleep(cur_time) # sleep to simulate delay
                        self.update_sinyal.emit(cur_sensors, cur_time)
                    except StopIteration:
                        self.finish_load = True
                        self.loaded_time = None
                        self.pause()

    # method to pause the thread          
    def pause(self):
        with QMutexLocker(self.mutex):
            self.is_paused = True

    # method to resume the thread
    def resume(self):
        with QMutexLocker(self.mutex):
            self.is_paused = False
            