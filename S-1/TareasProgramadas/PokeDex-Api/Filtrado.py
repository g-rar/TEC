"""
Desarrollado por: Abraham Meza, Gerardo López y Tribeth Rivas.
Fecha de creacion: 13/05/18.
Ultima modificacion: 20/05/18.
Version: 3.6.5
"""
import random
probabilidades = "cbigzsvyjk"
#Filtrado por aproximacion
def filtrarPorAproximacion(nombre,lista):
    """
    Funcion: Toma un nombre, busca en una lista y retorna una lista con
        nombres que estén en la lista que tengan parecido con el nombre
        ingresado.
    Entradas: String(str) Un nombre a buscar, Lista(list) Una lista en
        la cual se buscará el nombre ingresado.
    Salidas: Lista(list) Una lista con los nombres más parecidos, ordenados
        del más parecido, al menos parecido.
    """
    listaNumeros = []
    listaNombres = []
    if(len(nombre)>0):
        for i in lista:
            nombreAux = nombre
            if (len(nombreAux)!= len(i[1])):
                nombreAux = ajustarNombre(nombreAux,i[1])
            aproximado = 0
            puntero = 0
            for a in i[1]:
                if (nombreAux[puntero] == a):
                    aproximado+=1
                elif (nombreAux[puntero] in probabilidades and a in probabilidades):
                    aproximado+=1
                puntero+=1
            if (aproximado>=len(nombreAux)//2):
                listaNumeros.append(aproximado)
                listaNombres.append(i)
    return ordenar(listaNumeros,listaNombres)

def ajustarNombre(nombre1,nombre2):
    """
    Funcion: Toma como parametro dos nombres y si el primero es más grande
        que el segundo le recorta letras del centro al primero, sino añade
        vocales de manera aleatoria en el centro hasta que queden de igual
        longitud
    Entradas: String(str) Dos string cualquiera.
    Salidas: String(str) El primer string modificado de manera que sea de
        igual longitud que el segundo.
    """
    vocales = "aeiou"
    while(len(nombre1)>len(nombre2)):
        nombre1 = nombre1[:len(nombre1)//2]+nombre1[1+len(nombre1)//2:]
    while(len(nombre1)<len(nombre2)):
        nombre1 = nombre1[:len(nombre1)//2]+vocales[random.randint(0,4)]+nombre1[len(nombre1)//2:]
    return nombre1

def ordenar(numeros,nombres):
    """
    Funcion: Toma dos listas una con numeros y otra con nombres asociados
        a la misma posicion, ordena los numeros de mayor a menor y los nombres
        se ordenaran respectivamente al ordenamiento de los números,
        posteriormente retorna una lista con los nombres ordenados.
    Entradas: Lista(list) Una lista con números,Lista(list) Una lista con nombres.
    Salidas: Lista(list) Una lista con los nombres ordenados.
    """
    listaRetorno = []
    while(len(numeros) != 0):
        mayor = max(numeros)
        pokemon = nombres[numeros.index(mayor)]
        listaRetorno.append(pokemon)
        numeros.remove(mayor)
        nombres.remove(pokemon)
    return listaRetorno

def filtrarPorRango(lista, minimo, maximo):
    """
    Entradas: La lista de los pokemones, y dos números tipo str 
    Salidas: La lista filtrada
    Funcionamiento: Selecciona a los pokemones cuyos pesos se encuentran entre el
        número mínimo y el número máximo.
    """
    listaRetorno =  []
    for elem in lista:
        if float(elem[3][1]) >= float(minimo) and float(elem[3][1]) <= float(maximo):
            listaRetorno.append(elem)
    return listaRetorno
