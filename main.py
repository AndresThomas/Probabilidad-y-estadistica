#import libraries PyQt5
#import the name of the file from designer 
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
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
        uic.loadUi('./Views/grafica.ui', self)

        self.btnVolver.clicked.connect(self.close)
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


#Clase Main, donde se ejecuta la aplicacion Principal
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/menu.ui', self)

        #BOTONES QUE HAY EN EL MENU PRINCIPAL
        self.btnBarras.clicked.connect(self.printBarras)
        self.btnHistograma.clicked.connect(self.printHistograma)
        self.btnOjiva.clicked.connect(self.printOjiva)
        self.btnPastel.clicked.connect(self.printPastel)
        self.btnPoligono.clicked.connect(self.printPoligono)
        self.btnExit.clicked.connect(self.close) #<--- cerrar la aplicación

    """
    Encontrar el modo de poder instanciar una sola ventana
    de los diferentes tipos, es decir una sola instancia de
    windowGraphics pero que se muestre el poligono
    """
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
    window = Main()
    window.setWindowTitle("Uso del Transporte") #<--- colocar nombre a la aplicacion
    window.setWindowIcon(QIcon('./Resources/icon.png')) #<--- colocar icono para la aplicacion
    window.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
