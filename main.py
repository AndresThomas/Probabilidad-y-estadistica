#import libraries PyQt5
#import the name of the file from designer 
import sys
import pandas as pd
import numpy as np
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
        return clases #1,2,3,4,5,6,7,8,9

    def getListaDatos(self):
        lista = []
        indice = 0
        for x in dicts:
            lista.insert(indice, x.get("distancia"))
            indice+=1
        lista.sort() #<--- ordenar lista de manera ascendente
        return lista #mayor a menor en distancia

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
        listaFrecuenciaAbsoluta = []
        m = len(limites) #<---- 9 filas
        n = 2 #<---- 2 columnas
        lim_inf = []
        lim_sup = []
        items = []

        #consigue limite inferior y superior en un rango
        for f in range (m):
            for c in range (n):
                if c == 0:      
                    lim_inf.append(limites[f][c])
                    lim_sup.append(limites[f][c+1])
        """
        for posicion in range(m):
            count = 0
            for index in range (len(datos)):          
                if datos[index] <= lim_sup[posicion] and datos[index] >= lim_inf[posicion]:
                    count+=1
            print("Lim Inf: ", lim_inf[posicion], "-", "Lim Sup: ",lim_sup[posicion] ,"Conteo - Posicion ", posicion, ": ", count)
            listaFrecuenciaAbsoluta.append(count)
        """

        """
        listFrecuenciaDatos = self.__frecuenciaAbsolutaDatos.copy()
        listLimites = self.__limitesClases
        anterior = 0
        for limites in listLimites:
            superio = limites[1]
            acumulativo = 0
            for frecuencia in listFrecuenciaDatos:
                valor = frecuencia[0]
                if valor<= superio:
                    acumulativo += frecuencia[1]
            listFrecuencia.append(acumulativo-anterior)
            anterior=acumulativo
        return listFrecuencia
        """
        
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

global_datosContinuos = DatosContinuos()

#------------ Multiple Values - Tendenciales centrales y dispersion -------------------------------#
class TendenciaCentral_Continuo:
    def calcular_media_truncada(self,datos):
        suma = 0
        suma_inferior=0
        suma_superior=0
        
        for n in datos:
            suma +=n
        print(suma)
        
        
        for dato in datos[:20]:
            suma_inferior += dato
        print(suma_inferior)
        
        for m in datos[179:200]:
            suma_superior +=m
        print(suma_superior)
        suma -= (suma_inferior+suma_superior) 
        return round(suma/160,2)

    def __init__(self):
        datos = global_datosContinuos.getListaDatos()
        self.media_arimetica = round(stats.mean(datos),2) #<--- sacar la media aritmetica
        self.media_geometrica = round(stats.geometric_mean(datos),2) #<--- sacar la media geometrica
        self.mediana = round(stats.median(datos),2) #<--- sacar la mediana
        self.media_truncada =self.calcular_media_truncada(datos)
        self.moda = round(stats.mode(datos),2) #<--- sacar la moda
        self.varianza = round(stats.variance(datos),2) #<--- sacar la varianza muestral
        self.desviacion = round(stats.stdev(datos),2) #<--- sacar la desviacion estandar
        self.sesgo = cal_sesgo(self.media_arimetica, self.moda, self.desviacion) #<--- sacar el sesgo

def tendenciaCentral():
    return TendenciaCentral_Continuo()


class TendenciaCentral_Discreto:
    def __init__(self):
        datos = global_datosDiscretos.getListaDatos()
        self.media_arimetica = round(stats.mean(datos),2) #<--- sacar la media aritmetica
        self.mediana = round(stats.median(datos),2) #<--- sacar la mediana
        self.moda = round(stats.mode(datos),2) #<--- sacar la moda
        self.varianza = round(stats.variance(datos),2) #<--- sacar la varianza muestral
        self.desviacion = round(stats.stdev(datos),2) #<--- sacar la desviacion estandar
        self.sesgo = cal_sesgo(self.media_arimetica, self.moda, self.desviacion) #<--- sacar el sesgo

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
        lista = global_datosContinuos.getListaClases()
        return lista

    def getListaMarcaDeClase(self):
        lista = global_datosContinuos.getListaMarcaDeClase()
        return lista

    def getListaFrecAbsoluta(self):
        lista = global_datosContinuos.getListaFrecAbsoluta()
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
            value =  round(frecAbsoluta * pow(clase,2),2)
            lista.append(value)
            index+=1
        return lista
global_datosDiscretos = DatosDiscretos()

