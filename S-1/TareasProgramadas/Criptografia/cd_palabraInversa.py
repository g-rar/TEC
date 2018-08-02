def palabraInverso(frase):
    """
Recibe una frase dada por el usuario y lo devuelve invertido
"""
    frase1=frase[::-1]
    fraseInv=frase1.split()
    if len(fraseInv)==0:
        return ""
    else:
        return palabraInversoR(fraseInv[::-1])

def palabraInversoR(frase, cadena=""):
    if frase==[]:
        return cadena[1:]
    else:
        cadena += " " + frase[0]
        return palabraInversoR(frase[1:], cadena)
    

def valPalabraInversa(mensaje,mensajeV=''):
    """Valida que el mensaje se pueda mandar por correo. En caso de
    haberse ingresado letras no válidas, le muestra el error al usuario
    y le indica que intente de nuevo."""
    if mensaje == '':
        return mensajeV
    elif ord(mensaje[0])<=127:
        mensajeV += mensaje[0]
        return valPalabraInversa(mensaje[1:], mensajeV)
    else:
        print('''\n"'''+mensaje[0]+'''" es un carácter inválido.''')
        print('Vuelva a intentar.')
        return palabraInversorInput()

    
def palabraInversorInput():
    frase=input("Digite su frase:   ")
    return palabraInverso(valPalabraInversa(frase))


