#from re import I
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pyqtgraph as pg
import numpy as np
import sys
import serial
import serial.tools.list_ports
import time
import pyrebase
import random

#import custom class for plotting graph
from plot_graph import PlotGraph

# GUI
from ui_app import Ui_MainWindow

# IMPORT GUI FUNCTIONS
import ui_function

#Using serial tools
def serial_ports():
    ports = serial.tools.list_ports.comports()

    connected = []
    for port in ports:
            connected.append(port.name)
    print("Connected COM ports: " + connected[0])
    return connected

def connect_port(port):
    '''
    Connect to the port
    '''
    serialPort = serial.Serial(port = port, baudrate=115200, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
    return serialPort

# Button Events
def initButton(self):
  #self.btn_tracker.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
  self.btn_tracker.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
  self.btn_database.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
  self.btn_startGraph.clicked.connect(self.startThread)
  #self.btn_stopGraph.clicked.connect(self.pauseGraph)
  self.btn_login_register.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
  self.btn_register_register.clicked.connect(lambda: self.register())
  self.btn_login_login.clicked.connect(lambda: self.login())
  self.edit_register_nama.textEdited.connect(self.registerNama)
  self.edit_register_umur.textEdited.connect(self.registerUmur)
  self.edit_login_id.textEdited.connect(self.loginID)
  self.combox_register_gender.currentIndexChanged[str].connect(self.registerGender)
  
  # TOGGLE SIDEBAR
  self.btn_toggle.clicked.connect(lambda: ui_function.UIFunctions.toggleMenu(self, 250, True)) 

# Draw the graph
def initGraph(self):
    # GUI Configuration
    self.widget_graph.setBackground('w')
    self.widget_graph.setTitle("Main Graph", color="#F59100", size="13pt")
    #00F794
    
    styles = {"color": "#F59100", "font-size": "10px"}
    self.widget_graph.setLabel("left", "Range (mm)", **styles)
    self.widget_graph.setLabel("bottom", "Seconds (s)", **styles)
    pen = pg.mkPen(color='k', width=2)
    pen1 = pg.mkPen(color='r', width=2)
    pen2 = pg.mkPen(color='g', width=2)
    pen3 = pg.mkPen(color='b', width=2)

    # SET DATA
    self.curve = self.widget_graph.plot(pen=pen)
    self.curve1 = self.widget_graph.plot(pen=pen1)
    self.curve2 = self.widget_graph.plot(pen=pen2)
    self.curve3 = self.widget_graph.plot(pen=pen3)
    self.curve4 = self.widget_graph.plot(pen=pen3)
    self.curve5 = self.widget_graph.plot(pen=pen3)
    self.curve6 = self.widget_graph.plot(pen=pen3)
    self.curve7 = self.widget_graph.plot(pen=pen3)
    self.curve8 = self.widget_graph.plot(pen=pen3)
    self.curve9 = self.widget_graph.plot(pen=pen3)


    self.widget_graph.setYRange(0, 1500, padding=0)
    self.widget_graph.showGrid(x=True, y=True)


class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, obj=None, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    # Patient Variables
    self.createPatientName = ""
    self.createPatientAge = 0
    self.createPatientId = "01"
    self.createPatientGender = "Male"

    self.loginPatientId = ""

    # Patient Variables
    self.currentPatient = {}

    self.setupUi(self)
    initButton(self)
    initGraph(self)

    self.stackedWidget.setCurrentIndex(0)

    self.range = 2500
    self.x = np.zeros(self.range)
    self.y = np.zeros(self.range)
    self.y1 = np.zeros(self.range)
    self.y2 = np.zeros(self.range)
    self.y3 = np.zeros(self.range)
    self.y4 = np.zeros(self.range)
    self.y5 = np.zeros(self.range)
    self.y6 = np.zeros(self.range)
    self.y7 = np.zeros(self.range)
    self.y8 = np.zeros(self.range)
    self.y9 = np.zeros(self.range)

    self.index = 0
    self.pause = 2

    # #update graph every 1000 miliseconds
    # timer = QtCore.QTimer()
    # timer.timeout.connect(self.graphUpdate)
    # timer.start(1000)

    # #array to hold random numbers
    # self.array_x = []
    # self.array_y = []

    # Firebase 
    # self.firebase = firebase.FirebaseApplication('https://pythonrscm-default-rtdb.firebaseio.com/', None)  
    firebaseConfig =  {
        "apiKey": "AIzaSyCU_voEKdNpWbqxR8xJJLbEcVqkMIR6TBY",
        "authDomain": "pythonrscm.firebaseapp.com",
        "databaseURL": "https://pythonrscm-default-rtdb.firebaseio.com",
        "projectId": "pythonrscm",
        "storageBucket": "pythonrscm.appspot.com",
        "messagingSenderId": "613770294252",
        "appId": "1:613770294252:web:04696f4426ed13eab386c9",
        "measurementId": "G-JFQ69FT00H"
    }

    try:
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.db=firebase.database()
    except:
        print('Error', 'Error connecting to database. Please connect to internet')

  # Start the thread
  def startThread(self):
    if(self.pause == 2):
      self.worker = WorkerThread()
      self.worker.start()
      print("thread started")
      self.worker.int_signal.connect(self.graphUpdate)
      self.pause = 0
      self.btn_startGraph.setText("Pause")
    elif(self.pause == 1):
      self.pause = 0
      self.btn_startGraph.setText("Pause")
    elif(self.pause == 0):
      self.pause = 1
      self.btn_startGraph.setText("Start")
      

  # Uodating the graph
  def graphUpdate(self, int_array):
    # if(self.index < 50):
    #   self.widget_graph.setXRange(0, self.index, padding=0)
    # elif(self.index < 250):
    #   self.widget_graph.setXRange(self.index-50, self.index, padding=0)
    # elif(self.index >= 250):
    #   self.widget_graph.setXRange(self.index-100, self.index, padding=0)
    # elif(self.index >= 300):
    #   self.widget_graph.setXRange(self.index-300, self.index, padding=0)

    # self.y[self.index] = calculate(self, int_array)
    # self.y1[self.index] = int_array[0]
    # self.y2[self.index] = int_array[1]
    # self.y3[self.index] = int_array[2]
    

    # if(self.pause == 0):
    #   if(self.index == self.range-1):
    #     self.index = 0
    #   else:
    #     self.index += 1

    #   self.curve.setData(self.y)
    #   self.curve1.setData(self.y1)
    #   self.curve2.setData(self.y2)
    #   self.curve3.setData(self.y3)
    # else:
    #   self.index = self.index

    print("updating graph")
    # x_values, y_values = self.get_new_data()

    # # Update the curve with the new data
    # self.curve.setData(x_values, y_values)

  # def get_new_data(self):
  #   random_x = 0.01
  #   random_y = random.randint(600, 1200)
  #   self.array_x.append(random_x)
  #   self.array_y.append(random_y)
  #   return self.array_x, self.array_y

  # Register new patient
  def register(self):
    if(self.createPatientId == '') or (self.createPatientName == "") or (self.createPatientAge == "") or (self.createPatientGender == ""):
        print('Error Input', 'Please fill all the box needed')
        return
    elif not (self.createPatientAge.isnumeric()):
        print('Error Input', 'Age must be a number')
        return
    try:
        id_patient = self.createPatientId
        patient = {  
                "id": self.createPatientId,
                "name": self.createPatientName,
                "age": int(self.createPatientAge),
                "gender": self.createPatientGender,
                "max": 0,
                "min": 0,
                "rate": 0
        }
        self.db.child(id_patient).set(patient)
        self.label_nama.setText(self.createPatientName)
        self.label_gender.setText(self.createPatientGender)
        self.label_umur.setText(self.createPatientAge + " Tahun")
        #self.label_min.setText("Min : 0")
        #self.label_rate.setText("Rate : 0")
        #self.label_max.setText("Max : 0")
        #self.currentPatient = patient
        self.stackedWidget.setCurrentIndex(1)
    except:
        print('Error', 'Error connecting to database')
        return
    print(self.createPatientName)
    print(self.createPatientAge)
    print(self.createPatientGender)

  # Login to existing account
  def login(self):
    if (self.loginPatientId ==""):
        print('Error Input', 'ID cannot be empty')
        return
    try:
        patient = self.db.child(self.loginPatientId).get()
        self.currentPatient = {   
                    "id": self.loginPatientId,
                    "name": patient.val()["name"],
                    "age": patient.val()["age"],
                    "gender": patient.val()["gender"],
                    "max": patient.val()["max"],
                    "min": patient.val()["min"],
                    "rate": patient.val()["rate"]
        }
        self.label_nama.setText(patient.val()["name"])
        self.label_gender.setText( patient.val()["gender"])
        self.label_umur.setText(str(patient.val()["age"]) + " Tahun")
        #self.label_min.setText("Min : " + str(patient.val()["min"]))
        #self.label_rate.setText("Rate : " + str(patient.val()["rate"]))
        #self.label_max.setText("Max : " + str(patient.val()["max"]))
        self.stackedWidget.setCurrentIndex(1)
    except:
        print('Error Input', 'False ID or Error connecting to Database')
        return

  def registerNama(self, s):
    self.createPatientName = s
  
  def registerUmur(self, s):
    self.createPatientAge = s

  def registerGender(self, s):
    self.createPatientGender = s

  def loginID(self, s):
    self.loginPatientId = s

# Threading Class
class WorkerThread(QtCore.QThread):
  int_signal = pyqtSignal(object)
  def __init__(self, parent = None):
      super(WorkerThread, self).__init__(parent)
      
  # Function which is executed by the thread (must be named 'run')    
  def run(self):
    # Reading data from serial port
    # serialPorts  = serial_ports()
    # currentPortName = serialPorts[0]
    # currentPort = connect_port(currentPortName)
    print("Thread started")

    # pen = pg.mkPen(color='k', width=2)
    # curve = self.widget_graph.plot(pen=pen)

    # myGraph = PlotGraph()
    # while(True):
    #   if currentPort.in_waiting:
    #     line = currentPort.readline()
    #     decoded = line.decode('utf').strip("\r\n")
        
    #     arr = decoded.split(',')
    #     arrInt = list(map(int, arr))
    #     self.int_signal.emit(arrInt)
    
# Fungsi nyoba-nyoba
# def calculate(self, all_data):
#     sum = 0
#     count = 0
#     for i in all_data:
#       sum += i
#       count+=1

#     avg = sum/count
#     return avg

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.setWindowTitle("Surface Gating")
  window.show()
  app.exec_()