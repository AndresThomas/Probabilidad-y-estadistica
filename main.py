#import libraries PyQt5
#import the name of the file from designer 
import sys
import pandas as pd
from tkinter import Tk
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from matplotlib import pyplot
import math
from collections import Counter

import statistics as stats #<---- media aritmetica

#Leer archivo csv para hacer los calculos
df = pd.read_csv('file.csv', delimiter=',')
dicts = df.to_dict('records')

class DatosContinuos:
    def getNoDeClase(self):
        cantidadDatos = len(dicts)
        noDeClase = round(1 + 3.3*math.log10(cantidadDatos))      
        return noDeClase

    def getListaClases(self):
        noDeClases = self.getNoDeClase()
        x = 1
        indice = 0
        while indice < noDeClases:
            if indice == 0:
                clases = [x]
            else:
                clases.insert(indice, x)
            x+=1
            indice+=1
        return clases

    def getListaDatos(self):
        lista = []
        indice = 0
        for x in dicts:
            lista.insert(indice, x.get("distancia"))
            indice+=1
        lista.sort() #<--- ordenar lista de manera ascendente
        return lista

    def getRango(self):
        lista = self.getListaDatos()
        menor = min(lista)
        mayor = max(lista)
        rango = mayor - menor
        return rango

    def getAnchoDeClase(self):
        rango = self.getRango()
        noDeClase = self.getNoDeClase()
        anchoDeClase = rango / noDeClase
        return anchoDeClase

    def getLimites(self):
        inicial = min(self.getListaDatos())
        anchoDeClase = self.getAnchoDeClase()
        limites = []
        m = self.getNoDeClase() #<--- filas
        n = 2 #<----- columnas

        for f in range (m):
            limites.append([])
            for c in range (n):
                limites[f].append(0)

        for f in range(m):
            for c in range(n):
                if f == 0 and c == 0:
                    limites [f][c] = inicial         
                elif c == 0:
                    limites [f][c] = limites [f-1][c+1] 
                elif c > 0:
                    limites[f][c] = limites [f][c-1] + anchoDeClase

        return limites

    def getListaMarcaDeClase(self):
        limites = self.getLimites()
        listaMarcaClases = []
        m = len(limites)
        n = 2

        for f in range(m):
            for c in range (n):
                if c == 0:
                    suma = (limites[f][c] + limites[f][c+1]) / 2
                    listaMarcaClases.append(suma)  
        return listaMarcaClases

    def getListaFrecAbsoluta(self):
        datos = self.getListaDatos()
        limites = self.getLimites()
        m = len(limites)
        n = 2
        lim_inf = []
        lim_sup = []
        items = []
        listaFrecuenciaAbsoluta = []
        
        for f in range (m):
            for c in range (n):
                if c == 0:      
                    lim_inf.append(limites[f][c])
                    lim_sup.append(limites[f][c+1])

        for x in datos:
            if x <= lim_sup[0]:
                items.append(x)

        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[1] and x <= lim_sup[1]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[2] and x <= lim_sup[2]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[3] and x <= lim_sup[3]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[4] and x <= lim_sup[4]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[5] and x <= lim_sup[5]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[6] and x <= lim_sup[6]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        for x in datos:
            if x > lim_inf[7] and x <= lim_sup[7]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()
        
        for x in datos:
            if x > lim_inf[8] and x <= lim_sup[8]:
                items.append(x)
        listaFrecuenciaAbsoluta.append(len(items))
        items.clear()

        return listaFrecuenciaAbsoluta


    def getListaFrecRelativa(self):
        frecAbsoluta = self.getListaFrecAbsoluta()
        totalFrecAbsoluta = sum(self.getListaFrecAbsoluta())
        lista = []
        for x in frecAbsoluta:
            operacion = (x * 100) / totalFrecAbsoluta
            lista.append(round(operacion,2)) #<--- round se utiliza para redondear a 2 decimales

        return lista


    def getListaFrecAbsAcumulada(self):
        frecRelativa = self.getListaFrecRelativa()
        index = 0
        lista = []

        for x in frecRelativa:
            if index == 0:
                lista.append(round(x,2))
            else:
                aux = x + lista[index-1]
                lista.append(round(aux,2)) #<--- round se utiliza para redondear a 2 decimales
            index+=1
        return lista


