#Creado por: Abraham Meza, Gerardo López y Tribeth Rivas
#Fecha de creación: 5/5/18
#Última modificación: 19/5/18 por Gerardo
#Versión: 3.6.5
from Binario import *
from interfaz import *
from Filtrado import *
from Correo import *
import pickle

pokemones = []
index = 0
mostrarPesos = False

#Definición de funciones
def crearDialogo():
    """
    Entradas: N/A
    Salidas: Crea una ventana de dialogo
    Funcionamiento: Crea una ventana de dialogo para opciones de filtrado
    """
    dialogo = Tk()
    modificarVentana(dialogo, "Filtrar", "125", "425")
    crearLabel("¿Qué tipo de filtrado desea?", 15, 75, 0, dialogo)
    crearBoton("Filtrado por rango", 1, 15, 10, 90, dialogo, lambda: opcionPorRango(dialogo))
    crearBoton("Filtrado por aproximación", 1, 20, 265, 90, dialogo, lambda: opcionPorAproximacion(dialogo))
    return

def pedirDatosXML():
    """
    Entradas: N/A
    Salidas: Crea una ventana de dialogo
    Funcionamiento: Pide los datos de gmail al usuario para
        enviar el archivo XML
    """
    dialogo = Toplevel()
    modificarVentana(dialogo, "Enviar XML", "150", "300")
    titulo = crearLabel("Ingrese sus datos de gmail:", 11, 30, 10, dialogo)
    usuario = crearLabel("Usuario:", 9, 15, 43, dialogo)
    contrasenna = crearLabel("Contraseña:",9, 15, 70, dialogo)
    gmail = crearLabel("@gmail.com", 9, 215, 45, dialogo)
    cajaUsuario = crearCajaTexto(None, 90, 45, dialogo)
    cajaContra = crearCajaTexto(None, 90, 72, dialogo, '*')
    enviar = crearBoton("Enviar XML", None, None, 210, 105, dialogo, lambda: llamadaEnviarXML(cajaUsuario.get()+'@gmail.com', cajaContra.get(), dialogo))

def llamadaEnviarXML(usuario, contrasenna, ventanaPadre):
    """
    Entradas: Los strings usuario y contraseña, además de una ventana tipo Tk.
    Salidas: Una ventana de información.
    Funcionamiento: Destruye la ventana anterior y hace el llamado a la función
        para enviar el XML a la dirección de los datos ingresados
    """
    global guardados
    destruirVentana(ventanaPadre)
    envioCorreo = enviarXML(usuario, contrasenna, guardados)
    messagebox.showinfo('Resultado',envioCorreo)
    return        


def limpiarBotones():
    """
    Entradas: N/A
    Salidas: Vuelve los botones de la GUI al estado inicial
    Funcionamiento: A los botones pokemon1, 2 y 3 les pone como texto "PokemonN"
        los botones XML1, 2 y 3; binario1, 2 y 3 y pokemon1, 2 y 3 se desactivan,
        los labels textoID1, 2 y 3 y textoPeso1, 2 y 3 se vacian
    """
    cambiarEstadoBoton(siguiente, estado = DISABLED)
    cambiarNombreBoton(pokemon1, "Pokemon 1")
    cambiarNombreBoton(pokemon2, "Pokemon 2")
    cambiarNombreBoton(pokemon3, "Pokemon 3")
    cambiarEstadoBoton(xml1, DISABLED)
    cambiarEstadoBoton(xml2, DISABLED)
    cambiarEstadoBoton(xml3, DISABLED)
    cambiarEstadoBoton(binario1, DISABLED)
    cambiarEstadoBoton(binario2, DISABLED)
    cambiarEstadoBoton(binario3, DISABLED)
    cambiarEstadoBoton(pokemon1, DISABLED)
    cambiarEstadoBoton(pokemon2, DISABLED)
    cambiarEstadoBoton(pokemon3, DISABLED)
    textoID1.set("")
    textoID2.set("")
    textoID3.set("")
    textoPeso1.set("")
    textoPeso2.set("")
    textoPeso3.set("")
    return

