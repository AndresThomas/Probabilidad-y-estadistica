#import libraries PyQt5
#import the name of the file from designer 
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from matplotlib import pyplot
import pandas as pd

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
        IsAMen = self.df['Sexo'] == 'Hombre'
        self.menPoblation = self.df[IsAMen]
        IsAWomen = self.df['Sexo'] == 'Mujer'
        self.womenPoblation = self.df[IsAWomen]
        
        #BOTONES QUE HAY EN EL MENU PRINCIPAL
        self.btnBarras.clicked.connect(self.printBarras)
        self.btnHistograma.clicked.connect(self.printHistograma)
        self.btnOjiva.clicked.connect(self.printOjiva)
        self.btnPastel.clicked.connect(self.printPastel)
        self.btnPoligono.clicked.connect(self.printPoligono)
        self.btnExit.clicked.connect(self.close) #<--- cerrar la aplicación

    def printBarras(self):
        money = self.dataFilteredYesTakeACombi['dinero invertido'] #<-- Guarda los montos registrados
        pyplot.title('Grafica de barras')
        dict ={1:0}
        for m in money:
            dict.update({m:1})#<--- se llena el diccionario
        items = dict.keys() #<- se obtiene las llaves del diccionario
        for item in items:
            count = 0       #se hace un conteo
            for m in money: # para ver cuantas veces se repite (frecuencia abs)
                if(item == m):#la cantidad contenida en item
                    count+=1
            dict.update({item:count})#<- se actualiza el diccionario
        #print(dict) # todo ok
        dict.pop(1) # eliminamos el dato basura
        #print(dict.keys()) # eje X
        #print(dict.values()) # eje Y
        barras = pyplot.bar(dict.keys(),dict.values())
        pyplot.xlabel("Monto")
        pyplot.ylabel("Numero de estudiantes")
        pyplot.show()
        
    def printHistograma(self):
        pass
    def printOjiva(self):
        pass
    def printPastel(self):
        labels = ['Hombres','Mujeres']
        pyplot.pie([self.menPoblation.__len__(),self.womenPoblation.__len__()],labels=labels,autopct='%.2f %%')
        pyplot.show()
        
    def printPoligono(self):
        pass

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
