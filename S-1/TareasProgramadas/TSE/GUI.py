#Creado por: Gerardo López, Abraham Meza y Tribeth Rivas
#Fecha de creación: 6/6/18
#Última modificación: 14/6/18
#Versión: 3.6.5
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Certificaciones import *
from archivos import *
from Persona import *
import sys

#Definición de Clases
class Widgets:
    def crearBoton(self, objeto,metodo,nombre="Boton",coordenadas=(0,0),tamano=(0,0)):
        """
        Entradas: objeto de tipo obejto, metodo y nombre de tipo string y
        coordenadas junto con tamano de tipo tupla de enteros
        Salidas: Crea un botón y lo retorna
        Funcionamiento: Crea un botón en la ventana objeto, de nombre nombre,
        con las coordenadas y el tamaño dado, que llama al metodo metodo y lo
        retorna
        """
        boton = QPushButton(nombre, objeto)
        boton.move(coordenadas[0],coordenadas[1])
        boton.resize(tamano[0],tamano[1])
        exec("boton.clicked.connect(objeto."+metodo+")")
        return boton
    
    def crearEntrada(self, objeto,coordenadas=(0,0),tamano=(0,0)):
        """
        Entradas: objeto de tipo obejto, coordenadas y tamno de tipo tupla de
        enteros
        Salidas: Crea una caja de texto y la retorna 
        Funcionamiento: Crea una caja de texto en la ventana objeto, con las
        coordenadas y tamaño dado
        """
        Entrada = QLineEdit(objeto)
        Entrada.resize(tamano[0],tamano[1])
        Entrada.move(coordenadas[0],coordenadas[1])
        return Entrada

    def crearLabel(self, objeto,nombre="Label",coordenadas=(0,0),fuente=(None,10), tamano=(0,0)):
        """
        Entradas: objeto de tipo objeto, nombre de tipo string y coordenadas,
        fuente y tamano de tipo tupla de enteros
        Salidas: Crea y retorna un label
        Funcionamiento: Crea un label en la ventana objeto, con el texto nombre, en
        las coordenadas y con el tamaño y fuentes dados
        """
        Label = QLabel(nombre,objeto)
        Label.setFont(QFont(fuente[0],fuente[1]))
        Label.move(coordenadas[0],coordenadas[1])
        Label.resize(tamano[0], tamano[1])
        return Label

    def cambiarTextoLabel(self, label, texto):
        """
        Entradas: label de tipo QLabel y texto de tipo string
        Salidas: Cambia el texto del label y lo retorna
        Funcionamiento: Cambia el texto del Label por el dado y lo retorna
        """
        label.setText(texto)
        return label

    def cambiarColorVentana(self, ventana, color):
        """
        Entradas: ventana de tipo QMainWindow y color de tipo Qt
        Salidas: Modifica el color de la ventana
        Funcionamiento: Crea una paleta con el color dado y setea la paleta a
        la ventana
        """
        paleta = ventana.palette()
        paleta.setColor(ventana.backgroundRole(), color)
        ventana.setPalette(paleta)
        return ventana

    def cambiarColorBoton(self, boton, color):
        """
        Entradas: boton de tipo QPushButton y color de tipo string
        Salidas: Cambiar el color del botón y le pone un borde negro
        Funcionamiento: Setea un hoja de estilos para el botón que contiene
        el color dado junto con un borde negro
        """
        boton.setStyleSheet("background-color: " + color)
        boton.setStyleSheet("border: 1px solid black")
        return boton

    def crearListaDesplegable(self, objeto, lista, coordenadas = (0,0)):
        """
        Entradas: objeto tipo objeto, una lista de strings y coordenadas
        Salidas: Crea y retorna una lista desplegable
        Funcionamiento: Crea una lista desplegable donde cada opcion son los
        elementos de la lista
        """
        combo = QComboBox(self)
        for elem in lista:
            combo.addItem(str(elem))
        combo.resize(290,30)
        combo.move(coordenadas[0], coordenadas[1])
        return combo

    def crearRadioBoton(self, objeto, texto = '', coordenadas = (0,0)):
        btn = QRadioButton(objeto, text = texto)
        btn.move(coordenadas[0],coordenadas[1])
        return btn

