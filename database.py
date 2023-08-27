import sqlite3
import numpy as np
from dataclasses import dataclass, field
import os
from datetime import datetime

@dataclass
class SensorData:
    # Amount of sensor data
    patientId:int   = 0
    amount:int      = 0 
    len:int         = 0
    max:int         = 0
    min:int         = 0
    time:np.ndarray = field(default_factory = lambda : np.array([]))
    data:dict       = field(default_factory = dict) 
    date:datetime   = field(default_factory = datetime.now)

    def changePatientId(self, patientId):
        self.patientId = patientId
    
    def setAmount(self, amount = None):
        if not(amount):
            self.amount = amount
        else:
            self.amount = len(self.data)

    def append(self, newData, time):
        self.time = np.append(self.time, time)
        if isinstance(newData, list) or isinstance(newData, np.ndarray):
            if -1 not in self.data:
                self.data[-1] = [np.mean(newData)]
            else:
                self.data[-1] = np.append(self.data[-1], np.mean(newData))
                
            for key, value in enumerate(newData):
                if key not in self.data:
                    self.data[key] = np.array(value).astype(np.float64)
                    self.amount += 1
                else:
                    self.data[key] = np.append(self.data[key], value)
            self.len += 1
        elif isinstance(newData, dict):
            matrix = [value for value in newData.values()]
            matrix = np.mean(matrix, axis=0)
            if -1 not in self.data:
                self.data[-1] = np.array(matrix).astype(np.float64)
            else:
                self.data[-1] = np.append(self.data[-1], matrix)

            for key, value in newData.items():
                if key not in self.data:
                    self.data[key] = np.array(value).astype(np.float64)
                    self.amount += 1
                else:
                    self.data[key] = np.append(self.data[key], value)
            self.len += len(newData.values()[0])
        else:
            exit("Error: Invalid data type")

    def updateMetaData(self):
        self.len    = len(self.data[-1])
        self.max    = max(self.data[-1])
        self.min    = min(self.data[-1])
        self.amount = max(self.data)

    def updateAverage(self):
        matrix = [value for value in self.data.values()]
        matrix = np.mean(matrix, axis=0)
        self.data[-1] = matrix.astype(np.float64) if isinstance(matrix, np.ndarray) \
                        else np.array(matrix).astype(np.float64)

    def _dataToBytes(self):
        for key, value in self.data.items():
            yield key, np.array(value).tobytes()
        yield "-2", np.array(self.time).tobytes()
    
    def dataToBytes(self):
        return dict(self._dataToBytes())

    def dataFromBytes(self, bytesData):
        self.data = {}
        for key, value in bytesData.items():
            if key == "-2":
                self.time = np.frombuffer(value, dtype=np.float64)
                continue
            if key not in self.data:
                self.data[key] = np.frombuffer(value, dtype=np.float64)
            else:
                self.data[key] = np.frombuffer(value, dtype=np.float64)
        self.setAmount()
        self.updateMetaData()
        self.updateAverage()

    def _getData(self, i=0, j=0):
        if i == 0 and j == 0:
            yield self.data
        elif i != 0 and j == 0:
            yield self.data[i]
        elif i == 0 and j != 0:
            for key, value in self.data.items():
                yield value[j]
        else:
            yield (self.data[i])[j]

    def getData(self, i=0, j=0):
        if i == 0 and j == 0:
            return list(self._getData(i,j))[0]
        else:
            buff = list(self._getData(i, j))
            return buff[0] if isinstance(buff[0], list) else buff
        
@dataclass
class Patient:
    id:int = 0
    name:str = ""
    age:int = 0
    gender:str = ""
    data:SensorData = field(default_factory = lambda : SensorData())

    def fromDict(self, data:dict):
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.gender = data["gender"]
        self.data.changePatientId(data["id"])

    def toDict(self) -> dict:
        return {"id": self.id, "name": self.name, "age": self.age, "gender": self.gender}

    def toList(self) -> list:
        return [self.id, self.name, self.age, self.gender]

    def toTuple(self) -> tuple:
        return (self.id, self.name, self.age, self.gender)


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, path:str = "data/patient.db"):
        # check if path is valid
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        self.path = path
        c = sqlite3.connect(self.path)
        self.createTable()
        self.con = None

    def query(func):
        def wrapper(self, *args, **kwargs):
            self.connect()
            res = func(self, *args, **kwargs)
            self.disconnect()
            return res
        return wrapper

    def connect(self):
        self.con = sqlite3.connect(self.path) 
        self.cur = self.con.cursor()
    
    def disconnect(self):
        self.cur.close()
        self.con.close()

    @query
    def createTable(self):
        q = """CREATE TABLE IF NOT EXISTS
            patient (
                id integer PRIMARY KEY UNIQUE,
                name text,
                age integer,
                gender text
            );
            """
        
            # data {
            #     dataid integer pk increments unique
            #     patientid integer *> patient.id
            #     date datetime
            # }
            # sensor {
            #     sensorid integer pk unique
            #     dataid integer *> data.dataid
            #     data blob
            # }
        self.cur.execute(q)

    @query
    def isPresent(self, data):
        if isinstance(data, Patient):
            data = data.id
        elif isinstance(data, dict):
            data = data["id"]
        q = "SELECT * FROM patient WHERE id = ?"
        self.cur.execute(q, (data,))
        return True if self.cur.fetchone() else False

    @query
    def addPatient(self, data):
        if isinstance(data, Patient):
            data = data.toList()
        elif isinstance(data, dict):
            data = list(data.values())
        q = "INSERT INTO patient VALUES (?,?,?,?)"
        self.cur.execute(q, data)
        self.con.commit()
        return self.cur.lastrowid

    @query
    def updatePatient(self, data):
        if isinstance(data, Patient):
            data = data.toList()
        elif isinstance(data, dict):
            data = list(data.values())
        q = "UPDATE patient SET name = ?, age = ?, gender = ? WHERE id = ?"
        self.cur.execute(q, (data[1:], data[0]))
        self.con.commit()

    @query
    def deletePatient(self, data):
        if isinstance(data, Patient):
            data = data.id
        elif isinstance(data, dict):
            data = data["id"]
        q = "DELETE FROM patient WHERE id = ?"
        self.cur.execute(q, (data,))
        self.con.commit()
        
    @query
    def deleteAllPatients(self):
        q = "DELETE FROM patient"
        self.cur.execute(q)
        self.con.commit()

    @query
    def getPatient(self, data):
        if isinstance(data, Patient):
            data = data.id
        elif isinstance(data, dict):
            data = data["id"]
        q = "SELECT * FROM patient WHERE id = ?"
        self.cur.execute(q, (data,))
        return self.cur.fetchone()
    
    @query
    def getAllPatients(self):
        q = "SELECT * FROM patient"
        self.cur.execute(q)
        return self.cur.fetchall()
    
    @query
    def getPatientsInRange(self, start, end):
        q = "SELECT * FROM patient WHERE id BETWEEN ? AND ?"
        self.cur.execute(q, (start, end))
        return self.cur.fetchall()
    
# db = Database()

# firstnames = ["John", "Jane", "Jack", "Jill", "James", "Jenny", "Jesse", "Jasmine", "Jasper", "Jade"]
# lastnames = ["Smith", "Doe", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez"]

# # for i in range(1, 50):
# #     name = firstnames[np.random.randint(0, len(firstnames))] + " " + lastnames[np.random.randint(0, len(lastnames))]
# #     age = np.random.randint(20, 60)
# #     db.addPatient(Patient(i, name, age, "not specified"))

# print(db.getAllPatients())