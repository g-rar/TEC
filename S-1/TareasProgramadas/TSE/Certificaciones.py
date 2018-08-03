#Creado por: Gerardo López, Abraham Meza, Tribeth Rivas
#Fecha de creación: 7/6/18
#Última modificación: 7/6/18
#Versión 3.6.5
from Persona import *
from archivos import *
import time

class Certificacion:
    #Constructor
    def __init__(self):
        self.persona = Persona()
    #Metodos
    def formatearFecha(self):
        """
        Entradas: N/A
        Salidas: Fecha y hora con formato numerico
        Funcionamiento: Obtiene la fecha y hora actual y si el día es de un
        solo dígito se le agrega un 0 al inicio; además se reemplaza el mes
        por su valor númerico
        """
        fecha = time.asctime().split()
        fecha[2] = fecha[2] = "0"+fecha[2] if len(fecha[2]) == 1 else fecha[2]
        meses = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        fecha[1] = str(meses.index(fecha[1])+1)
        fecha[1] = "0"+fecha[1] if len(fecha[1])==1 else fecha[1]
        return fecha

    
    def crearCertificacion(self, persona):
        """
        Entradas: persona de tipo Persona
        Salidas: Crea un archivo HTML de la certificación de nacimiento
        Funcionamiento: Crea un archivo con el nombre:
        'Analisis-dd-mm-aaaa-hh-mm-ss.hmtl' en donde está contenido el código
        generado por generarHTML
        """
        fecha = self.formatearFecha()
        archivo = Archivo("Analisis-" + fecha[2] + "-" + fecha[1] + "-" + fecha[4] + "-" + fecha[3][:2] + "-" + fecha[3][3:5] + "-" + fecha[3][6:] + ".html")
        archivo.escribirTexto(self.generarHTML(persona))
        return

    def corregirAcentos(self, persona):
        acentos = {"Á":"&Aacute;", "Ä":"&Auml;", "É":"&Eacute;", "Í":"&Iacute;", "Ñ":"&Ntilde;", "Ó":"&Oacute;", "Ú":"&Uacute;", "Ü":"&Uuml;", "á":"&aacute;", "ä":"&auml;", "é":"&eacute;", "í":"&iacute;", "ñ":"&ntilde;", "ó":"&oacute;", "ú":"&uacute;", "ü":"&uuml;"}
        for i in persona.getNombre():
            if i in acentos:
                persona.setNombre(persona.getNombre().replace(i, acentos[i]))
        for i in persona.getUbicacion():
            if i in acentos:
                persona.setUbicacion(persona.getUbicacion().replace(i, acentos[i]))
        for i in persona.getPadre():
            if i in acentos:
                persona.setPadre(persona.getPadre().replace(i, acentos[i]))
        for i in persona.getMadre():
            if i in acentos:
                persona.setMadre(persona.getMadre().replace(i, acentos[i]))
        for i in persona.getNacionalidadpadre():
            if i in acentos:
                persona.setNacionalidadpadre(persona.getNacionalidadpadre().replace(i, acentos[i]))
        for i in persona.getNacionalidadmadre():
            if i in acentos:
                persona.setNacionalidadmadre(persona.getNacionalidadmadre().replace(i, acentos[i]))
        return persona
    
    def generarHTML(self, persona):
        """
        Entradas: Persona de tipo Persona
        Salidas: Archivo HTML con los datos de la persona
        Funcionamiento: Crea un Archivo HTML con los archivos de la persona y lo
        retorna
        """
        persona = self.corregirAcentos(persona)
        codigo = "<!DOCTYPE html>\n"\
               + "<html>\n"\
               + "  <head>\n"\
               + "    <title>Certificado de Nacimiento</title>\n"\
               + "    <meta charset = 'UTF-8'>\n"\
               + "    <style>\n"\
               + "      table{\n"\
               + "        border-collapse: collapse;\n"\
               + "        width: 500px;\n"\
               + "        text-align: center;\n"\
               + "      }\n"\
               + "      .dato{\n"\
               + "        text-align: left;\n"\
               + "      }\n"\
               + "      .negrita{\n"\
               + "        font-weight: bold;\n"\
               + "      }\n"\
               + "    </style>\n"\
               + "  </head>\n"\
               + "  <body>\n"\
               + "    <table border = '1'>\n"\
               + "      <tr>\n"\
               + "        <td colspan = '2'>\n"\
               + "          <strong>Certificado de Nacimiento</strong>\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Al tomo:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getCedula()[2:6] + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Asiento:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getCedula()[-4:] + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Cita:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getCedula() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Dice que:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getNombre() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Sexo:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getSexo() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Naci&oacute; en:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getUbicacion() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          El d&iacute;a:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getFechanacimiento() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Padre:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getPadre() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Nacionalidad:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getNacionalidadpadre() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Madre:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getMadre() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "      <tr>\n"\
               + "        <td class = 'negrita'>\n"\
               + "          Nacionalidad:\n"\
               + "        </td>\n"\
               + "        <td class = 'dato'>\n"\
               + "          " + persona.getNacionalidadmadre() + "\n"\
               + "        </td>\n"\
               + "      </tr>\n"\
               + "    </table>\n"\
               + "  </body>\n"\
               + "</html>"
        return codigo
