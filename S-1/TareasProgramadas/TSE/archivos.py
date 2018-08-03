#Creado por: Gerardo López, Abraham Meza y Tribeth Rivas
#Fecha de creación: 6/6/2018
#últma modificación: 6/6/2018
#Versión: 3.6.5
import pickle

class Archivo:
    nombre = ""
    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre
    #Getters y Setters
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    #Metodos
    def leerTexto(self):
        """
        Entradas: N/A
        Salidas: Texto dentro del archivo
        Funcionamiento: Lee el archivo y regresa un string con lo que había
        dentro de este
        """
        datos = open(self.nombre, "r")
        texto = ""
        for linea in datos:
            texto += linea
        datos.close()
        return texto
    
    def escribirTexto(self, texto):
        """
        Entradas: texto de tipo string
        Salidas: Escribe en el archivo
        Funcionamiento: Escribe el texto dado en el archivo
        """
        datos = open(self.nombre, "a")
        datos.write(texto)
        datos.close()
        return
    
    def leerBinario(self):
        """
        Entradas: N/A
        Salidas: Lista con los datos del archivo
        Funcionamiento: Lee y archivo y retorna una lista con los datos que hay
        en este.
        """
        datos = open(self.nombre, "rb")
        lista = pickle.load(datos)
        datos.close()
        return lista

    def guardarBinario(self, lista):
        """
        Entradas: lista de objetos
        Salidas: Guarda en el archivo binario
        Funcionamiento: Guarda la lista pasada por parametro en el archivo binario
        """
        datos = open(self.nombre, "wb")
        pickle.dump(lista, datos)
        datos.close()
        return
    
