def mensajeInverso(frase):
    """
    Recibe una frase dada por el usuario y lo devuelve invertido
    """
    return frase[::-1]+'  '

def validacion(frase,mensajeV=''):
    """Valida que el mensaje se pueda mandar por correo. En caso de
    haberse ingresado letras no válidas, le muestra el error al usuario
    y le indica que intente de nuevo."""
    if frase == '':
        return mensajeV
    elif ord(frase[0])<=127:
        mensajeV += frase[0]
        return validacion(frase[1:], mensajeV)
    else:
        print('''\n"'''+frase[0]+'''" es un carácter inválido.''')
        print('Vuelva a intentar.')
        return inputMensajeInverso()

def inputMensajeInverso():
    frase=input("Digite su frase:   ")
    return validacion(mensajeInverso(frase))

def decMensajeInverso(frase):
    """
    Recibe una frase dada por el usuario y lo devuelve invertido
    """
    return frase[::-1]
