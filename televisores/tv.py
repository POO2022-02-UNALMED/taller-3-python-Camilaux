from televisores.marca import Marca
from televisores.control import Control

class TV:
    __numTV = 0

    def __init__(self,marca,estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.__numTV += 1

    def setMarca(self,marca):
        self._marca = marca
    
    def getMarca(self):
        return self._marca
    
    def setControl(self,control):
        self._control = control

    def getControl(self):
        return self._control

    def setPrecio(self,precio):
        self._precio = precio
    
    def getPrecio(self):
        return self._precio

    def setVolumen(self,volumen):
        if self._estado == True and volumen >= 1 and volumen <= 7:
            self._volumen = volumen
    
    def getVolumen(self):
        return self._volumen

    def setCAnal(self,canal):
        if self._estado == True and canal >= 1 and canal >= 120:
            self._canal = canal

    def getCanal(self):
        return self._canal

    def turnOn(self):
        self._estado == True
    
    def turnOff(self):
        self._estado == False
    
    def getEstado(self):
        return self._estado

    @staticmethod
    def getNumTV():
        return TV.__numTV
    
    @staticmethod
    def setNumTV(cls,num):
        TV.__numTV = num

    def canalUp(self):
        if(self.getCanal() < 120 and self.getEstado() == True):
            self._canal += 1
        self.setCanal(self._canal)    
    
    def canalDown(self):
        if(self.getCanal() <= 120 and self.getEstado() == True):
            self._canal -= 1
        self.setCanal(self._canal)  

    def volumenUp(self):
        if(self.getVolumen() < 7 and self.getEstado() == True):
            self._volumen += 1
        self.setVolumen(self._volumen) 

    def volumenDown(self):
        if(self.getVolumen() <= 7 and self.getEstado() == True):
            self._volumen -= 1
        self.setVolumen(self._volumen)  
        