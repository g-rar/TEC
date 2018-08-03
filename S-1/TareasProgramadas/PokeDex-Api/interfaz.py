#Creado por: Abraham Meza, Gerardo López y Tribeth Rivas
#Fecha de creación: 10/5/18
#Última modificación: 19/5/18 por Gerardo
#Versión: 3.6.5
from tkinter import *
from tkinter import messagebox
from PokeApi import *

#Definición de funciones
def modificarVentana(ventana, nombre, alto, ancho):
    """
    Entradas: ventana de tipo Tk, nombre de tipo string y alto y ancho de tipo
        entero
    Salidas: Modifica los datos de una ventana
    Funcionamiento: A la ventana que se pasó se le pone el nombre que se pasa y
        se le dan las dimensiones dadas por alto y ancho
    """
    ventana.title(nombre)
    ventana.geometry(ancho+"x"+alto)
    ventana.resizable(False, False)
    return

def cambiarNombreBoton(boton,nombre):
    """
    Entradas: boton de tipo widget y nombre de tipo strin
    Salidas: Se cambia el texto de un boton
    Funcionamiento: Se cambia el texto que muestra el boton por el que se le
        pasó
    """
    boton["text"] = nombre
    return

def destruirVentana(ventana):
    """
    Entradas: ventana de tipo Tk
    Salidas: cierra una ventana
    Funcionamiento: Cierra la ventana que se le pasó por parametro
    """
    ventana.destroy()
    return

def crearLabel(texto, tamannoFuente, x, y, ventanaPadre, textoVariable = None):
    """
    Entradas: texto de tipos string, tamannoFuente, x, e y de tipo entero, junto
        con ventanaPadre de tipo Tk
    Salidas: Retorna un label
    Funcionamiento: Crea un label con el texto y el tamaño de la fuente dada y
        los posiciona en la coordenadas y ventana pasados.
    """
    label = Label(ventanaPadre, text = texto, font = (None, tamannoFuente), textvariable = textoVariable)
    label.place(x = x, y = y)
    return label

def crearCajaTexto(ancho, x, y, ventanaPadre, mostrar = None):
    """
    Entradas: ancho, x e y de tipo entero
    Salidas: Retorna una caja de texto
    Funcionamiento: Crea una caja de texto y la posiciona en la coordenadas dadas
    """
    cajaTexto = Entry(ventanaPadre, width = ancho, show = mostrar)
    cajaTexto.place(x = x, y = y)
    return cajaTexto

def crearBoton(texto, largo, ancho, x, y, ventanaPadre, funcion = None, estado = "normal"):
    """
    Entradas: texto de tipo string, largo ancho, x, e y de tipo entero, una
        función y ventanaPadre de tipo Tk
    Salidas: Retorna un boton
    Funcionamiento: Crea un boton y lo posiciona en las coordenadas y la ventana
        pasadas
    """
    boton = Button(ventanaPadre, text = texto, height = largo, width = ancho, state = estado, command = funcion)
    boton.place(x = x, y = y)
    return boton

def cambiarEstadoBoton(boton, estado):
    """
    Entradas: boton de tipo widget y estados de tipo string
    Salidas: Boton habilitado/inhabilitado
    Funcionamiento: Asigna estado dado al boton pasado
    """
    boton.config(state = estado)
    return

def mostrarPokemon(num, pokemones):
    """
    Entradas: El número del index y la lista de pokemones
    Salidas: Una ventana
    Funcionamiento: Crea la ventana en la que se muestra la información
        del pokemon. Tiene un botón que destruye ésta ventana.
    """
    dialogo = Toplevel()
    modificarVentana(dialogo, "Información del pokémon", '300', '300')
    fondo = Canvas(dialogo, width = 300, height = 300)
    descargarImagen(pokemones[num][3][0])
    fondo.create_rectangle(30,10,270,120)
    fondo.create_rectangle(30,130,145,165)
    fondo.create_rectangle(155,130,270,165)
    fondo.create_rectangle(30,175,145,210)
    fondo.create_rectangle(155,175,270,210)
    imagen = cargarImagen("pokemon.gif")
    fondo.create_image(40,20, anchor = NW, image = imagen)
    borrarImagen("pokemon.gif")
    nombre = crearLabel(pokemones[num][1].title(), 13, 155, 53, dialogo)
    tPeso = crearLabel("Peso:", 10, 69, 137, dialogo)
    tAltura = crearLabel("Altura:",10,69,182,dialogo)
    peso = crearLabel(pokemones[num][3][1], 11, 194, 137, dialogo)
    altura = crearLabel(pokemones[num][3][2], 11, 194, 182, dialogo)
    regresar = crearBoton("Regresar", 2, 33, 30, 220, dialogo, lambda: destruirVentana(dialogo))
    fondo.place(x  = 0, y = 0)
    dialogo.mainloop()