def cal_sesgo(media_aritmetica, moda, desviacion_estandar):
    sego = None
    value = ((media_aritmetica - moda)/(desviacion_estandar))
    if value < 0:
        sego ="Izquierda"
    elif value == 0:
        sego = "Centro"
    else:
        if value > 0:
            sego ="Derecha"
            
    return sego
    

class WindowGraphics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Views/secondWindow.ui', self)
        self.btnVolver.clicked.connect(self.close)
        tendencia = tendenciaCentral()
        self.label_NDeClases_Resultado.setText(str(global_datosContinuos.getNoDeClase()))
        self.label_Rango_Resultado.setText(str(global_datosContinuos.getRango()))
        self.label_AnchoClases_Resultado.setText(str(global_datosContinuos.getAnchoDeClase()))
        self.label_MediaAritmetica_Resultado.setText(str(tendencia.media_arimetica))
        self.label_MediaGeometrica_Resultado.setText(str(tendencia.media_geometrica))
        self.label_Mediana_Resultado.setText(str(tendencia.mediana))
        self.label_Moda_Resultado.setText(str(tendencia.moda))
        self.label_Varianza_Resultado.setText(str(tendencia.varianza))
        self.label_DesviacionEstandar_Resultado.setText(str(tendencia.desviacion))
        self.label_Sesgo_Resultado.setText(str(tendencia.sesgo))

        tendencia_Discreto = tendenciaCentral_Discreto()
        self.label_MediaAritmetica_Resultado_Discreto.setText(str(tendencia_Discreto.media_arimetica))
        self.label_Mediana_Resultado_Discreto.setText(str(tendencia_Discreto.mediana))
        self.label_Moda_Resultado_Discreto.setText(str(tendencia_Discreto.moda))
        self.label_Varianza_Resultado_Discreto.setText(str(tendencia_Discreto.varianza))
        self.label_DesviacionEstandar_Resultado_Discreto.setText(str(tendencia_Discreto.desviacion))
        self.label_Sesgo_Resultado_Discreto.setText(str(tendencia_Discreto.sesgo))


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
        self.data = pd.read_csv('file.csv') #<-- leemos el archivo csv
        self.df = pd.DataFrame(self.data) #<-- creamos un dataframe        
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
        self.btnTendencia.clicked.connect(self.tendenciaCentral)
        self.btnDatosAgrupados.clicked.connect(self.datosAgrupados)
        self.btnExit.clicked.connect(self.close) #<--- cerrar la aplicación

        #TABLEVIEW - Datos Discretos
        self.tableView_Discretos.setColumnWidth(0,260) #Columna 1
        self.tableView_Discretos.setColumnWidth(1,260) #Columna 2
        self.tableView_Discretos.setColumnWidth(2,260) #Columna 3

        #TableVIEW - Datos Continuos
        self.tableView_Continuos.setColumnWidth(0,105) #Columna 1
        self.tableView_Continuos.setColumnWidth(1,105) #Columna 2
        self.tableView_Continuos.setColumnWidth(2,105) #Columna 3
        self.tableView_Continuos.setColumnWidth(3,105) #Columna 4
        self.tableView_Continuos.setColumnWidth(4,105) #Columna 5
        self.tableView_Continuos.setColumnWidth(5,105) #Columna 6
        self.tableView_Continuos.setColumnWidth(6,140) #Columna 7
        
        self.loadData_Discretos() #<--- llenar tableView Datos Discretos
        self.loadData_Continuos() #<-- llenar tableView Datos Continuos

        #LABELS - DATOS DISCRETOS
        sumFrecAbs = sum(global_datosDiscretos.getListaFrecAbsoluta())
        sumFrecRel = sum(global_datosDiscretos.getListaFrecRelativa())
        self.label_FrecuenciaAbsTotal_Discretos_Resultados.setText(str(sumFrecAbs))
        self.label_FrecuenciaRelTotal_Discretos_Resultados.setText(str(sumFrecRel))

        #LABELS - DATOS CONTINUOS
        sumFrecAbs_2 = sum(global_datosContinuos.getListaFrecAbsoluta())
        sumFrecRel_2 = sum(global_datosContinuos.getListaFrecRelativa())
        self.label_FrecuenciaAbsTotal_Continuos_Resultados.setText(str(sumFrecAbs_2))
        self.label_FrecuenciaRelTotal_Continuos_Resultados.setText(str(sumFrecRel_2))
        
