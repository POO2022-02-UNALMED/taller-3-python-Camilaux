class Control:

    def __init__(self):
        self.__tv = None

    def enlazar(self,tele):
        self.__tv = tele
        tele.setControl(self)

    def turnOn(self):
        self.__tv.turnOn()

    def turnOff(self):
        self.__tv.turnOff()

    def canalUp(self):
        self.__tv.canalUp()

    def canalDown(self):
        self.__tv.canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()

    def volumneDown(self):
        self.__tv.volumenDown()

    def setCanal(self,canal):
        self.__tv.setCanal(canal)

    def setTv(self,tv):
        self.__tv = tv

    def getTv(self):
        return self.__tv


    