class VentanaPrincipal(QMainWindow, Widgets):
    #Definicion de Atributos
    labelPersonas = None
    #Constructor
    def __init__(self, lista):
	    super().__init__()
	    self.setWindowTitle("Tribunal Supremo de Elecciones")
	    self.lista = lista
	    self.setGeometry(450, 250, 350, 310)
	    #Botones
	    self.botonRegistrar = self.crearBoton(self, "cambiarARegistrar", "Registrar Nacimiento", (110, 75), (150, 50))
	    self.botonGenealogico = self.crearBoton(self, "cambiarAGenealogico", "Mostrar Árbol Genealógico", (110, 135), (150, 50))
	    self.botonCertificado = self.crearBoton(self, "cambiarACertificado", "Certificado de Nacimiento", (110, 195), (150, 50))
	    self.botonSalir = self.crearBoton(self, "salir", "Salir", (110, 255), (150, 50))
	    #Labels
	    self.labelTitulo = self.crearLabel(self, "Tribunal Supremo de Elecciones", (10, 10), (None, 17), (350, 17))
	    self.labelPersonas = self.crearLabel(self, "Total de personas: 0", (210, 50), (None, 10), (150, 15))
	    self.setLabelPersonas(len(lista))
	    #Color de fondo
	    self = self.cambiarColorVentana(self, Qt.white)
	    self.botonRegistrar = self.cambiarColorBoton(self.botonRegistrar, "white")
	    self.botonGenealogico = self.cambiarColorBoton(self.botonGenealogico, "white")
	    self.botonCertificado = self.cambiarColorBoton(self.botonCertificado, "white")
	    self.botonSalir = self.cambiarColorBoton(self.botonSalir, "white")
	    #Icono
	    self.setWindowIcon(QtGui.QIcon("favicon.ico"))
            #Mostrar todo	    
	    self.show()

    def salir(self):
        """
        Entradas: N/A
        Salidas: Cierra la ventana
        Funcionamiento: Destuye la ventana
        """
        self.destroy()
        sys.exit(0)

    def cambiarACertificado(self):
        """
        Entradas: N/A
        Salidas: Cierra la ventana principal y abre la ventana de certificaciones
        Funcionamiento: Desruye la ventana principal y crea una ventana de
        busqueda de personas para las certificaciones de nacimiento
        """
        self.ventana = VentanaBusqueda(self.lista)
        self.ventana.show()
        self.destroy()

    def cambiarARegistrar(self):
        """
        Entradas: N/A
        Salidas: Cierra la ventana principal y abre la ventana de certificaciones
        Funcionamiento: Desruye la ventana principal y crea una ventana de
        registrar un nacimento
        """
        self.ventana = VentanaNuevaPersona(self.lista)
        self.ventana.show()
        self.destroy()

    def cambiarAGenealogico(self):
        """
        Entradas: N/A
        Salidas: Cierra la ventana principal y abre la ventana de árbol genealógico
        Funcionamiento: Desruye la ventana principal y crea una ventana de
        árbol genealógico
        """
        self.ventana = VentanaArbol(self.lista)
        self.ventana.show()
        self.destroy()

    def setLabelPersonas(self, cantidad):
        """
        Entradas: Cantidad de tipo entero
        Salidas: Cambia el texto de labelPersonas
        Funcionamiento: Cambia el texto de label personas por
        'Total de personas: X' donde X es la cantidad dada
        """
        self.labelPersonas = self.cambiarTextoLabel(self.labelPersonas, "Total de personas: " + str(cantidad))

