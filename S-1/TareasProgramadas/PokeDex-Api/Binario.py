#Elaborado por: Geraro López Calderón, Abraham y Triveth.
#Fecha de creación: 14/5/2018
#Última modificación: 14/5/2018
#Versión: 3.6.4

import pickle

def guardarEnBinario(objeto):
    """
    Entradas: El objeto a guardar
    Salidas: La lista junto con el objeto guardado
    Funcionamiento: Carga la lista en binario, luego añade el objeto
        a la lista y vuelve a guardar el archivo. Retorna la lista con
        el objeto guardado
    """
    archivo = open('MisPokemones','rb')
    lista = pickle.load(archivo)
    archivo.close()
    lista.append(objeto)
    archivo = open('MisPokemones', 'wb')
    pickle.dump(lista, archivo)
    archivo.close()
    return lista

def cargarBinario():
    """
    Entradas: N/A
    Salidas: La lista contenida en el archivo binario
    Funcionamiento: Carga el archivo binario y retorna la lista que
        contiene
    """
    archivo = open('MisPokemones','rb')
    lista = pickle.load(archivo)
    archivo.close()
    return lista

