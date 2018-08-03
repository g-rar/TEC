#Creado por: Gerardo López, Abraham Meza y Tribeth Rivas
#Fecha de creación: 7/6/18
#Última modificación: 7/6/18
#Versión: 3.6.5
from Inicio import *
import sys

archivo = Archivo("Poblacion")
try:
    lista = archivo.leerBinario()
    print(lista[0].getNombre())
except:
    lista = []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = Inicio(lista)
    sys.exit(app.exec())
