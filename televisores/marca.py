class Marca:

    def __init__(self,nombre,marca):
        self._nombre = nombre
        self.marca = marca
    
    def setNombre(self,nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