class VentanaBusqueda(QWidget, Widgets):
    #Definicion de Atributos
    errorLabel = None
    cedulaEntrada1 = None
    cedulaEntrada2 = None
    cedulaEntrada3 = None
    nombreEntrada = None
    priApellidoEntrada = None
    segApellidoEntrada = None
    #Constructor 
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.title = 'Buscar persona'
        self.initUI()

    #Metodos
    def initUI(self):
        """
        Entradas: N/A
        Salidas: N/A
        Funcionamiento: Crea la ventana de busqueda de personas junto con sus respectivos botones, labels ,etc..
        """
        #Ventana
        self.setWindowTitle(self.title)
        self.setGeometry(700,400,550,285)
        #Labels
        self.busquedaCedLabel = self.crearLabel(self,"Búsqueda por # de cédula",(5,5),(None,15), (300, 25))
        self.busquedaNombreLabel = self.crearLabel(self,"Busqueda por nombres",(5,140),(None,15), (300, 25))
        self.cedLabel = self.crearLabel(self,"Cédula",(130,45),(None,15), (300, 25))
        self.cedEspacio1 = self.crearLabel(self,"-",(236,45),(None,15), (300, 25))
        self.cedEspacio2 = self.crearLabel(self,"-",(305,45),(None,15), (300, 25))
        self.nombreLabel = self.crearLabel(self,"Nombre",(45,175),(None,15), (300, 25))
        self.priApellidoLabel = self.crearLabel(self,"Primer Apellido",(210,175),(None,15), (300, 25))
        self.segApellidoLabel = self.crearLabel(self,"Segundo Apellido",(392,175),(None,15), (300, 25))
        #Error label
        self.errorLabel = self.crearLabel(self,"",(0,0),(None,6, (300, 25)))
        self.errorLabel.resize(350,25)
        self.errorLabel.setStyleSheet('color: red')
        #Cajas de entrada
        self.cedulaEntrada1 = self.crearEntrada(self,(205,45),(25,25))
        self.cedulaEntrada2 = self.crearEntrada(self,(250,45),(50,25))
        self.cedulaEntrada3 = self.crearEntrada(self,(320,45),(50,25))
        self.nombreEntrada = self.crearEntrada(self,(5,205),(150,25))
        self.priApellidoEntrada = self.crearEntrada(self,(200,205),(150,25))
        self.segApellidoEntrada = self.crearEntrada(self,(395,205),(150,25))
        #Botones
        self.botonBuscarCed = self.crearBoton(self,"BuscarCed","Buscar",(225,80),(100,30))
        self.botonBuscarNom = self.crearBoton(self,"BuscarNom","Buscar",(225,250),(100,30))
        self.botonRegresar = self.crearBoton(self, "regresar", "Regresar", (25, 250), (75, 30))
        #Icono
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        #Cambios de color
        self.cambiarColorVentana(self, Qt.white)
        self.botonBuscarCed = self.cambiarColorBoton(self.botonBuscarCed, "white")
        self.botonBuscarNom = self.cambiarColorBoton(self.botonBuscarNom, "white")
        self.botonRegresar = self.cambiarColorBoton(self.botonRegresar, "white")
        #Mostrar todo
        self.show()

    def regresar(self):
        """
        Entradas: N/A
        Salidas: Abre la ventana principal y cierra esta
        Funcionamiento: Instancia una ventana principal y destruye la ventana
        actual
        """
        self.ventana = VentanaPrincipal(self.lista)
        self.ventana.show()
        self.destroy()

    def BuscarCed(self):
        """
        Entradas: N/A
        Salidas: (class)Objeto persona si este existe
        Funcionamiento: Busca si una persona existe basado en su cédula, si la persona no existe informa de ello y si existe retorna el objeto persona
        """
        n1 = self.cedulaEntrada1.text()
        n2 = self.cedulaEntrada2.text()
        n3 = self.cedulaEntrada3.text()
        valCed = self.validarCedula(n1,n2,n3)
        self.errorLabel.move(5,123)
        if(valCed != None):
            self.errorLabel.setText(valCed)
            return
        cedula = n1 + "-" + n2 + "-" + n3
        for i in self.lista:
            if i.getCedula() == cedula:
                certificacion = Certificacion()
                certificacion.crearCertificacion(i)
                QMessageBox.question(self, "Certificado creado", "¡El certificado fue creado con exito!", QMessageBox.Ok)
                return self.regresar()
        self.errorLabel.setText("La persona buscada no existe")
        
    def BuscarNom(self):
        """
        Entradas: N/A
        Salidas: (class)Objeto persona si este existe
        Funcionamiento: Busca si una persona existe basado en su nombre, si la persona no existe informa de ello y si existe retorna el objeto persona
        """
        nom = self.nombreEntrada.text()
        apellido1 = self.priApellidoEntrada.text()
        apellido2 = self.segApellidoEntrada.text()
        valNom = self.validarNombre(nom,apellido1,apellido2)
        self.errorLabel.move(5,230)
        if(valNom != None):
            self.errorLabel.setText(valNom)
            return
        nombre = nom + " " + apellido1 + " " + apellido2
        for i in self.lista:
            if i.getNombre() == nombre:
                certificacion = Certificacion()
                certificacion.crearCertificacion(i)
                QMessageBox.question(self, "Certificado creado", "¡El certificado fue creado con exito!", QMessageBox.Ok)
                return self.regresar()
        self.errorLabel.setText("La persona buscada no existe")
        
    def validarCedula(self, n1,n2,n3):
        """
        Entradas: String(str) n1 representa el primer dígito de la cédula de una persona, n2 represeta a los consiguientes 4 dígitos y n3 representa a sus últimos 4 dígitos.
        Salidas: String(str), Nada(None) Si encuentra datos invalidos devuelve un mensaje indicando la falla de lo contrario retorna vacío.
        Funcionamiento: Analiza los posibles errores que puede tener una persona e informa de ellos.
        """
        if n1 == "" and n2 == "" and n3 == "":
            return "Debe rellanar todos los campos de la cédula"
        elif n1 == "":
            return "Debe rellanar el primer campo de la cédula"
        elif n2 == "":
            return "Debe rellanar el segundo campo de la cédula"
        elif n3 == "":
            return "Debe rellanar el tercer campo de la cédula"
        try:
            n1 = int(n1)
            int(n2)
            int(n3)
        except:
            return "Debe ingresar solo valores numéricos"
        if (n1<1 or n1>8):
            return "El primer digito debe ser entre 1 y 8"
        if(len(n2)!= 4 or len(n3)!= 4):
            return "EL segundo y tercer espacio deben tener un número de 4 cifras"
        
    def validarNombre(self,nom,apellido1,apellido2):  
        """
        Entradas: String(str) nom representa al nombre de la persona, apellido1 a su primer apellido y apellido2 a su segundo apellido.
        Salidas: String(str), Nada(None) Si encuentra datos invalidos devuelve un mensaje indicando la falla de lo contrario retorna vacío.
        Funcionamiento: Analiza los posibles errores que puede tener una persona e informa de ellos.
        """
        if nom == "" and apellido1 == "" and apellido2 == "":
            return "Debe rellanar todos los campos del nombre"
        elif nom == "":
            return "Debe rellanar el campo del nombre"
        elif apellido1 == "":
            return "Debe rellanar el campo del primer apellido"
        elif apellido2 == "":
            return "Debe rellanar el campo del segundo apellido"
        if not (nom.replace(" ","").isalpha() and apellido1.isalpha() and apellido2.isalpha()):
            return "Debe ingresar solo letras"
        if(len(nom)<3 or len(apellido1)<3 or len(apellido2)<3):
            return "El nombre y los apellidos deben tener al menos 3 letras"

