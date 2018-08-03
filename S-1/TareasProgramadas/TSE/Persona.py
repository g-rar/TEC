#Creado por: Gerardo López, Abraham Meza y Tribeth Rivas
#Fecha de creación: 6/6/18
#Última modificación: 6/6/18
#Versión: 3.6.5

#Definición de clases
class Persona:
    cedula = ""
    nombre = ""
    sexo = ""
    ubicacion = ""
    fechaNacimiento = ""
    padre = ""
    nacionalidadPadre = ""
    madre = ""
    nacionalidadMadre = ""

    #Inicializador
    def __init__(self):
        self.cedula = ""
        self.nombre = ""
        self.sexo = ""
        self.ubicacion = ""
        self.fechaNacimiento = ""
        self.padre = ""
        self.nacionalidadPadre = ""
        self.madre = ""
        self.nacionalidadMadre = ""

    #Getters y Setters
    def getCedula(self):
        return self.cedula
    def setCedula(self,vcedula):
        self.cedula = vcedula
    def getNombre(self):
        return self.nombre
    def setNombre(self,vnombre):
        self.nombre = vnombre
    def getSexo(self):
        return self.sexo
    def setSexo(self,vsexo):
        self.sexo = vsexo
    def getUbicacion(self):
        return self.ubicacion
    def setUbicacion(self,vubicacion):
        self.ubicacion = vubicacion
    def getFechanacimiento(self):
        return self.fechaNacimiento
    def setFechanacimiento(self,vfechaNacimiento):
        self.fechaNacimiento = vfechaNacimiento
    def getPadre(self):
        return self.padre
    def setPadre(self,vpadre):
        self.padre = vpadre
    def getNacionalidadpadre(self):
        return self.nacionalidadPadre
    def setNacionalidadpadre(self,vnacionalidadPadre):
        self.nacionalidadPadre = vnacionalidadPadre
    def getMadre(self):
        return self.madre
    def setMadre(self,vmadre):
        self.madre = vmadre
    def getNacionalidadmadre(self):
        return self.nacionalidadMadre
    def setNacionalidadmadre(self,vnacionalidadMadre):
        self.nacionalidadMadre = vnacionalidadMadre

    #Funcion de mostrar todos los atributos 
    def mostrar(self):
        yield self.cedula
        yield self.nombre
        yield self.sexo
        yield self.ubicacion
        yield self.fechaNacimiento
        yield self.padre
        yield self.nacionalidadPadre
        yield self.madre
        yield self.nacionalidadMadre

