def cifradoCesar(frase):
    """
    Recibe un string dado por el usuario y lo cifra én césar bajo la clave de 3.
    """
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(frase)==0:
        return "CE"
    elif frase[0]==" ":
        return " "+ cifradoCesar(frase[1:])
    else:
        buscador=abc.find(frase[0])+3
        formula=int(buscador)%len(abc)
        return str(abc[formula]) + cifradoCesar(frase[1:])

def validacionCifradoCesar(frase):
    """
    Verifica que la entrada de datos se encuentre dentro del abecedario establecido,
    si se encuentra dentro del abecedario procede a cifrar
    Si es un integer o un float da el mensaje 'Digite únicamente letras del alfabeto'
    """ 
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    if frase=="":
        return True    
    elif abc.find(frase[0])==-1:
        print("Digite únicamente letras del alfabeto")
        return False 
    else:
        return validacionCifradoCesar(frase[1:])

def inputCifradoCesar():
    """
    #Función que pide los datos al usuario e imprime el mensaje cifrado en caso que los datos sean válidos
    def cifradoCesarInput(frase):
    """
    frase=input("Digite la frase a cifrar:   ").upper()
    if validacionCifradoCesar(frase):
        return cifradoCesar(frase)
    else:
        print("Ingrese una nueva frase.")
        return inputCifradoCesar()
        
#actualizar el decrifrado

def decifradoCesar(frase):
    """
    Recibe un string que se encuentra cifrado con clave de 3 dado por el usuario y lo decifra.
    """
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(frase)==0:
        return ""
    elif frase[0]==" ":
        return " "+ decifradoCesar(frase[1:])
    else:
        buscador=abc.find(frase[0])-3
        formula=int(buscador)%len(abc)
        return str(abc[formula]) + decifradoCesar(frase[1:])

def validacionDecifradoCesar(frase):
    """
    Verifica que la entrada de datos se encuentre dentro del abecedario establecido,
    si se encuentra dentro del abecedario procede a decifrar
    Si es un integer o un float da el mensaje 'Digite únicamente letras del alfabeto'
    """        
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    if frase=="":
        return True
    elif abc.find(frase[0])==-1:
        return False
    else:
        return validacionDecifradoCesar(frase[1:])

def inputDecifradoCesar():
    """Función que pide los datos al usuario e imprime el mensaje decifrado en caso que los datos sean válidos"""
    frase=input("Digite la frase a decifrar:   ").upper()
    if validacionDecifradoCesar(frase):
        return decifradoCesar(frase)
    else:
        print("Ingrese una nueva frase.")
        return inputDecifradoCesar()
    