class VentanaNuevaPersona(QMainWindow, Widgets):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista

        self.setWindowTitle("Registro de nacimiento")
        self.setGeometry(650,150,500,800)

        titulo = self.crearLabel(self, nombre="Datos Nueva Persona", coordenadas = (160,10), tamano = (210,15) )
        titulo.setStyleSheet("font-weight: bold")
        self.crearLabel(self, nombre = "Cita:", coordenadas = (30,50), tamano = (125,15))
        self.crearLabel(self, nombre = "-", coordenadas = (180,50), tamano = (125,15))
        self.crearLabel(self, nombre = "-", coordenadas = (245,50), tamano = (125,15))
        self.crearLabel(self, nombre = "Nombre:", coordenadas = (30,100), tamano = (125,15))
        self.crearLabel(self, nombre = "Apellidos:", coordenadas = (30,150), tamano = (125,20))
        self.crearLabel(self, nombre = "Sexo:", coordenadas = (30,200), tamano = (125,15))
        self.crearLabel(self, nombre = "Distrito:", coordenadas = (30,250), tamano = (125,15))
        self.crearLabel(self, nombre = "Cantón:", coordenadas = (30,300), tamano = (125,15))
        self.crearLabel(self, nombre = "Provincia:", coordenadas = (30,350), tamano = (125,15))
        self.crearLabel(self, nombre = "Día:", coordenadas = (30,400), tamano = (125,15))
        self.crearLabel(self, nombre = "Mes:", coordenadas = (30,450), tamano = (125,15))
        self.crearLabel(self, nombre = "Año:", coordenadas = (30,500), tamano = (125,15))
        self.crearLabel(self, nombre = "Padre:", coordenadas = (30,550), tamano = (125,15))
        self.crearLabel(self, nombre = "Nacionalidad:", coordenadas = (30,600), tamano = (125,15))
        self.crearLabel(self, nombre = "Madre:", coordenadas = (30,650), tamano = (125,15))
        self.crearLabel(self, nombre = "Nacionalidad:", coordenadas = (30,700), tamano = (125,15))
        
        self.errorLabel = self.crearLabel(self, nombre = "", coordenadas = (30,740), tamano = (2000, 30), fuente = (None,5))
        self.errorLabel.setStyleSheet('color: red')
        
        self.cita1 = self.crearEntrada(self, coordenadas = (150,50), tamano = (20,20))
        self.cita2 = self.crearEntrada(self, coordenadas = (200,50), tamano = (35,20))
        self.cita3 = self.crearEntrada(self, coordenadas = (265,50), tamano = (40,20))
        self.entradaNombre = self.crearEntrada(self, coordenadas = (150,100), tamano = (310,20))
        self.entradaApellido = self.crearEntrada(self, coordenadas = (150,150), tamano = (310,20))
        self.entradaDistrito = self.crearEntrada(self, coordenadas = (150,250), tamano = (310,20))
        self.entradaCanton = self.crearEntrada(self, coordenadas = (150,300), tamano = (310,20))
        self.entradaProvincia = self.crearEntrada(self, coordenadas = (150, 350), tamano = (310,20))
        self.cita1.textChanged.connect(self.actualizarProvincia)
        self.entradaProvincia.setReadOnly(True)
        
        self.sexoM = self.crearRadioBoton(self, texto = 'Hombre', coordenadas = (150,190))
        self.sexoF = self.crearRadioBoton(self, texto = 'Mujer', coordenadas = (300, 190))
        
        self.nacionalidades = ['-','Afgano','Alemán/a','Árabe','Argentino/a','Australiano/a','Belga','Boliviano/a','Brasileño/a','Camboyano/a','Canadiense','Chileno/a','Chino/a','Colombiano/a','Coreano/a','Costarricense','Cubano/a','Danés/a','Ecuatoriano/a','Egipcio/a','Salvadoreño/a','Escocés/a','Español/a','Estadounidense','Estonio/a','Etiope','Filipino','Finlandés/a','Francés/a','Galés/a','Griego/a','Guatemanteco/a','Haitiano/a','Holandés/a','Hondureño/a','Indonés/a','Inglés/a','Iraquí','Iraní','Irlandés/a','Israelí','Italiano/a','Japonés/a','Jordano/a','Laosiano/a','Letón/a','Malayo/a','Marroquí','Mexicano/a','Nicaragüense','Noruego/a','Neozelandés/a','Panameño/a','Paraguayo/a','Peruano/a','Polaco/a','Portugués/a','Puertorriqueño/a','Dominicano/a','Rumano/a','Ruso/a','Sueco/a','Suizo/a','Tailandés/a','Taiwanés/a','Turco/a','Ucraniano/a','Uruguayo/a','Venezolano/a','Vietnamita']
        calendario = [['-','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],['-','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],[]]
        for i in range(1899,int(time.strftime("%Y"))):
            calendario[2].append(str(i+1))
        calendario[2].append('-')
        calendario[2] = calendario[2][::-1]
        self.dias = self.crearListaDesplegable(self, calendario[0], coordenadas = (170,395))
        self.meses = self.crearListaDesplegable(self, calendario[1], coordenadas = (170,445))
        self.annos = self.crearListaDesplegable(self, calendario[2], coordenadas = (170,495))
        self.padre = self.crearListaDesplegable(self, self.registroPorGenero('M'), coordenadas = (170,545))
        self.madre = self.crearListaDesplegable(self, self.registroPorGenero('F'), coordenadas = (170,645))
        self.nacionalidadPadre = self.crearListaDesplegable(self,self.nacionalidades, coordenadas = (170,595))
        self.nacionalidadMadre = self.crearListaDesplegable(self,self.nacionalidades, coordenadas = (170,695))

        self.padre.currentIndexChanged.connect(self.pDesconocido)
        self.madre.currentIndexChanged.connect(self.mDesconocida)
        
        self.botonRegistrar = self.crearBoton(self, 'volver', nombre = 'Volver', coordenadas = (200,750),tamano = (100,30))
        self.botonRegresar = self.crearBoton(self, 'registrar', nombre = 'Registrar', coordenadas = (320,750),tamano = (100,30))
        #Icono
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        #Cambios de color
        self.cambiarColorVentana(self, Qt.white)
        self.botonRegistrar = self.cambiarColorBoton(self.botonRegistrar, "white")
        self.botonRegresar = self.cambiarColorBoton(self.botonRegresar, "white")
        self.dias = self.cambiarColorBoton(self.dias, "white")
        self.meses = self.cambiarColorBoton(self.meses, "white")
        self.annos = self.cambiarColorBoton(self.annos, "white")
        self.padre = self.cambiarColorBoton(self.padre, "white")
        self.madre = self.cambiarColorBoton(self.madre, "white")
        self.nacionalidadPadre = self.cambiarColorBoton(self.nacionalidadPadre, "white")
        self.nacionalidadMadre = self.cambiarColorBoton(self.nacionalidadMadre, "white")
        
        self.show()

    def pDesconocido(self):
        """
        Entradas: N/A
        Salidas: N/A
        Funcionalidad: Modifica el comboBox de la nacionalidad del padre.
        """
        if self.padre.currentText() == "--Se desconoce--":
            self.nacionalidadPadre.clear()
            self.nacionalidadPadre.addItems([self.tr("--Se desconoce--")])
        else:
            self.nacionalidadPadre.clear()
            self.nacionalidadPadre.addItems(self.nacionalidades)

    def mDesconocida(self):
        """
        Entradas: N/A
        Salidas: N/A
        Funcionalidad: Modifica el comboBox de la nacionalidad de la madre.
        """
        if self.madre.currentText() == "--Se desconoce--":
            self.nacionalidadMadre.clear()
            self.nacionalidadMadre.addItems([self.tr("--Se desconoce--")])
        else:
            self.nacionalidadMadre.clear()
            self.nacionalidadMadre.addItems(self.nacionalidades)

    def actualizarProvincia(self):
        """Pone el texto de la provincia automáticamente según la cédula
        llamando a la función self.obtenerProvincia"""
        self.entradaProvincia.setText(self.obtenerProvincia())
        
    def validaciones(self, lista):
        """Entradas: La lista con la información ingresada de una persona.
        Salidas: Un booleano
        Funcionalidad: Indica si la información ingresada cumple con las validaciones."""
        if lista[0] == 'n':
            self.errorLabel.setText("--- Error: Debe ingresar solo\n valores numéricos en la cédula ---")
            return False
        if lista[0] == 'l':
            self.errorLabel.setText("--- Error: Revise la cédula ---")
            return False
        if not (lista[1] and lista[2] and lista[3] and lista[4] and lista[5]):
            self.errorLabel.setText("--- Error: Debe rellenar todos\n los campos ---")
            return False
        if not (self.palabras(lista[1]) and self.palabras(lista[2]) and self.palabras(lista[4]) and self.palabras(lista[5])):
            self.errorLabel.setText("--- Error: Use solo letras para\n nombres y apellidos ---")
            return False
        for elem in lista[7:]:
            if elem == '-':
                self.errorLabel.setText("--- Error: Debe rellenar todos\n los campos ---")
                return False
        if not self.existeFecha(lista[7:10]):
            self.errorLabel.setText("--- Error: La fecha que ingresó\nno existe ---")
            return False
        if not " " in lista[2]:
            self.errorLabel.setText("--- Error: Debe ingresar al menos\ndos apellidos ---")
            return False
        return True

    def obtenerCedula(self):
        """Toma las partes ingresadas de la cédula y las une con guiones
        si cumplen con el formato de una cédula para retornarlas unidas.
        Retorna una letra l si se ingresan carácteres no numéricos o una
        letra n se ingresa una mayor o menor cantidad de carácteres de
        los que conforman una cédula."""
        c1 = self.cita1.text()
        c2 = self.cita2.text()
        c3 = self.cita3.text()
        if not (c1.isnumeric() and c2.isnumeric() and c3.isnumeric()):
            return 'n'
        if len(c1)!=1:
            return 'l'
        if len(c2) != 3 and len(c2) != 4:
            return 'l'
        if len(c3) != 3 and len(c3) != 4:
            return 'l'
        if len(c2) == 3:
            c2 = '0'+c2
        if len(c3) == 3:
            c3 = '0'+c3
        return c1+'-'+c2+'-'+c3

    def obtenerProvincia(self):
        """Dependiendo del primer caracter ingresado en la cédula
        asigna automáticamente la provincia de nacimiento"""
        t = self.cita1.text()
        if t == '1':
            return "San José"
        if t == '2':
            return "Alajuela"
        if t == '3':
            return "Cartago"
        if t == '4':
            return "Heredia"
        if t == '5':
            return "Guanacaste"
        if t == '6':
            return "Puntarenas"
        if t == '7':
            return "Limón"
        if t == '8':
            return "PEN"
        if t == '9':
            return "Nacionalizado"
        return ''

    def registroPorGenero(self, g):
        """Entradas: String "F" o "M"
        Retorna una lista de las personas guardadas que sean del género g"""
        retorno = ['-',"--Se desconoce--"]
        try:
            for elem in Archivo("Poblacion").leerBinario():
                if elem.getSexo() == g:
                    padre = elem.getCedula() + " " + elem.getNombre()
                    retorno.append(padre)
        except:
            pass
        return retorno
        
    def registrar(self):
        """Toma los datos ingresados por el usuario y crea una persona
        con esa información si esta cumple con las validaciones. En cualquier
        otro caso el programa no hace nada"""
        cedula = self.obtenerCedula()
        nombre = self.entradaNombre.text()
        apellido = self.entradaApellido.text()
        sexo = 'Masculino' if self.sexoM.isChecked() else ('Femenino' if self.sexoF.isChecked() else '')
        distrito = self.entradaDistrito.text()
        canton = self.entradaCanton.text()
        provincia = self.obtenerProvincia()
        dia = self.dias.currentText()
        mes = self.meses.currentText()
        anno = self.annos.currentText()
        nacPadre = self.nacionalidadPadre.currentText()
        pa = self.padre.currentText()
        ma = self.madre.currentText()
        nacMadre = self.nacionalidadMadre.currentText()
        info = [cedula, nombre, apellido, sexo, distrito, canton, provincia, dia, mes, anno, pa, nacPadre, ma, nacMadre]
        if not self.validaciones(info):
            return
        nuevoCiudadano = Persona()
        nuevoCiudadano.setCedula(cedula)
        nuevoCiudadano.setNombre(nombre + " " + apellido)
        nuevoCiudadano.setSexo(sexo)
        nuevoCiudadano.setUbicacion(provincia+' '+canton+' '+distrito)
        nuevoCiudadano.setFechanacimiento(dia+'/'+mes+'/'+anno)
        nuevoCiudadano.setPadre(pa)
        nuevoCiudadano.setNacionalidadpadre(nacPadre)
        nuevoCiudadano.setMadre(ma)
        nuevoCiudadano.setNacionalidadmadre(nacMadre)
        self.lista += [nuevoCiudadano]
        archivo = Archivo("Poblacion")
        archivo.guardarBinario(self.lista)
        QMessageBox.question(self, "Persona registrada", "¡La persona fue registrada con exito!", QMessageBox.Ok)
        return self.volver()

    def volver(self):
        """
        Entradas: N/A
        Salidas: Abre la ventana principal y cierra esta
        Funcionamiento: Instancia una ventana principal y destruye la ventana
        actual
        """
        self.ventana = VentanaPrincipal(self.lista)
        self.ventana.show()
        self.destroy()

    def palabras(self, p):
        """Se le ingresa un string p, e indica si es de una o varias palabras
        con carácteres alphabeticos."""
        for elem in p.split():
            if not elem.isalpha():
                return False
        return True     
    
    def divisible(self, n1, n2):
        """
        Entradas: Dos intigers
        Salidas: Un booleano.
        Funcionalidad: Indica s n1 es divisible por n2
        """
        if n1%n2 == 0:
            return True
        return False

    def annoBisiesto(self, a):
        """
        Entradas: Un año como int
        Salidas: Un booleano
        Funcionalidad: Detecta si un año es bisiesto o no
        """
        if self.divisible(a,4) and ((not self.divisible(a,100)) or self.divisible(a,400)):
            return True
        return False

    def existeFecha(self, lista):
        """
        Entradas: Una fecha como lista en formato [d, m, a]
        Salidas: Un booleano
        Funcionalidad: Detecta si una fecha existe o no
        """
        dia = lista[0]
        mes = lista[1]
        anno = lista[2] 
        if mes == '2':
            if int(dia)>29 or (dia == '29' and not self.annoBisiesto(int(anno))):
                return False
        if (mes == '4' or mes == '6' or mes == '9' or mes == '11') and dia == '31':
            return False
        return True

