#Elaborado por: Geraro López Calderón, Abraham y Triveth.
#Fecha de creación: 14/5/2018
#Última modificación: 14/5/2018
#Versión: 3.6.4
import smtplib
from XML import *

def enviarXML(usuario, contrasenna, pokemones):
    """
    Entradas: usuario y contraseña de tipo string y pokemones de tipo matriz
    Salidas: mensaje a enviar
    Funcionamiento: Crea un XML con todos los pokemones guardados y llama a
        enviarCorreo
    """
    xml = ""
    for i in range(len(pokemones)):
        xml += PokemonXML(pokemones[i])
    return enviarCorreo(usuario, contrasenna, PokemonesXML(xml))

def enviarCorreo(correo, contrasenna, mensaje):
    """
    Entradas: mensaje, contraseña y correo de tipo string
    Salidas: Mensaje de confirmación/error del envio del correo
    Funcionamiento: Envia un correo a la dirección dada con el mensaje dado
    """
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.ehlo()
        servidor.login(correo, contrasenna)
        servidor.sendmail(correo, correo, mensaje + "\n")
        servidor.quit()
        return "¡Correo enviado con exito!"
    except smtplib.SMTPServerDisconnected:
        return "Error: Se perdio la conexión con el servidor"
    except smtplib.SMTPResponseException:
        return "Error del servidor"
    except smtplib.SMTPSenderRefused:
        return "Error: Se ha rechazado al remitente"
    except smtplib.SMTPRecipientsRefused:
        return "Error: Se rechazado el destinatario"
    except smtplib.SMTPDataError:
        return "Error: El servidor ha rechazado el mensaje"
    except smtplib.SMTPConnectError:
        return "Error: Al conectar con el servidor"
    except smtplib.SMTPHeloError:
        return "Error: Se rechazado el saludo al servidor"
    except smtplib.SMTPNotSupportedError:
        return "Error: La operación no es soportada por el servidor"
    except smtplib.SMTPAuthenticationError:
        return "Error: Usuario/contraseña erroneos"
    except smtplib.socket.error:
        return "Error: No hay conexión a internet"
    except smtplib.socket.timeout:
        return "Error: Se ha excedido el tiempo de espera"
    except Exception as err:
        return "Error: " + str(err)
