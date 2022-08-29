from televisores.marca import Marca
from televisores.control import Control

class TV:
    __numTV = 0

    def __init__(self,marca,estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = None
        TV.__numTV += 1

    def setMarca(self,marca):
        if isinstance(marca, Marca):
            self.__marca = marca
    
    def getMarca(self):
        return self.__marca
    
    def setControl(self,control):
        if isinstance(control,Control):
            self.__control = control

    def getControl(self):
        return self.__control

    def setPrecio(self,precio):
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio

    def setVolumen(self,volumen):
        if self.__estado == True and volumen >= 1 and volumen <= 7:
            self.__volumen = volumen
    
    def getVolumen(self):
        return self.__volumen

    def setCAnal(self,canal):
        if self.__estado == True and canal >= 1 and canal >= 120:
            self.__canal = canal

    def getCanal(self):
        return self.__canal

    def turnOn(self):
        self.__estado == True
    
    def turnOff(self):
        self.__estado == False
    
    def getEstado(self):
        return self.__estado

    @staticmethod
    def getNumTV():
        return TV.__numTV
    
    @staticmethod
    def setNumTV(num):
        TV.__numTV = num

    def canalUp(self):
        if(self.getCanal() < 120 and self.getEstado() == True):
            self._canal += 1
        self.setCanal(self.__canal)    
    
    def canalDown(self):
        if(self.getCanal() <= 120 and self.getEstado() == True):
            self.__canal -= 1
        self.setCanal(self.__canal)  

    def volumenUp(self):
        if(self.getVolumen() < 7 and self.getEstado() == True):
            self.__volumen += 1
        self.setVolumen(self.__volumen) 

    def volumenDown(self):
        if(self.getVolumen() <= 7 and self.getEstado() == True):
            self.__volumen -= 1
        self.setVolumen(self.__volumen)  
        