#Tarea programada nº1
#Realizado por: Gerardo López & Mariell Sánchez
#Última modificación: 16-4-2018
#Versión: 3.4.6

###########################
#Importación de funciones.#
###########################
import smtplib
import cd_cesar
import cd_bin
import cd_tel
import cd_rsa
import cd_Vigenere
import cd_mensajeInverso
import cd_palabraInversa
import cd_porLlave
import Manejo_de_correo
    

###########
#Funciones#
###########
def mainMenu():
    """Esta función es un menú para que el usuario navegue entre las
    diferentes funciones del programa."""
    print("\n-Menú principal-")
    print("\n1. Encriptar.")
    print("2. Desencriptar.")
    print("0. Cerrar programa.")
    feature=input("Escriba el número de la función que desea usar.\n")
    try:
        if int(float(feature))>=0 and int(float(feature))<=2:
            if feature=='1':
                preMenuE()
            elif feature=='2':
                preMenuD()
            else:
                return
        else:
            print("\nOpción inválida. Intente de nuevo.")
            mainMenu()
    except ValueError:
        print("\nOpción inválida. Intente de nuevo.")
        mainMenu()

def preMenuE():
    """En esta función se ingresa la información de usuario
    para enviar mensajes cifrados."""
    correoUsuario=input('Necesitamos una dirección de correo electrónico para enviar los mensajes codificados. \nPor favor ingresela a continuación:\n')
    menuE(correoUsuario)
    
def protocoloE(mensaje,correoUsuario):
    """Recibe el mensaje ya cifrado y lo envía.
    Notifica de errores en el proceso."""
    if mensaje:
        print('Enviando correo...')
        try:
            if Manejo_de_correo.enviarCorreo(correoUsuario,mensaje):
                mainMenu()
            else:
                print('Intente de nuevo.')
                mainMenu()
        except:
            print('No se pudo conectar con los servidores. Compruebe su conexión a internet e intente de nuevo.')
            menuE(correoUsuario)
    else:
        print("No se ha ingresado ningún mensaje.")
        menuE(correoUsuario)
    
def menuE(correoUsuario):
    """Aquí se pueden accesar las funciones de encriptación de mensajes.
    Luego de asignado l mensaje cifrado a la variable 'mesaje', se manda
    a la función de protocolo."""
    print("\n-Menú Encriptar-")
    print("\n1. Cifrado César.")
    print("2. Cifrado por llave.")
    print("3. Sustitución Vigenére.")
    print("4. Palabra inversa.")
    print("5. Mensaje inverso.")
    print("6. Encriptado por código telefónico.")
    print("7. Cifrado por codificación binaria.")
    print("8. RSA.")
    print("\n0. Volver.")
    pFeature=input("\nEscriba el número de la función que desea usar.\n")
    try:
        feature = int(float(pFeature))
        try:
            if feature>=0 and feature<=8:
                if feature == 1:
                    mensaje = cd_cesar.inputCifradoCesar()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 2:
                    mensaje = cd_porLlave.inputCifradoporLlave()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 3:
                    mensaje = cd_Vigenere.inputCifradoVigenere()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 4:
                    mensaje = cd_palabraInversa.palabraInversorInput() + 'ni'
                    protocoloE(mensaje,correoUsuario)
                elif feature == 5:
                    mensaje = cd_mensajeInverso.inputMensajeInverso()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 6:
                    mensaje = cd_tel.llamadaCifTel()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 7:
                    mensaje = cd_bin.llamadaCifBin()
                    protocoloE(mensaje,correoUsuario)
                elif feature == 8:
                    mensaje = cd_rsa.llamadaCifRSA()
                    protocoloE(mensaje,correoUsuario)
                else:
                    mainMenu()
            else:
                print("\nOpción inválida. Intenta de nuevo.")
                menuE(correoUsuario)
        except: #Aquí es por si hubo un error general en el código.
            print("\nAlgo salió mal.")
            mainMenu()
    except:   #Si se ingrase una letra, cae en éste except y vuelve a intentar.
        print("\nOpción inválida. Intenta de nuevo.")
        menuE(correoUsuario)