class VentanaArbol(QMainWindow, Widgets):
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        
        self.setWindowTitle("Árbol genealógico")
        self.setGeometry(650,150,600,400)

        titulo = self.crearLabel(self, nombre = "Mostrar Árbol Genealógico", coordenadas = (190,10), tamano = (300, 25))
        titulo.setStyleSheet("font-weight: bold")
        self.crearLabel(self, nombre = "Persona:", coordenadas = (30,50), tamano = (100, 15))
        self.crearLabel(self, nombre = "Resultados de la búsqueda:", coordenadas = (30,160), tamano = (250,25))
        self.labelPadre = self.crearLabel(self, nombre= "-", fuente = (None, 5), coordenadas = (105,195), tamano = (150,50))
        self.labelMadre = self.crearLabel(self, nombre= "-", fuente = (None, 5), coordenadas = (355,195), tamano = (150,50))
        self.labelPersona = self.crearLabel(self, nombre= "-", fuente = (None, 5), coordenadas = (230,285), tamano = (150,50))

        self.labelError = self.crearLabel(self, nombre = "", fuente = (None,5), coordenadas = (50,80), tamano = (150,50))
        self.labelError.setStyleSheet('color: red')
        
        self.botonMostrar = self.crearBoton(self, 'mostrar', nombre = 'Mostrar', coordenadas = (170, 90), tamano = (100, 50))
        self.botonLimpiar = self.crearBoton(self, 'limpiar', nombre = 'Limpiar', coordenadas = (280, 90), tamano = (100, 50))
        self.botonRegresar = self.crearBoton(self, 'volver', nombre = 'Volver', coordenadas = (390, 90), tamano = (100, 50))

        self.persona = self.crearListaDesplegable(self, self.obtenerPersonas(), coordenadas = (170, 45))
        #Icono
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        #Cambios de color
        self.cambiarColorVentana(self, Qt.white)
        self.persona = self.cambiarColorBoton(self.persona, "white")
        self.botonMostrar = self.cambiarColorBoton(self.botonMostrar, "white")
        self.botonLimpiar = self.cambiarColorBoton(self.botonLimpiar, "white")
        self.botonRegresar = self.cambiarColorBoton(self.botonRegresar, "white")
        
        self.show()
        
    def paintEvent(self, e):
        """Se activa automáticamente para dibujar líneas y rectángulos en la ventana"""
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.drawRect(100,200,150,40)
        painter.drawRect(350,200,150,40)
        painter.drawRect(225,290,150,40)
        painter.drawLine(190,240,250,290)
        painter.drawLine(410,240,350,290)
                
    
    def obtenerPersonas(self):
        """Retorna una lista con los nombre y cédulas de las personas registradas."""
        retorno = ['-']
        for elem in self.lista:
            nombre = elem.getNombre()
            nombre = elem.getCedula()+" "+nombre
            retorno.append(nombre)
        return retorno
    
    def volver(self):
        """Destruye la ventana actual y regresa a la anterior"""
        self.ventana = VentanaPrincipal(self.lista)
        self.destroy()

    def acomodarNombre(self, lista):
        """Dado un string al que se le haya realizado un split
        retorna el mismo string con un line break después de la
        segunda palabra"""
        p1 = ""
        p2 = ""
        for elem in lista[:2]:
            p1 += elem + " "
        for elem in lista[2:]:
            p2 += elem + " "
        return p1 + "\n" + p2
    
    def mostrar(self):
        """Según la opción seleccionada por el usuario se muestra el
        nombre del padre, madre y de la misma persona"""
        ced = self.persona.currentText().split()[0]
        for elem in Archivo("Poblacion").leerBinario():
            if ced == elem.getCedula():
                a = elem.getNombre().split()
                p = elem.getPadre().split()[1:] if elem.getPadre() != "--Se desconoce--" else elem.getPadre().split()
                m = elem.getMadre().split()[1:] if elem.getMadre() != "--Se desconoce--" else elem.getMadre().split()
                self.labelPersona.setText(self.acomodarNombre(a))
                self.labelPadre.setText(self.acomodarNombre(p))
                self.labelMadre.setText(self.acomodarNombre(m))
                self.labelError.setText("")
                return
        self.labelError.setText("--Error, seleccione\nalguna persona---")
                        

    def limpiar(self):
        """Resetea todos los labels"""
        self.labelPersona.setText("-")
        self.labelPadre.setText("-")
        self.labelMadre.setText("-")
        self.labelError.setText("")
        