def actualizarBotones():
    """
    Entradas: N/A
    Salidas: Actualiza la info
    Funcionamiento: Establece los botones y labels con la info de la pestaña
        actual
    """
    global index, mostrarPesos
    try:
        cambiarNombreBoton(pokemon1, pokemones[index][1].title())
        cambiarNombreBoton(pokemon2, pokemones[index + 1][1].title())
        cambiarNombreBoton(pokemon3, pokemones[index + 2][1].title())
        cambiarEstadoBoton(xml1, "normal")
        cambiarEstadoBoton(xml2, "normal")
        cambiarEstadoBoton(xml3, "normal")
        cambiarEstadoBoton(binario1, "normal")
        cambiarEstadoBoton(binario2, "normal")
        cambiarEstadoBoton(binario3, "normal")
        cambiarEstadoBoton(pokemon1, "normal")
        cambiarEstadoBoton(pokemon2, "normal")
        cambiarEstadoBoton(pokemon3, "normal")
        textoID1.set(str(pokemones[index][0]))
        textoID2.set(str(pokemones[index + 1][0]))
        textoID3.set(str(pokemones[index + 2][0]))
        if mostrarPesos:
            textoPeso1.set(pokemones[index][3][1])
            textoPeso2.set(pokemones[index + 1][3][1])
            textoPeso3.set(pokemones[index + 2][3][1])
        if len(pokemones) > 3:
            cambiarEstadoBoton(siguiente, "normal")
        if index <= 0:
            cambiarEstadoBoton(atras, DISABLED)
    except IndexError:
        cambiarEstadoBoton(siguiente, estado = DISABLED)
        if index <= 0:
            cambiarEstadoBoton(atras, DISABLED)
        if len(pokemones) == 2 or len(pokemones) % 3 == 2:
            cambiarNombreBoton(pokemon1, pokemones[index][1].title())
            cambiarNombreBoton(pokemon2, pokemones[index + 1][1].title())
            cambiarEstadoBoton(xml1, "normal")
            cambiarEstadoBoton(xml2, "normal")
            cambiarEstadoBoton(binario1, "normal")
            cambiarEstadoBoton(binario2, "normal")
            cambiarEstadoBoton(pokemon1, "normal")
            cambiarEstadoBoton(pokemon2, "normal")
            textoID1.set(str(pokemones[index][0]))
            textoID2.set(str(pokemones[index+1][0]))
            if mostrarPesos:
                textoPeso1.set(pokemones[index][3][1])
                textoPeso2.set(pokemones[index + 1][3][1])
        elif len(pokemones) == 1 or len(pokemones) % 3 == 1:
            cambiarNombreBoton(pokemon1, pokemones[index][1].title())
            cambiarEstadoBoton(xml1, "normal")
            cambiarEstadoBoton(binario1, "normal")
            cambiarEstadoBoton(pokemon1, "normal")
            textoID1.set(str(pokemones[index][0]))
            if mostrarPesos:
                textoPeso1.set(pokemones[index][3][1])
    return

def opcionPorAproximacion(ventana):
    """
    Entradas: ventana de tipo Tk
    Salidas: Crea una ventana de dialogo para el filtrado por aproximación
    Funcionamiento: Destruye la ventana anterior, crea una nueva y le da el
        formato para pedir los datos para el filtrado
    """
    destruirVentana(ventana)
    dialogo = Tk()
    modificarVentana(dialogo, "Nombre", "90", "325")
    crearLabel("Ingrese el nombre del pokemon: ", 15, 5, 0, dialogo)
    caja = crearCajaTexto(47, 5, 30, dialogo)
    crearBoton("Aceptar", 1, 6, 125, 55, dialogo, lambda: aproximarVal(caja.get(), dialogo))
    return

def opcionPorRango(ventana):
    """
    Entradas: ventana de tipo Tk
    Salidas: Crea una ventana de dialogo
    Funcionamiento: Crea una ventana de dialogo donde pide la información para
        el filtrado por rango
    """
    destruirVentana(ventana)
    dialogo = Tk()
    modificarVentana(dialogo, "Rango", "110", "300")
    minimo = crearLabel("Ingrese el peso mínimo:", 9, 10, 20, dialogo)
    maximo = crearLabel("Ingrese el peso máximo:", 9, 10, 60, dialogo)
    entradaMinimo = crearCajaTexto(10, 150, 22, dialogo)
    entradaMaximo = crearCajaTexto(10, 150, 62, dialogo)
    botonListo = crearBoton("¡Listo!", 3, 9, 220, 22, dialogo, lambda: porRangoVal(entradaMinimo.get(), entradaMaximo.get(), dialogo))
    return


