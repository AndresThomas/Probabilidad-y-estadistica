#import libraries PyQt5
#import the name of the file from designer 
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from matplotlib import pyplot
import pandas as pd

""" esta clase es la GUI generica para instanciar
las diferentes maneras de mostrar los datos """
class WindowGraphics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/grafica.ui', self)
        self.btnVolver.clicked.connect(self.close)
    def barras(x,takenCombi,noTakenCombi):
        money = takenCombi['dinero invertido'] #<-- Guarda los montos registrados
        pyplot.title('Grafica de barras')
        pyplot.ylabel(money)
        
    def histograma(x,takenCombi,noTakenCombi):
        print(takenCombi['N de combis'])
        """
        hay que hacer algo con los rangos, ya que estamos trabajando con numeros
        por lo que: ----> 3 a 4  <---- no es un numero
        """
    def ojiva(x,takenCombi,noTakenCombi):
        print('ojiva')
    def poligono(x,data):
        print('poligono')
    def pastel(x,takenCombi,noTakenCombi):
        print('pastel')


#Clase Main, donde se ejecuta la aplicacion Principal
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/menu.ui', self)
        self.data = pd.read_csv('data.csv') #<-- leemos el archivo csv
        self.df = pd.DataFrame(self.data) #<-- creamos un dataframe
        filt = self.df['toma combi'] == 'Sí'# <-- devuelve true en los datos donde la expresion evaluada cumple
        self.dataFilteredYesTakeACombi = self.df[filt] # <- guardamos los elementos donde si toman combi
        filt = self.df['toma combi'] == 'No'# <-- devuelve true en los datos donde la expresion evaluada cumple
        self.dataFilteredNoTakeACombi = self.df[filt] # <- guardamos los elementos donde si toman combi
        
        
        #BOTONES QUE HAY EN EL MENU PRINCIPAL
        self.btnBarras.clicked.connect(self.printBarras)
        self.btnHistograma.clicked.connect(self.printHistograma)
        self.btnOjiva.clicked.connect(self.printOjiva)
        self.btnPastel.clicked.connect(self.printPastel)
        self.btnPoligono.clicked.connect(self.printPoligono)
        self.btnExit.clicked.connect(self.close) #<--- cerrar la aplicación

    def printBarras(self):
        b = WindowGraphics()
        b.barras(self.dataFilteredYesTakeACombi,self.dataFilteredNoTakeACombi)
        self.demo = b
        self.demo.show()
    def printHistograma(self):
        w = WindowGraphics()
        w.histograma(self.dataFilteredYesTakeACombi,self.dataFilteredNoTakeACombi)
        self.demo = w
        self.demo.show()
    def printOjiva(self):
        print("abriendo ojiva")
        o = WindowGraphics()
        o.ojiva(self.dataFilteredYesTakeACombi,self.dataFilteredNoTakeACombi)
        self.demo = o
        self.demo.show()
    def printPastel(self):
        print("abriendo pastel")
        p = WindowGraphics()
        p.pastel(self.dataFilteredYesTakeACombi,self.dataFilteredNoTakeACombi)
        self.demo = p
        self.demo.show()
    def printPoligono(self):
        print("abriendo poligono")
        pol = WindowGraphics()
        pol.poligono(self.dataFilteredYesTakeACombi,self.dataFilteredNoTakeACombi)
        self.demo = pol
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
