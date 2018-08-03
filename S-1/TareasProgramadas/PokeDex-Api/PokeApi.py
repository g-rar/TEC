import requests
import os
import urllib.request

#Manejo de http request/respond
def conseguirPokemones(limite):
    """
    Entradas: Un número entero.
    Salidas: Una lista
    Funcionamiento: La hace varios request a la API para obtener la
        información de los pokemones, y los inserta en una lista.
    """
    matrizRetorno = []
    listaAux = []
    subLista = []
    url = "https://pokeapi.co/api/v2/pokemon-form/?limit="+str(limite)
    pokeapi = requests.get(url)
    informacionPokemon = pokeapi.json()
    resultados = informacionPokemon.get('results',[])
    ID = 1
    for pokemon in resultados:
        listaAux.append(ID)
        listaAux.append(pokemon["name"])
        listaAux.append("https://pokeapi.co/api/v2/pokemon/"+str(ID))
        pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(ID))
        informacionPokemon = pokemon.json()
        subLista.append(informacionPokemon["sprites"]["front_default"])
        subLista.append(str(informacionPokemon["weight"]))
        subLista.append(str(informacionPokemon["height"]))
        listaAux.append(subLista)
        matrizRetorno.append(listaAux)
        subLista , listaAux = [], []
        ID+=1
    return matrizRetorno
                
def descargarImagen(url):
    """
    Entradas: Una URL
    Salidas: N/A
    Funcionamiento: Descarga la imagen de la URL y le da el formato .gif
    """
    urllib.request.urlretrieve(url, 'pokemon.gif')
    return
