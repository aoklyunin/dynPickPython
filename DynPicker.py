# coding=utf-8
import serial
import time
from scanf import scanf

"""
    Класс для работы с датчиком DynPicker
"""
class DynPicker:
    """
        Конструктор
        comPort - адрес Ком-порта
        fr - битрейт(скорость)
        timeout - задержка
        auto_ajust - флаг, нужно ли выполнять калибровку
    """
    def __init__(self,comPort='/dev/ttyUSB0',fr=921600,timeout=0,auto_ajust=True):
        self.comPort = comPort
        self.fr = fr
        self.timeout = timeout
        self.ser = serial.Serial(self.comPort, self.fr, timeout=self.timeout)
        self.ajust(auto_ajust)
        self.offset = self.readForces(False)


    """
        Получение калибровочных коээфициентов с флагом, нужно ли их считывать из датчика
    """
    def ajust(self,auto_ajust):
        if auto_ajust:
            self.ser.write("p")
            time.sleep(0.1)
            reply = self.ser.read(100)
            self.calib = scanf("%f,%f,%f,%f,%f,%f",reply)
        else:
            self.calib = [1]*6

    """
        Cчитываем показания датчика
        flgZero определяет, нужно ли делать поправку на начальные значения
    """
    def readForces(self,flgZero = True):
        self.ser.write("R")
        time.sleep(0.1)
        line = self.ser.read(100)
        n = int(line[1])
        force = [int(line[i * 4 + 3:i * 4 + 7], 16)/self.calib[i] - 8192 for i in range(6)]
        if flgZero:
            return [force[i]-self.offset[i] for i in range(len(force))]
        else:
            return force