#------------ Multiple Values - Tendenciales centrales y dispersion -------------------------------#
class TendenciaCentral_Continuo:
    def __init__(self):
        datos = DatosContinuos()
        datos = datos.getListaDatos()
        self.media_arimetica = round(stats.mean(datos),2) #<--- sacar la media aritmetica
        self.media_geometrica = round(stats.geometric_mean(datos),2) #<--- sacar la media geometrica
        self.mediana = round(stats.median(datos),2) #<--- sacar la mediana
        self.moda = round(stats.mode(datos),2) #<--- sacar la moda
        self.varianza = round(stats.variance(datos),2) #<--- sacar la varianza muestral
        self.desviacion = round(stats.stdev(datos),2) #<--- sacar la desviacion estandar

def tendenciaCentral():
    return TendenciaCentral_Continuo()


class TendenciaCentral_Discreto:
    def __init__(self):
        datos = DatosDiscretos()
        datos = datos.getListaDatos()
        self.media_arimetica = round(stats.mean(datos),2) #<--- sacar la media aritmetica
        self.mediana = round(stats.median(datos),2) #<--- sacar la mediana
        self.moda = round(stats.mode(datos),2) #<--- sacar la moda
        self.varianza = round(stats.variance(datos),2) #<--- sacar la varianza muestral
        self.desviacion = round(stats.stdev(datos),2) #<--- sacar la desviacion estandar

def tendenciaCentral_Discreto():
    return TendenciaCentral_Discreto()


class TendenciaCentral_DatosAgrupados:
    def __init__(self):
        datos = DatosAgrupados()
        total_FrecAbs = sum(datos.getListaFrecAbsoluta())
        totalFrec_Marca_Media = sum(datos.getListaFrecuencia_Marca_Media())
        self.media_arimetica = round(((1/total_FrecAbs)*totalFrec_Marca_Media),2) #<--- sacar la media aritmetica
        
        #MEDIANA
        cantidadClases = len(datos.getListaClases())
        cantidadClases = int(cantidadClases)
        mediana_ = 0

        if cantidadClases % 2 == 0:
            print("Cantidad de clases par")
            index_1 = int(cantidadClases/2)
            index_2 = int((cantidadClases/2) + 1)
            
            marca_1 = datos.getListaMarcaDeClase().__getitem__(index_1)
            marca_2 = datos.getListaMarcaDeClase().__getitem__(index_2)
            mediana_ =(marca_1 + marca_2)/2
        else:
            print("Cantidad de clases impar")
            clase =int((cantidadClases + 1)/2)
            mediana_ = datos.getListaMarcaDeClase().__getitem__(clase-1) #<--- se le resta -1 ya que toma el indice 5, en lugar del 4, porque va de 0 a 8
               
        self.mediana = round(mediana_,2) #<--- sacar la mediana de clases

        marcaDeClase = datos.getListaMarcaDeClase()
        self.moda = round(stats.mode(marcaDeClase),2) #<--- sacar la moda de clases
       
        totalFrec_Marca_Dispersion = sum(datos.getListaFrecuencia_Marca_Dispersion())
        media_arimetica_2 = pow(self.media_arimetica,2)
        operacion_varianza = ((totalFrec_Marca_Dispersion - (total_FrecAbs * media_arimetica_2))/(total_FrecAbs-1)) #<--- sacar la varianza muestral de datos agrupados
        self.varianza = round(operacion_varianza,2) #<--- sacar la varianza muestral de datos agrupados

        self.desviacion = round(math.sqrt(self.varianza),2) #<--- sacar la desviacion estandar de datos agrupados
    

def tendenciaCentral_DatosAgrupados():
    return TendenciaCentral_DatosAgrupados()

#-------------------------------- ---------------------#  
        
