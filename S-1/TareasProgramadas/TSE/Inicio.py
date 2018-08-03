#Creado por: Gerardo López, Abraham Meza y Tribeth Rivas
#Fecha de creación: 6/6/18
#Última modificación: 14/6/18
#Versión: 3.6.5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from GUI import *
from archivos import *

class Inicio(QWidget, Widgets):
    #Esta clase crea un objeto de tipo inicio el cual tiene una opción de ingresar nombre y usuario para buscar
    def __init__(self, lista):
        super().__init__()
        self.lista = lista
        self.title = 'Inicio'
        self.initUI()

    def initUI(self):
        """
        Función: Inicializa la ventana.
        Entradas: N/A
        Salidas: N/A
        """
        #Ventana
        self.setWindowTitle(self.title)
        self.setGeometry(700,400,400,190)
        #Labels
        self.usuarioLabel = self.crearLabel(self,"Usuario",(5,20),(None,15), (300, 20))
        self.contrasennaLabel = self.crearLabel(self,"Contraseña",(5,85),(None,15), (300, 20))
        #Error label
        self.errorLabel = self.crearLabel(self,"",(5,120),(None,6))
        self.errorLabel.resize(350,25)
        self.errorLabel.setStyleSheet('color: red')
        #Cajas de texto
        self.usuarioEntrada = self.crearEntrada(self,(150,20),(225,25))
        self.contrasennaEntrada = self.crearEntrada(self,(150,85),(225,25))
        self.contrasennaEntrada.setEchoMode(QLineEdit.Password)
        #Botones
        self.botonIngresar = self.crearBoton(self,"ingresar","Ingresar",(50,150),(100,30))
        self.botonLimpiar = self.crearBoton(self,"limpiar","Limpiar",(250,150),(100,30))
        #Icono
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        #Cambio de colores
        self.cambiarColorVentana(self, Qt.white)
        self.botonIngresar = self.cambiarColorBoton(self.botonIngresar, "white")
        self.botonLimpiar = self.cambiarColorBoton(self.botonLimpiar, "white")
        #Mostrar
        self.show()
 
    def ingresar(self):
        """
        Función: Revisa si la contraseña es válida y que el usuario tenga formato de correo
        Entradas: N/A
        Salidas: N/A
        """
        val = self.validarContrasenna(self.contrasennaEntrada.text())
        if(not self.validarUsuario(self.usuarioEntrada.text())):
            self.errorLabel.setText("El usuario debe tener formato de correo electronico")
            return
        elif(val != "a"):
            self.errorLabel.setText(val)
            return
        self.buscar()

    def buscar(self):
        """
        Entradas: N/A
        Salidas: Entra a la ventana principal o marca error
        Funcionamiento: Guarda lo que hay en user.txt y verifica si lo ingresado
        en usuario y contraseña conincide con algún usuario registrado, de ser
        así pasa a la ventana principal. De lo contrario, marca el debido error
        """
        archivo = Archivo("users.txt")
        usuarios = archivo.leerTexto().split("\n")
        login = self.usuarioEntrada.text() + "    " + self.contrasennaEntrada.text()
        if login in usuarios:
            self.ventana = VentanaPrincipal(self.lista)
            self.ventana.show()
            self.destroy()
        else:
            for usuario in usuarios:
                if self.usuarioEntrada.text() == usuario[:usuario.index(" ")]:
                    self.errorLabel.setText("Contraseña incorrecta")
                    return
            self.errorLabel.setText("El usuario no existe")
    
    def limpiar(self):
        """
        Función: Busca los espacios de entrada para usuario y contraseña y elimina todo en su interior
        Entradas: N/A
        Salidas: N/A
        """
        self.usuarioEntrada.setText("")
        self.contrasennaEntrada.setText("")

    def validarUsuario(self, texto):
        """
        Función: Valida si el usuario tiene formato de correo electrónico
        Entradas: string(str) el texto a analizar
        Salidas: Booleano(bool) True si tiene formato de correo electronico False si no
        """
        return "." in texto[:-2] and "@" in texto[1:]

    def validarContrasenna(self, texto):
        """
        Función: Valida si la contraseña tiene entre 5 y 15 caractéres, y que tenga al menos una letra y un número
        Entradas: string(str) el texto a analizar
        Salidas: String(str) Devuelve los respectivos avisos en caso de que se manifieste el error o "a" en caso de que todo esté correctamente
        """
        text = False
        num = False
        if(len(texto)>4 and len(texto)<16):
            for i in texto:
                if(i.isalpha()):
                    text = True
                if(i.isdigit()):
                    num = True
                if(text and num):
                    return "a"
            if(text):
                return "La contraseña debe tener al menos 1 número"
            if(num):
                return "La contraseña debe tener al menos 1 letra"
        return "La contraseña debe tener entre 5 y 15 caracteres"