def porRangoVal(minimo, maximo, ventana):
    """
    Entradas: Dos string y un objeto tipo Tk
    Salidas: Llamada a la función porRango() o un messagebox
    Funcionamiento: Valida que el mínimo y máximo sean numéricos y que
        se cumpla que minimo < maximo
    """
    if minimo.isdigit() and maximo.isdigit() and minimo < maximo:
        porRango(minimo, maximo, ventana)
        return
    else:
        messagebox.showinfo('Error','Ingrese solo números sin decimales en ambos espacios y el minimo no puede ser mayor al máximo.')
        return

def aproximarVal(nombre, ventana):
    """
    Entradas: Un string y u objeto tipo Tk
    Salidas: Llamada a la función aproximar() o un messagebox
    Funcionamiento: Valida que el string ingresado sea una única palabra
        y que no contenga números ni signos de puntuación
    """
    if nombre.isalpha():
        aproximar(nombre, ventana)
        return
    else:
        messagebox.showinfo('Error','Ingrese solo una palabra.')
        return

def aproximar(nombre, ventana):
    """
    Entradas: nombre de tipo string y ventana de tipo Tk
    Salidas: El resultado de la filtración
    Funcionamiento: Destuye la ventana anterior y llama a filtrarPorAproximacion
        para luego actualizar los botones
    """
    destruirVentana(ventana)
    global pokemones, index
    index = 0
    pokemones = filtrarPorAproximacion(nombre, pokemones)
    limpiarBotones()
    actualizarBotones()
    return 

def porRango(minimo, maximo, ventana):
    """
    Entradas: Dos string numéricos y ventana tipo Tk
    Salidas: El resultado de la filtración
    Funcionamiento: Destruye la ventana anterior, llama a filtrarPorRango,
        habilita mostrarPesos y actualiza los botones. 
    """
    destruirVentana(ventana)
    global pokemones, index, mostrarPesos
    index = 0
    pokemones = filtrarPorRango(pokemones, minimo, maximo)
    mostrarPesos = True
    limpiarBotones()
    actualizarBotones()
    return

def guardarBinario(pokemon):
    """
    Entradas: pokemon de tipo matriz
    Salidas: Guarda en el binario
    Funcionamiento: llama a guardarEnBinario, actuliza los pokemones guardados y
        la cantidad mostrada en Mis pokemones
    """
    global guardados
    guardarEnBinario(pokemon)
    guardados = cargarBinario()
    cambiarEstadoBoton(verMisPokemones, "normal")
    cantidadMisPokemones.set("Mis pokemones: " + str(len(guardados)))
    return

def realizarBusqueda():
    """
    Entradas: datos de cuantosDeseaBuscarEntrada
    Salidas: actualiza la información de la ventana
    Funcionamiento: Obtiene lo ingresado en cuantosDeseaBuscarEntrada para
        realizar la busqueda y luego mostrar la información
    """
    global pokemones, index, mostrarPesos
    index = 0
    cantidad = cuantosDeseaBuscarEntrada.get()
    if cantidad == "0" or cantidad == "" or not cantidad.isdigit():
        messagebox.showinfo('Error','Ingrese un número sin decimales.')
        return
    if int(cantidad)>1000:
        messagebox.showinfo('Error','Ingrese un número menor o igual que 1000.')
        return
    #pokemones = conseguirPokemones(cantidad)
    with open("Pokemones","rb") as pk:
        pokemones = pickle.load(pk)
    mostrarPesos = False
    cuantosDeseaBuscarEntrada.delete(0, END)
    cambiarEstadoBoton(filtrar, "normal")
    limpiarBotones()
    actualizarBotones()
    return

def opcionSiguiente():
    """
    Entradas: N/A
    Salidas: Cambia de página
    Funcionamiento: incrementa el indice, activa el botón de atras y actualiza
        la información
    """
    global index, pokemones
    index += 3
    cambiarEstadoBoton(atras, "normal")
    limpiarBotones()
    actualizarBotones()
    if index + 3 >= len(pokemones):
        cambiarEstadoBoton(siguiente, DISABLED)

def opcionAtras():
    """
    Entradas: N/A
    Salidas: Cambia de página
    Funcionamiento: decrementa el indice, activa el botón de siguiente y actualiza
        la información
    """
    global index, pokemones
    index -= 3
    cambiarEstadoBoton(siguiente, "normal")
    limpiarBotones()
    actualizarBotones()
    if index <= 0:
        cambiarEstadoBoton(atras, DISABLED)