class DatosDiscretos:
    def getListaDatos(self):
        lista = []
        indice = 0
        for x in dicts:
            lista.insert(indice, x.get("N de combis"))
            indice+=1
        lista.sort() #<--- ordenar lista de manera ascendente
        return lista

    def getListaValores(self):
        datos = self.getListaDatos()
        lista = Counter(datos) #<---- obtener los valores de cada llave
        lista = list(lista.keys()) #obtener las llaves y luego convertilo a una lista
        return lista

    def getListaFrecAbsoluta(self):
        datos = self.getListaDatos()
        lista = Counter(datos) #<---- obtener los valores de cada llave
        lista = list(lista.values())
        return lista

    def getListaFrecRelativa(self):
        frecAbsoluta = self.getListaFrecAbsoluta()
        totalFrecAbsoluta = sum(self.getListaFrecAbsoluta())
        lista = []
        for x in frecAbsoluta:
            operacion = (x * 100) / totalFrecAbsoluta
            lista.append(round(operacion,2)) #<--- round se utiliza para redondear a 2 decimales

        return lista


class DatosAgrupados:
    def getListaClases(self):
        datosContinuos = DatosContinuos()       
        lista = datosContinuos.getListaClases()
        return lista

    def getListaMarcaDeClase(self):
        datosContinuos = DatosContinuos()
        lista = datosContinuos.getListaMarcaDeClase()
        return lista

    def getListaFrecAbsoluta(self):
        datosContinuos = DatosContinuos()
        lista = datosContinuos.getListaFrecAbsoluta()
        return lista

    def getListaFrecuencia_Marca_Media(self):
        lista = []
        tamano = len(self.getListaClases())
        index = 0
        while index < tamano:
            clase = self.getListaMarcaDeClase().__getitem__(index)
            frecAbsoluta = self.getListaFrecAbsoluta().__getitem__(index)
            value =  clase * frecAbsoluta
            lista.append(value)
            index+=1
        return lista

    def getListaFrecuencia_Marca_Dispersion(self):
        lista = []
        tamano = len(self.getListaClases())
        index = 0
        while index < tamano:
            clase = self.getListaMarcaDeClase().__getitem__(index)
            frecAbsoluta = self.getListaFrecAbsoluta().__getitem__(index)
            value =  clase * pow(frecAbsoluta,2)
            lista.append(value)
            index+=1
        return lista


class WindowGraphics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/secondWindow.ui', self)
        self.btnVolver.clicked.connect(self.close)

        datosContinuos = DatosContinuos()
        tendencia = tendenciaCentral()
        self.label_NDeClases_Resultado.setText(str(datosContinuos.getNoDeClase()))
        self.label_Rango_Resultado.setText(str(datosContinuos.getRango()))
        self.label_AnchoClases_Resultado.setText(str(datosContinuos.getAnchoDeClase()))
        self.label_MediaAritmetica_Resultado.setText(str(tendencia.media_arimetica))
        self.label_MediaGeometrica_Resultado.setText(str(tendencia.media_geometrica))
        self.label_Mediana_Resultado.setText(str(tendencia.mediana))
        self.label_Moda_Resultado.setText(str(tendencia.moda))
        self.label_Varianza_Resultado.setText(str(tendencia.varianza))
        self.label_DesviacionEstandar_Resultado.setText(str(tendencia.desviacion))

        tendencia_Discreto = tendenciaCentral_Discreto()
        self.label_MediaAritmetica_Resultado_Discreto.setText(str(tendencia_Discreto.media_arimetica))
        self.label_Mediana_Resultado_Discreto.setText(str(tendencia_Discreto.mediana))
        self.label_Moda_Resultado_Discreto.setText(str(tendencia_Discreto.moda))
        self.label_Varianza_Resultado_Discreto.setText(str(tendencia_Discreto.varianza))
        self.label_DesviacionEstandar_Resultado_Discreto.setText(str(tendencia_Discreto.desviacion))


