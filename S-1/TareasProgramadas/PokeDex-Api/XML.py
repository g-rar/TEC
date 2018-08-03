"""
Desarrollado por: Abraham Meza, Gerardo López y Tribeth Rivas.
Fecha de creacion: 13/05/18.
Ultima modificacion: 20/05/18.
Version: 3.6.5
"""
#Manejo de XML
def PokemonXML(lista):
    """
    Funcion: Toma una lista de tipo pokemon basado en el formato
        [ID,nombre,URL,[Imagen,Peso,Altura]] que denota un pokemon
        y convierte esa lista en un string con formato XML para pokemones.
    Entradas: Lista(list) Una lista con el formato mencionado anteiormente.
    Salidas: String(str) Un string en formato XML con todas las
        descripciones del pokemon basado en la lista.
    """
    return "\n    <Pokemon>\n        <ID>"+str(lista[0])+"</ID>\n        <nombre>"+str(lista[1])+"</nombre>\n        <URL>"+lista[2]+"</URL>\n        <Icono>"+lista[3][0]+"</Icono>\n        <Peso>"+str(lista[3][1])+"</Peso>\n        <Altura>"+str(lista[3][2])+"</Altura>\n    </Pokemon>\n"

def PokemonesXML(lista):
    """
    Entradas: Un string con la lista de los pokemones en formato XML
    Salidas: La lista con la etiqueta de inicio y final.
    Funcionamiento: Coloca la etiqueta de comienzo y final para completar
        la lista en formato XML
    """
    return "<Pokemones>"+lista+"</Pokemones>"