#Funciones para descifrar

def detectarAlgoritmo(encriptado):
    """Encuentra la función de validación en la lista cuyo valor no sea
    False, y procede a llamar la función que la desencripta. En caso de no
    encontrar ninguna, avisa que el mensaje no pudo ser decodificado."""
    if encriptado[-2:]=='CE':
        return cd_cesar.decifradoCesar(encriptado[:-2])
    elif encriptado[-2:] == '88':
        return cd_tel.decTel(encriptado[:-2])
    elif encriptado[-2:] == '*1':
        return cd_rsa.llamadaDecRSA(encriptado[:-2])
    elif encriptado[-2:] == '01':
        return cd_bin.decBin(encriptado[:-2])
    elif encriptado[-2:] == 'VG':
        return cd_Vigenere.inputDecifradoVigenere(encriptado[:-2])
    elif encriptado[-2:] == '  ':
        return cd_mensajeInverso.decMensajeInverso(encriptado[:-2])
    elif encriptado[-2:] == 'ni':
        return cd_palabraInversa.palabraInverso(encriptado[:-2])
    elif encriptado[-2:] == 'll':
        return cd_porLlave.inputDecifradoporLlave(encriptado[:-2])
    else:
        print('No se pudo desencriptar el mensaje.')
        mainMenu()
    

def preMenuD():
    """Aquí se ingresan el correo y la contraseña del usuario
    para poder extraer el mensaje encriptado."""
    correoUsuario = input('Vamos a accesar a su cuenta de correos para decodificar el último mensaje recibido. \nPor favor ingrese su dirección de gmail:\n')
    contra = input('Ahora ingrese su contraseña (no recabamos ninguna información de su cuenta, ingrese "e" si quiere salir):\n')
    if correoUsuario == 'e' or contra == 'e':
        print('\nSaliendo. Va a volver al menú principal.')
        mainMenu()
    else:
        menuD(correoUsuario,contra)

def menuD(correoUsuario, contra):
    """Una vez ingresadas el correo y la contraseña, se extrae el último
    correo recibido como un string y se pasa por la función llamadaDetectar.
    Tras esto se imprime el mensaje desencriptado y se vuelve al menú principal."""
    print("\n----Desencriptar----")    
    try:
        print('\nExtrayendo el mensaje encriptado de la cuenta de correos.')
        try:
            msgEncriptado = Manejo_de_correo.leerCorreo(correoUsuario,contra)
            if msgEncriptado: #al igual que más arriba, si msgEncriptado no es un string vacío, retornará True
                print('\nDesencriptando.')
                mensaje = detectarAlgoritmo(msgEncriptado)
                if mensaje:
                    print('\nEl mensaje oculto es: \n---------------------------------\n')
                    print(mensaje + '\n')
                    print('---------------------------------')
                    mainMenu()
                else:
                    print('Intente de nuevo.')
                    mainMenu()
            else:
                print('Intente de nuevo')
                mainMenu()
        except:
            print('No se pudo conectar con los servidores. Compruebe su conexión a internet e intente de nuevo.')
            mainMenu()
    except:
        print("\nAlgo sucedió. Intenta de nuevo.")
        mainMenu()


###################
#Accionar programa#
###################
print(" _____  ___ ______ __ ____  __   _____ ___   ___    _____ ___´__   ___")
print("(/  (/ |   )  ||  |  ) ||  /__\ (/  (/|   ) / _ \  |        ||    / _ \ ")
print("(|     |__/   ||  |_/  || ((__))(| _  |__/ / /_\ \ |===     ||   / /_\ \ ")
print("(\__/) |  \ ------|    ||  \__/ (\__\)|  \|_/   \_||      ------|_/   \_| ")

mainMenu()