class WindowGraphics_DatosAgrupados(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/datosAgrupados.ui', self)
        self.btnVolver.clicked.connect(self.close)

        #Table View de la Media
        self.tableView_Media.setColumnWidth(0,250) #Columna 1
        self.tableView_Media.setColumnWidth(1,288) #Columna 2
        self.tableView_Media.setColumnWidth(2,290) #Columna 3
        self.tableView_Media.setColumnWidth(3,290) #Columna 3

        #Table View de Dispersion
        self.tableView_Dispersion.setColumnWidth(0,250) #Columna 1
        self.tableView_Dispersion.setColumnWidth(1,288) #Columna 2
        self.tableView_Dispersion.setColumnWidth(2,290) #Columna 3
        self.tableView_Dispersion.setColumnWidth(3,290) #Columna 3

        #Labels de tendencia central y dispersion para datos agrupados
        datosAgrupados = tendenciaCentral_DatosAgrupados()

        self.label_MediaAritmetica_Resultado_Agrupado.setText(str(datosAgrupados.media_arimetica))
        self.label_Moda_Resultado_Agrupado.setText(str(datosAgrupados.moda))
        self.label_Mediana_Resultado_Agrupado.setText(str(datosAgrupados.mediana))
        self.label_Varianza_Resultado_Agrupado.setText(str(datosAgrupados.varianza))
        self.label_DesviacionEstandar_Resultado_Agrupado.setText(str(datosAgrupados.desviacion))

        datos_ = DatosAgrupados()
        total_1 = sum(datos_.getListaFrecuencia_Marca_Media())
        total_2 = sum(datos_.getListaFrecuencia_Marca_Dispersion())
        self.label_Total_1_Resultado.setText(str(total_1))
        self.label_Total_2_Resultado.setText(str(total_2))

        self.loadData_DatosAgrupados()

    def loadData_DatosAgrupados(self):
        datosAgrupados = DatosAgrupados()
        clases = datosAgrupados.getListaClases()
        marcaDeClase = datosAgrupados.getListaMarcaDeClase()
        frecAbs = datosAgrupados.getListaFrecAbsoluta()
        frec_Marca_Media = datosAgrupados.getListaFrecuencia_Marca_Media()
        frec_Marca_Dispersion = datosAgrupados.getListaFrecuencia_Marca_Dispersion()
        tamano = len(clases)
        row = 0
        
        self.tableView_Media.setRowCount(tamano)
        self.tableView_Dispersion.setRowCount(tamano)
        while row < tamano:
            self.tableView_Media.setItem(row, 0, QtWidgets.QTableWidgetItem(str(clases[row])))
            self.tableView_Media.setItem(row, 1, QtWidgets.QTableWidgetItem(str(marcaDeClase[row])))
            self.tableView_Media.setItem(row, 2, QtWidgets.QTableWidgetItem(str(frecAbs[row])))
            self.tableView_Media.setItem(row, 3, QtWidgets.QTableWidgetItem(str(frec_Marca_Media[row])))
            
            self.tableView_Dispersion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(clases[row])))
            self.tableView_Dispersion.setItem(row, 1, QtWidgets.QTableWidgetItem(str(marcaDeClase[row])))
            self.tableView_Dispersion.setItem(row, 2, QtWidgets.QTableWidgetItem(str(frecAbs[row])))
            self.tableView_Dispersion.setItem(row, 3, QtWidgets.QTableWidgetItem(str(frec_Marca_Dispersion[row])))
            row=row+1


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

        datosDiscretos = DatosDiscretos()
        datosContinuos = DatosContinuos()
   
        #BOTONES QUE HAY EN EL MENU PRINCIPAL
        self.btnBarras.clicked.connect(self.printBarras)
        self.btnHistograma.clicked.connect(self.printHistograma)
        self.btnOjiva.clicked.connect(self.printOjiva)
        self.btnPastel.clicked.connect(self.printPastel)
        self.btnPoligono.clicked.connect(self.printPoligono)
        self.btnTendencia.clicked.connect(self.tendenciaCentral)
        self.btnDatosAgrupados.clicked.connect(self.datosAgrupados)
        self.btnExit.clicked.connect(self.close) #<--- cerrar la aplicación

        #TABLEVIEW - Datos Discretos
        self.tableView_Discretos.setColumnWidth(0,360) #Columna 1
        self.tableView_Discretos.setColumnWidth(1,360) #Columna 2
        self.tableView_Discretos.setColumnWidth(2,375) #Columna 3

        #TableVIEW - Datos Continuos
        self.tableView_Continuos.setColumnWidth(0,120) #Columna 1
        self.tableView_Continuos.setColumnWidth(1,160) #Columna 2
        self.tableView_Continuos.setColumnWidth(2,160) #Columna 3
        self.tableView_Continuos.setColumnWidth(3,150) #Columna 4
        self.tableView_Continuos.setColumnWidth(4,150) #Columna 5
        self.tableView_Continuos.setColumnWidth(5,150) #Columna 6
        self.tableView_Continuos.setColumnWidth(6,185) #Columna 7
        
        self.loadData_Discretos() #<--- llenar tableView Datos Discretos
        self.loadData_Continuos() #<-- llenar tableView Datos Continuos

        #LABELS - DATOS DISCRETOS
        sumFrecAbs = sum(datosDiscretos.getListaFrecAbsoluta())
        sumFrecRel = sum(datosDiscretos.getListaFrecRelativa())
        self.label_FrecuenciaAbsTotal_Discretos_Resultados.setText(str(sumFrecAbs))
        self.label_FrecuenciaRelTotal_Discretos_Resultados.setText(str(sumFrecRel))

        #LABELS - DATOS CONTINUOS
        sumFrecAbs_2 = sum(datosContinuos.getListaFrecAbsoluta())
        sumFrecRel_2 = sum(datosContinuos.getListaFrecRelativa())
        self.label_FrecuenciaAbsTotal_Continuos_Resultados.setText(str(sumFrecAbs_2))
        self.label_FrecuenciaRelTotal_Continuos_Resultados.setText(str(sumFrecRel_2))
        
