#import libraries PyQt5
#import the name of the file from designer 
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class Student:
    #clase estudiante
    def __init__(self,grade,takeABus,numOfBus,moneyEspend,distance,time,sex):
        self.grade = grade
        self.takeABus = takeABus
        self.numOfBus = numOfBus
        self.moneyEspend = moneyEspend
        self.distance = distance
        self.time = time
        self.sex = sex

""" esta clase es la GUI generica para instanciar
las diferentes maneras de mostrar los datos """
class WindowGraphics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('grafica.ui', self)
    """
    x no se que sea, tal vez es la referencia de self o el propio
    objeto, pero si se borra da error xd
    """
    
    """
    plantear que variables vamos a utlizar, instalar matploblib XD

    
    """

    def barras(x,data):
        print('creando barras',data)
    def histograma(x,data):
        print('histo')
    def ojiva(x,data):
        print('ojiva')
    def poligono(x,data):
        print('poligono')
    def pastel(x,data):
        print('pastel')

class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('init.ui', self)

        self.btnBarras.clicked.connect(self.printBarras)
        self.btnHistograma.clicked.connect(self.printHistograma)
        self.btnOjiva.clicked.connect(self.printOjiva)
        self.btnPastel.clicked.connect(self.printPastel)
        self.btnPoligono.clicked.connect(self.printPoligono)

    
    def printBarras(self):
        print("abriendo barras")
        w = WindowGraphics()
        w.barras('conjunto de datos en una variable')
        self.demo = w
        self.demo.show()
    def printHistograma(self):
        print("abriendo histograma")
        w = WindowGraphics()
        w.histograma('data')
        self.demo = WindowGraphics()
        self.demo.show()
    def printOjiva(self):
        print("abriendo ojiva")
        w = WindowGraphics()
        w.ojiva('conjunto de datos en una variable')
        self.demo = WindowGraphics()
        self.demo.show()
    def printPastel(self):
        print("abriendo pastel")
        w = WindowGraphics()
        w.pastel('conjunto de datos en una variable')
        self.demo = WindowGraphics()
        self.demo.show()
    def printPoligono(self):
        print("abriendo poligono")
        self.demo = WindowGraphics()
        self.demo.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
