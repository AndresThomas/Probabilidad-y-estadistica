#import libraries PyQt5
#import the name of the file from designer 
import sys
import pandas as pd
from tkinter import Tk
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.uic.uiparser import QtWidgets
from matplotlib import pyplot



#Clase Main, donde se ejecuta la aplicacion Principal
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/menu.ui', self)
        self.data = pd.read_csv('data2.csv') #<-- leemos el archivo csv
        self.df = pd.DataFrame(self.data) #<-- creamos un dataframe
        #filt = self.df['toma combi'] == 'Sí'# <-- devuelve true en los datos donde la expresion evaluada cumple
        #self.dataFilteredYesTakeACombi = self.df[filt] # <- guardamos los elementos donde si toman combi
        #filt = self.df['toma combi'] == 'No'# <-- devuelve true en los datos donde la expresion evaluada cumple
        #self.dataFilteredNoTakeACombi = self.df[filt] # <- guardamos los elementos donde si toman combi
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

        #TABLEVIEW - Datos Discretos
        self.tableView_Discretos.setColumnWidth(0,120) #Columna 1
        self.tableView_Discretos.setColumnWidth(1,170) #Columna 2
        self.tableView_Discretos.setColumnWidth(2,170) #Columna 3
        self.tableView_Discretos.setColumnWidth(3,150) #Columna 4
        self.tableView_Discretos.setColumnWidth(4,150) #Columna 5
        self.tableView_Discretos.setColumnWidth(5,150) #Columna 6
        self.tableView_Discretos.setColumnWidth(6,209) #Columna 7

        #TableVIEW - Datos Continuos
        #TABLEVIEW - Datos Discretos
        self.tableView_Continuos.setColumnWidth(0,120) #Columna 1
        self.tableView_Continuos.setColumnWidth(1,170) #Columna 2
        self.tableView_Continuos.setColumnWidth(2,170) #Columna 3
        self.tableView_Continuos.setColumnWidth(3,150) #Columna 4
        self.tableView_Continuos.setColumnWidth(4,150) #Columna 5
        self.tableView_Continuos.setColumnWidth(5,150) #Columna 6
        self.tableView_Continuos.setColumnWidth(6,209) #Columna 7

        

#------------------------ LLENAR DATOS EN LA TABLA ------------------------
    def loadData(self):
        clase = [{"clase": 1},{"clase": 2}, {"clase": 3}, {"clase": 4}, {"clase": 5}, {"clase": 6}, {"clase": 7}, {"clase": 8}, {"clase": 9}, {"clase": 10}]
        row = 0
        self.tableView_Discretos.setRowCount(len(clase))
        for cl in clase:
            self.tableView_Discretos.setItem(row, 0, QtWidgets.QTableWidgetItem(cl["clase"]))
            row = row + 1

#------------------------ GRAFICAS -----------------------------------------
    def printBarras(self):
        money = self.dataFilteredYesTakeACombi['N de combis'] #<-- Guarda los montos registrados
        pyplot.title('Grafica de barras')
        dict ={1:0}
        for m in money:
            dict.update({m:1})#<--- se llena el diccionario
        #items = dict.keys() #<- se obtiene las llaves del diccionario
        #for item in items:
            #count = 0       #se hace un conteo
            #for m in money: # para ver cuantas veces se repite (frecuencia abs)
                #if(item == m):#la cantidad contenida en item
                    #count+=1
            #dict.update({item:count})#<- se actualiza el diccionario
        #print(dict) # todo ok
        #dict.pop(1) # eliminamos el dato basura
        #print(dict.keys()) # eje X
        #print(dict.values()) # eje Y
        #pyplot.bar(dict.keys(),dict.values())
        pyplot.xlabel("Numero de transportes abordados")
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


##sintaxis del main
if __name__ == '__main__':
    screen = Tk()
    app = QApplication(sys.argv)
    window = Main()
    window.resize(screen.winfo_screenwidth(),screen.winfo_screenheight()) # <-- se ajusta al tamaño de la pantalla
    window.setWindowTitle("Uso del Transporte") #<--- colocar nombre a la aplicacion
    window.setWindowIcon(QIcon('./Resources/icon.png')) #<--- colocar icono para la aplicacion
    screen =''
    window.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