#Ventana principal
ventanaPrincipal = Tk()
modificarVentana(ventanaPrincipal, "Pokepad",  "700", "700")
#Texto del Label
textoID1 = StringVar()
textoID2 = StringVar()
textoID3 = StringVar()
textoPeso1 = StringVar()
textoPeso2 = StringVar()
textoPeso3 = StringVar()
cantidadMisPokemones = StringVar()
#Labels
crearLabel("Pokepad", 20, 300, 0, ventanaPrincipal)
crearLabel("¿Cuántos desea buscar?", 15, 15, 50, ventanaPrincipal)
crearLabel("Mis pokemons: ", 11, 510, 570, ventanaPrincipal, cantidadMisPokemones)
nombrelabel = crearLabel("Nombre", 12, 180, 140, ventanaPrincipal)
idlabel = crearLabel("ID", 12, 50, 140, ventanaPrincipal)
idlabel1 = crearLabel("", 12, 50, 180, ventanaPrincipal, textoID1)
idlabel2 = crearLabel("", 12, 50, 247, ventanaPrincipal, textoID2)
idlabel3 = crearLabel("", 12, 50, 310, ventanaPrincipal, textoID3)
pesoLabel1 = crearLabel("", 12, 290, 180, ventanaPrincipal,textoPeso1)
pesoLabel2 = crearLabel("", 12, 290, 247, ventanaPrincipal,textoPeso2)
pesoLabel3 = crearLabel("", 12, 290, 310, ventanaPrincipal,textoPeso3)
#Caja de texto
cuantosDeseaBuscarEntrada = crearCajaTexto(20, 290, 55, ventanaPrincipal)
#Botones
buscar = crearBoton("Buscar", 1, 12, 425, 50, ventanaPrincipal, realizarBusqueda)
filtrar = crearBoton("Filtrar", 1, 12, 550, 50, ventanaPrincipal, crearDialogo, DISABLED)
xml1 = crearBoton("Guardar en XML", 2, 12, 550, 175, ventanaPrincipal, lambda: pedirDatosXML(), DISABLED)
xml2 = crearBoton("Guardar en XML", 2, 12, 550, 237, ventanaPrincipal, lambda: pedirDatosXML(), DISABLED)
xml3 = crearBoton("Guardar en XML", 2, 12, 550, 300, ventanaPrincipal, lambda: pedirDatosXML(), DISABLED)
binario1 = crearBoton("Guardar en Binario", 2, 13, 355, 175, ventanaPrincipal, lambda: guardarBinario(pokemones[index]), estado = DISABLED)
binario2 = crearBoton("Guardar en Binario", 2, 13, 355, 237, ventanaPrincipal, lambda: guardarBinario(pokemones[index+1]), estado = DISABLED)
binario3 = crearBoton("Guardar en Binario", 2, 13, 355, 300, ventanaPrincipal, lambda: guardarBinario(pokemones[index+2]), estado = DISABLED)
pokemon1 = crearBoton("Pokemon 1", 2, 13, 160, 175, ventanaPrincipal, lambda: mostrarPokemon(index, pokemones), DISABLED)
pokemon2 = crearBoton("Pokemon 2", 2, 13, 160, 237, ventanaPrincipal, lambda: mostrarPokemon(index+1, pokemones), DISABLED)
pokemon3 = crearBoton("Pokemon 3", 2, 13, 160, 300, ventanaPrincipal, lambda: mostrarPokemon(index+2, pokemones), DISABLED)
atras = crearBoton("Atras", 1, 12, 40, 475, ventanaPrincipal, opcionAtras, estado = DISABLED)
siguiente = crearBoton("Siguiente", 1, 12, 550, 475, ventanaPrincipal, opcionSiguiente, DISABLED)
verMisPokemones = crearBoton("Ver mis pokemones", 1, 17, 510, 630, ventanaPrincipal, lambda: misPokemones(guardados),DISABLED)
#Activar MisPokemones
try:
    guardados = cargarBinario()
except:
    guardados = []
    archivo = open('MisPokemones', 'wb')
    lista = []
    pickle.dump(lista, archivo)
    archivo.close()
cantidadMisPokemones.set("Mis pokemones: " + str(len(guardados)))
if len(guardados) != 0:
    cambiarEstadoBoton(verMisPokemones, "normal")
#Main loop
ventanaPrincipal.mainloop()
