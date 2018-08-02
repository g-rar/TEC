def llamadaCifTel():
    """Aquí el usuario ingresa el mensaje que quiere encriptar y éste se
pasa por la función de validación. En caso de que no pudiera ser validado
retorna un False."""
    print('\nSe va a proceder a encriptar un mensaje en código de teléfono.')
    preMensaje=input('Ingrese a continuación el mensaje a codificar: \n').lower()
    print('\nValidando...')
    if valCifTel(preMensaje):
        print('Encriptando...')
        return cifTel(valCifTel(preMensaje))+"88"
    else:
        return False
        
def valCifTel(mensaje,mensajeV='',i=0):     #iteratividad disfrazada de recursividad
    """Valida que el mensaje sea encriptable. En caso de
haberse ingresado letras mayúsculas las cambia por minúsculas
y retorna el mensaje validado."""
    lista=list(mensaje)
    if i>(len(lista)-1):   #Condición de pare
        return mensajeV
    elif ord(lista[i])==32 or (ord(lista[i])>=97 and ord(lista[i])<=122):
        mensajeV += lista[i]     #Si la letra es minúscula o un espacio, lo añade tal y como está.
        return valCifTel(mensaje, mensajeV,i+1)
    else:
        print('''\n"'''+lista[i]+'''" es un carácter inválido.
Para el cifrado telefónico se puede usar únicamente el alfabeto
de la <<A>> a la <<Z>> (ya sean mayúsculas o minúsculas) y el
espacio. No se pueden usar acentos, la <<Ñ>> ni signos de puntuación.''')
        print('Vuelva a intentar.')
        return False


def cifTel(mensaje, mensajeCifrado='',i=1):
    """Recibe el mensaje validado, lo encripta y retorna el mensaje encriptado."""
    lista= [' ',['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    #Aquí el truco está en usar la posición de la lista dentro de la lista
    #y la posición de la letra dentro de la lista.
    if mensaje == '':   #Condición de pare
        return mensajeCifrado
    elif mensaje[0] in lista:  #el espacio es el único que está el la lista solo
        mensajeCifrado += '* '
        return cifTel(mensaje[1:],mensajeCifrado,i=0)
    elif mensaje[0] in lista[i]:   #Se busca el carácter en la primera lista.
        mensajeCifrado += str( (lista.index(lista[i])+1)*10 + lista[i].index(mensaje[0])+1)+' '
        #añade la posición de la lista y del carácter dentro de la lista.
        return cifTel(mensaje[1:],mensajeCifrado,i=0)
    else:
        return cifTel(mensaje, mensajeCifrado, i+1) #si no se encuentra el carácte en la primera lista, busca en la que sigue.

def decTel(mensaje, revelado=''):
    """Descifra el mensaje y retorna el mensaje descifrado.
En caso de no poder descifrarlo retorna un False."""
    try:
        lista = ['*','*',['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if mensaje=='':  #funciona similar a la función de encriptación.
            return revelado
        elif mensaje[0]==' ':
            return decTel(mensaje[1:],revelado)
        elif mensaje[0] in lista:
            revelado += ' '
            return decTel(mensaje[1:],revelado)
        else:
            revelado += lista[int(mensaje[0])][int(mensaje[1])-1]
            return decTel(mensaje[2:],revelado)
    except:
        return False
        