#------------------------ LLENAR DATOS EN LA TABLA ------------------------
    def loadData_Discretos(self):
        datosDiscretos = DatosDiscretos()
        valores = datosDiscretos.getListaValores() 
        frecAbsoluta = datosDiscretos.getListaFrecAbsoluta()
        frecRelativa = datosDiscretos.getListaFrecRelativa()
        tamano = len((valores))
        row = 0
        
        self.tableView_Discretos.setRowCount(tamano)
        while row < tamano:
            self.tableView_Discretos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(valores[row])))
            self.tableView_Discretos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(frecAbsoluta[row])))
            self.tableView_Discretos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(frecRelativa[row])))
            row=row+1

    def loadData_Continuos(self):
        datosContinuos = DatosContinuos()
        clases = datosContinuos.getListaClases()
        tamano = len(clases)
        marcaDeClase = datosContinuos.getListaMarcaDeClase()
        frecAbsoluta = datosContinuos.getListaFrecAbsoluta()
        frecRelativa = datosContinuos.getListaFrecRelativa()
        frecAbsolutaAcumulada = datosContinuos.getListaFrecAbsAcumulada()        
        row = 0

        self.tableView_Continuos.setRowCount(tamano)
        while row < tamano:
            self.tableView_Continuos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(clases[row])))
            self.tableView_Continuos.setItem(row, 3, QtWidgets.QTableWidgetItem(str(marcaDeClase[row])))
            self.tableView_Continuos.setItem(row, 4, QtWidgets.QTableWidgetItem(str(frecAbsoluta[row])))
            self.tableView_Continuos.setItem(row, 5, QtWidgets.QTableWidgetItem(str(frecRelativa[row])))
            self.tableView_Continuos.setItem(row, 6, QtWidgets.QTableWidgetItem(str(frecAbsolutaAcumulada[row])))
            row+=1

        #LIMITES
        limites = datosContinuos.getLimites()
        m = len(limites) #<--- filas
        n = 2 #<----- columnas
        for f in range(m):
            for c in range(n):
                self.tableView_Continuos.setItem(f, c+1, QtWidgets.QTableWidgetItem(str(limites[f][c])))

#------------------------ GRAFICAS -----------------------------------------
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
        pyplot.bar(dict.keys(),dict.values())
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

    def tendenciaCentral(self):
        w = WindowGraphics()
        self.demo = w
        self.demo.show()

    def datosAgrupados(self):
        w = WindowGraphics_DatosAgrupados()
        self.demo = w
        self.demo.show()


##sintaxis del main
if __name__ == '__main__':
    screen = Tk()
    app = QApplication(sys.argv)
    window = Main()
    window.resize(screen.winfo_screenwidth(),screen.winfo_screenheight()) # <-- se ajusta al tamaño de la pantalla
    window.setWindowTitle("Uso del Transporte") #<--- colocar nombre a la aplicacion
    window.setWindowIcon(QIcon('./Resources/icon.png')) #<--- colocar icono para la aplicacion
    window.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