def cargarImagen(nombre):
    """
    Entradas: El nombre de la imagen .gif
    Salidas: Un objeto tipo PhotoImage
    Funcionamiento: Carga la imagen desde el equipo
    """
    ruta = os.path.join(nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

def borrarImagen(nombre):
    """
    Entradas: El nombre del archivo a borrar
    Salidas: N/A
    Funcionamiento: Borra la imagen
    """
    os.remove(nombre)

def misPokemones(pokemones):
    """
    Entradas: Una lista de los pokemones guardados
    Salidas: Una ventana que los muestra
    Funcionamiento: Hace una ventana que permite ver la información de
        los pokemones guardados. La información en sí la muestra la
        función miPokemon
    """
    global dialogoMP, atrasMP, siguienteMP, textoPesoMP, textoNombreMP, textoAlturaMP, labelImagen, indexInterno, fondoMP
    indexInterno = 0
    dialogoMP = Toplevel()
    modificarVentana(dialogoMP, "Información del pokémon", '300', '300')
    #Texto de labels
    textoNombreMP = StringVar()
    textoPesoMP = StringVar()
    textoAlturaMP = StringVar()
    #Canvas
    fondoMP = Canvas(dialogoMP, width = 300, height = 300)
    fondoMP.create_rectangle(30,10,270,120)
    fondoMP.create_rectangle(30,130,145,165)
    fondoMP.create_rectangle(155,130,270,165)
    fondoMP.create_rectangle(30,175,145,210)
    fondoMP.create_rectangle(155,175,270,210)
    #Labels
    tPesoMP = crearLabel("Peso:", 10, 69, 137, dialogoMP)
    tAlturaMP = crearLabel("Altura:", 10, 69, 182, dialogoMP)
    nombreMP = crearLabel("", 13, 155, 53, dialogoMP, textoNombreMP)
    pesoMP = crearLabel("", 11, 194, 137, dialogoMP, textoPesoMP)
    alturaMP = crearLabel("", 11, 194, 182, dialogoMP, textoAlturaMP)
    labelImagen = Label(dialogoMP, image = None)
    labelImagen.place(x  = 40, y = 20)
    fondoMP.place(x  = 0, y = 0)
    #Botones
    regresarMP = crearBoton("Regresar", 2, 10, 110, 220, dialogoMP, lambda: destruirVentana(dialogoMP))
    atrasMP = crearBoton("Atras", 2, 10, 25, 220, dialogoMP, lambda: opcionAtrasMisPokemones(pokemones), estado = DISABLED)
    siguienteMP = crearBoton("Siguiente", 2, 10, 195, 220, dialogoMP, lambda: opcionSiguienteMisPokemones(pokemones))
    #Ejecución, mainloop
    miPokemon(pokemones)
    return
    

def opcionSiguienteMisPokemones(pokemones):
    """
    Entradas: La lista de los pokemones guardados
    Salidas: N/A
    Funcionamiento: Incrementa el indexInterno en uno y llama a
        la función miPokemon con la lista para actualizar la información
    """
    global indexInterno
    indexInterno += 1
    miPokemon(pokemones)

def opcionAtrasMisPokemones(pokemones):
    """
    Entradas: La lista de los pokemones guardados
    Salidas: N/A
    Funcionamiento: Decrementa el indexInterno en uno y llama a
        la función miPokemon con la lista para actualizar la información
    """
    global indexInterno
    indexInterno -= 1
    miPokemon(pokemones)

def miPokemon(pokemones):
    """
    Entradas: La lista de pokemones guardados
    Salidas: Actualiza la ventana misPokemones
    Funcionamiento: Actualiza la ventana misPokemones con toda la
        información del pokemon en el indexInterno, junto con el 
        estado de los botones de ser necesario.
    """
    global atrasMP, siguienteMP, textoPesoMP, textoNombreMP, textoAlturaMP, labelImagen, indexInterno, fondoMP
    descargarImagen(pokemones[indexInterno][3][0])
    imagen = cargarImagen("pokemon.gif")
    labelImagen.config(image = imagen)
    borrarImagen("pokemon.gif")
    dialogoMP.update()
    textoNombreMP.set(str(pokemones[indexInterno][1]).title())
    textoPesoMP.set(str(pokemones[indexInterno][3][1]))
    textoAlturaMP.set(str(pokemones[indexInterno][3][2]))
    if len(pokemones)== indexInterno+1:
        cambiarEstadoBoton(siguienteMP, estado = DISABLED)
    elif len(pokemones) >= indexInterno:
        cambiarEstadoBoton(siguienteMP, estado = 'normal')
    if indexInterno == 0:
        cambiarEstadoBoton(atrasMP, estado = DISABLED)
    elif indexInterno != 0:
        cambiarEstadoBoton(atrasMP, estado = 'normal')
    dialogoMP.mainloop()
    return
