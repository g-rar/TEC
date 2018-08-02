def llamadaCifBin():
    """Le pide al usuario el mensaje que quiere encriptar y lo hace
pasar por la función de validación y encriptación. Retorna el mensaje
encriptado."""
    print('Se va a encriptar con cifrado binario. \nIngrese el mensaje que desea encriptar:')
    mensaje = input().lower()
    print('\nValidando...')
    if valCifBin(mensaje):
        print('Encriptando...')
        return cifBin(valCifBin(mensaje)) + '01'
    else:
        return False

def valCifBin(mensaje,mensajeV=''):    #mensajeV es para "mensaje Validado"
    """Valida que el mensaje sea validable. En caso de
haberse ingresado letras mayúsculas las cambia por minúculas
y retorna el mensaje validado."""
    #funciona igual a la validación del código telefónico.
    if mensaje=='':
        return mensajeV
    elif ord(mensaje[0])==32 or (ord(mensaje[0])>=97 and ord(mensaje[0])<=122):
        mensajeV += mensaje[0]
        return valCifBin(mensaje[1:], mensajeV)
    else:
        print('''\n"'''+mensaje[0]+'''" es un carácter inválido.
Para el cifrado binario se puede usar únicamente el alfabeto
de la <<A>> a la <<Z>> (ya sean mayúsculas o minúsculas) y el
espacio. No se pueden usar acentos, la <<Ñ>> ni signos de puntuación.''')
        print('Vuelva a intentar.')
        return False


def cifBin(mensaje,encriptado=''):
    """Toma el mensaje validado y lo retorna encriptado con cifrado binario."""
    if mensaje=='':   #condición de pare
        return encriptado[:-1] #quita el último espacio
    else:
        listaA = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        listaBin = ['* ','00000 ','00001 ','00010 ','00011 ','00100 ','00101 ','00110 ','00111 ','01000 ','01001 ','01010 ','01011 ','01100 ','01101 ','01110 ','01111 ','10000 ','10001 ','10010 ','10011 ','10100 ','10101 ','10110 ','10111 ','11000 ','11001 ']
        encriptado += listaBin[ listaA.index(mensaje[0]) ]   #usa la posición de la letra en la primera lista y añade al mensaje encriptado el elemento que está en la misma posición.
        return cifBin(mensaje[1:],encriptado)

def decBin(encriptado,lista=[],revelado=''):
    """Descifra el mensaje binario y lo retorna descifrado."""
    listaA = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listaBin = ['*','00000','00001','00010','00011','00100','00101','00110','00111','01000','01001','01010','01011','01100','01101','01110','01111','10000','10001','10010','10011','10100','10101','10110','10111','11000','11001']
    if lista == []:    #la lista empieza vacía, ésto es lo primero que va a hacer la función
        lista = encriptado.split(' ')  #toma el mensaje encriptado y lo separa por espacios en la lista
        return decBin(encriptado,lista) #continúa la recursividad con la nueva lista
    elif (lista[0] in listaBin) and len(lista)==1:   #condición de pare, toma el último elemento que queda en la lista
        revelado += listaA[ listaBin.index(lista[0]) ]
        return revelado
    elif lista[0] in listaBin:
        revelado += listaA[ listaBin.index(lista[0]) ] #usa la posición de la letra encriptada en la segunda lista y añada al mensaje revelado el elemento que está en la misma posición.
        return decBin(encriptado,lista[1:],revelado)
    else:
        return False
        
        
