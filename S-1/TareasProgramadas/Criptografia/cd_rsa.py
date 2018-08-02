import random
listaPrimos=[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

def coprimo(phi,i=0):
    """Selecciona un número que sea coprimo de phi."""
    candidatos=[17,3,5,7,11,13]
    if phi%candidatos[i]==0:  #El número no puede ser divisible por phi
        return coprimo(phi,i+1)  #Intenta con el siguiente elemento en la lista
    else:
        return candidatos[i]

def valorD(e,phi,d=1,aux1=0,aux2=0,aux3=0,aux4=0,i=0):
    """Selecciona un valor para 'd' usando el algoritmo euclidiano extendido."""
    if e == 1:
        return d
    elif d == 1:
        aux1 = e
        aux2 = d
        d= phi-((phi//e)*d)
        e= phi-((phi//e)*e)
        if d<0:
            d= d % phi
            return valorD(e,phi,d,aux1,aux2)
        else:
            return valorD(e,phi,d,aux1,aux2)
    elif i==0:
        aux3 = e
        aux4 = d
        d = aux2-((aux1//e)*d)
        e = aux1-((aux1//e)*e)
        if d<0:
            d = d % phi
            return valorD(e,phi,d,aux1=0,aux2=0,aux3=aux3,aux4=aux4,i=1)
        else:
            return valorD(e,phi,d,aux1=0,aux2=0,aux3=aux3,aux4=aux4,i=1)
    elif i==1:
        aux1 = e
        aux2 = d
        d = aux4-((aux3//e)*d)
        e = aux3-((aux3//e)*e)
        if d<0:
            d = d % phi
            return valorD(e,phi,d,aux1,aux2)
        else:
            return valorD(e,phi,d,aux1,aux2)

def llamadaCifRSA():
    """Aquí el usuario ingresa el mensaje a encriptar y se le pregunta si
tiene una llave pública para encriptar el mensaje. Si no la tiene, se
genera una llave pública y una privada y se retorna el mensaje encritpado."""
    mensaje = input('Se va a encriptar usando el algoritmo RSA.\nIngrese a continuación el mensaje que desea encriptar:\n')
    if mensaje:
        tienellave = input('\nSi tiene una llave pública, ingrese "1".\nSi no la tiene, ingrese "0" y generaremos una llave pública y una privada para usted:\n')
        if tienellave=='1':
            try:
                llavePublica = input('Ingrese la llave a continuación:\n')
                n = int(llavePublica.split(', ')[0][1:])   #se extrae n de la llave ingresada
                e = int(llavePublica.split(', ')[1][:-1])  #se extrae e de la llave ingresada
                return cifRSA(mensaje,n,e)
            except:
                print('\nLa llave que ingresó no es válida.')
                return False
        elif tienellave=='0':
            p = random.choice(listaPrimos)  #se elige un número primo al azar de la lista de arriba
            q = random.choice(listaPrimos)  #se elige otro primo
            n = p*q
            phi = (p-1)*(q-1)
            e= coprimo(phi)   #se usa la función coprimo para seleccionar e
            d= valorD(e,phi)  #se usa la función valorD para seleccionar d
            print('Automáticamente se usa la llave pública para codificar el mensaje.\nEs muy importante que copie las llaves tal y como están.\nLa llave privada no la comparta con nadie, la puede usar para decodificar el mensaje.')
            print('La llave pública es: ',(n,e))
            print('La llave privada es: ',(n,d))
            return cifRSA(mensaje,n,e)
        else:
            print('Opción inválida.')
            return False
    else:
        print('No se ha ingresado ningun mensaje.')
        return False
    
def cifRSA(mensaje,n,e,cifrado=''):
    """Encripta el mensaje y lo retorna cifrado con RSA."""
    if mensaje=='':
        return cifrado + '1'
    else:
        cifrado += (str(ord(mensaje[0])**e%n)) + '*'
        return cifRSA(mensaje[1:],n,e,cifrado)

def listaInt(lista,resultado):
    """Retorna una lista que tiene solo los números enteros del mensaje encriptado."""
    if lista==[]:
        return resultado
    else:
        resultado += [int(lista[0])]
        return listaInt(lista[1:],resultado)

def valRSA(encriptado):
    """Valida que el mensaje esté encriptado en RSA."""
    if ' ' in encriptado:  #RSA es el único encriptado que no tiene espacios
        return False
    else:
        return 1

def llamadaDecRSA(mensaje):
    """Le pide al usuario l llave privada para descifrar y retorna
la función decRSA (que va a retornar el mensaje descifrado)."""
    lista = listaInt(mensaje.split('*'),[])
    llavePrivada = input('Para descifrar un cifrado RSA necesitamos que por favor ingrese la llave privada:\n')
    n = int(llavePrivada.split(', ')[0][1:])
    d = int(llavePrivada.split(', ')[1][:-1])
    return decRSA(lista,n,d)
    

def decRSA(lista,n,d,revelado=''):
    """Descifra el mensaje encriptado en RSA usando la llave privada."""
    if lista==[]:
        return revelado
    else:
        revelado+= chr(lista[0]**d%n)
        return decRSA(lista[1:],n,d,revelado)


##p = random.choice(listaPrimos)
##q = random.choice(listaPrimos)
##print('p es: ', p)
##print('q es: ', q)
###p y q son los números primos que multiplicados me dan n
##n = p*q
##print('n es: ',n)
##phi = (p-1)*(q-1)
##print('phi es: ',phi)
##e=coprimo(phi)
##print('e es: ',e)
##d= valorD(e,phi)
##print('d es:',d)
##
#pequeño registro de errores: salió una combinación de phi=5916456 y e=3, resulta que phi era divisible entre 3