#------------------------ LLENAR DATOS EN LA TABLA ------------------------
    def loadData_Discretos(self):
        valores = global_datosDiscretos.getListaValores() 
        frecAbsoluta = global_datosDiscretos.getListaFrecAbsoluta()
        frecRelativa = global_datosDiscretos.getListaFrecRelativa()
        tamano = len((valores))
        row = 0
        
        self.tableView_Discretos.setRowCount(tamano)
        while row < tamano:
            self.tableView_Discretos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(valores[row])))
            self.tableView_Discretos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(frecAbsoluta[row])))
            self.tableView_Discretos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(frecRelativa[row])))
            row=row+1

    def loadData_Continuos(self):
        #datosContinuos = DatosContinuos()
        clases = global_datosContinuos.getListaClases()
        tamano = len(clases)
        marcaDeClase = global_datosContinuos.getListaMarcaDeClase()
        frecAbsoluta = global_datosContinuos.getListaFrecAbsoluta()
        frecRelativa = global_datosContinuos.getListaFrecRelativa()
        frecAbsolutaAcumulada = global_datosContinuos.getListaFrecAbsAcumulada()        
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
        limites = global_datosContinuos.getLimites()
        m = len(limites) #<--- filas
        n = 2 #<----- columnas
        for f in range(m):
            for c in range(n):
                self.tableView_Continuos.setItem(f, c+1, QtWidgets.QTableWidgetItem(str(limites[f][c])))

#------------------------ GRAFICAS -----------------------------------------
    def printBarras(self):
        pyplot.bar(global_datosDiscretos.getListaValores(),global_datosDiscretos.getListaFrecAbsoluta())
        #pyplot.bar(dict.keys(),dict.values())
        pyplot.xlabel("Valores")
        pyplot.ylabel("Frecuencia Absoluta")
        pyplot.show()
        
        
    def printHistograma(self):
        pyplot.xlabel("Valores")
        pyplot.ylabel("Frecuencia Absoluta")
        pyplot.hist(global_datosContinuos.getListaFrecAbsoluta(),bins=5,edgecolor='black',density=True)
        pyplot.show()

    def printOjiva(self):
        lim_inf = []
        m = len(global_datosContinuos.getLimites()) #<---- 9 filas
        n = 2 #<---- 2 columnas
        #consigue limite inferior y superior en un rango
        for f in range (m):
            for c in range (n):
                if c == 0:      
                    lim_inf.append(global_datosContinuos.getLimites()[f][c])

        #Datos primordiales
        frec_rel = [0,0,0,0,0,0,0,0,0]
        class_mark = [0,0,0,0,0,0,0,0,0]
        total = len(global_datosContinuos.getListaDatos())
        rango = global_datosContinuos.getRango()
        nclass = global_datosContinuos.getNoDeClase()
        anchoclass = (rango / nclass) + 0.0001
        limite_in_array = lim_inf
        frecuence = global_datosContinuos.getListaFrecAbsoluta()
        
        #Obtener frecuencia relativa
        for i in range(len(limite_in_array)):
            j = len(limite_in_array) - (i + 1)
            frec_rel[i] = ((frecuence[j] / total))
            class_mark[i] =((limite_in_array[j] + (anchoclass) / 2))
            
        #Frecuencia relativa acumulada 
        fr_rlv_acum = np.zeros(nclass, dtype=float)
        for i in range(len(frec_rel)):
            if(i == 0):
                fr_rlv_acum[i] = frec_rel[i]
            else:
                fr_rlv_acum[i] = round(fr_rlv_acum[i-1] + frec_rel[i], 4)
        
        pyplot.title("Ojiva")
        pyplot.plot(fr_rlv_acum)
        pyplot.ylabel("Frecuencia relativa acumulada")
        pyplot.show()

    def printPastel(self):
        labels = ['Hombres','Mujeres']
        pyplot.pie([self.menPoblation.__len__(),self.womenPoblation.__len__()],labels=labels,autopct='%.2f %%')
        pyplot.show()
        
    def printPoligono(self):
        pyplot.xlabel("Valores")
        pyplot.ylabel("Frecuencia Absoluta")
        #bins = [0,2.5,5,7.5,10,12.5,15,17.5,20,22.5,25,27.5,30,32.5,35,37.5,40,42.5,45,47.5,50,52.5]
        bins = [0,5,10,15,20,25,30,35,40,45,50,55,60]
        pyplot.xticks(bins)
        y,edges,_ =pyplot.hist(global_datosContinuos.getListaDatos(),bins=bins,histtype='step',edgecolor='k')
        middle_points = 0.5 *(edges[1:]+edges[:-1])
        pyplot.plot(middle_points,y,'r-*')
        pyplot.show()

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
    screen =''
    window.show()

    try: 
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')