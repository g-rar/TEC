

abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def cifradoVigenere1(frase,clave):
    """
Recibe un string dado por el usuario y una contraseña y lo cifra bajo esa contraseña
"""
    if type(clave)==str:
        print ("La frase debe ser unicamente valores numéricos")
        return inputCifradoVigenere()
    elif (clave//10)//10==0:
        if len(frase)==0:
            return "VG"
        elif frase[0]==" ":
            return " "+ cifradoVigenere1(frase[1:], clave)
        else:
            buscador=abc.find(frase[0])+clave//10
            formula=int(buscador)%len(abc)
            return str(abc[formula])+cifradoVigenere2(frase[1:],clave)
    else:
        print ("La clave debe tener unicamente dos digitos")
        return inputCifradoVigenere()
    

def cifradoVigenere2(frase,clave):
    if len(frase)==0:
        return "VG"
    elif frase[0]==" ":
        return " "+ cifradoVigenere1(frase[1:],clave)
    else:
        buscador1=abc.find(frase[0])+clave%10
        formula1=int(buscador1)%len(abc)
        return str(abc[formula1])+cifradoVigenere1(frase[1:],clave)


def validacionCifradoVigenere(frase,clave):
    """
Verifica que la entrada de datos se encuentre dentro del abecedario establecido,
si se encuentra dentro del abecedario procede a cifrar
Si es un integer o un float da el mensaje 'Digite únicamente letras del alfabeto'
""" 
    if frase=="":
        return True    
    elif abc.find(frase[0])==-1:
        if frase[0]== ' ':
            return validacionCifradoVigenere(frase[1:],clave)
        else:
            print("Digite únicamente letras del alfabeto. ")
            return False 
    else:
        return validacionCifradoVigenere(frase[1:],clave)

#Función que pide los datos al usuario e imprime el mensaje cifrado en caso que los datos sean válidos
def inputCifradoVigenere():
    frase=input("Digite la frase a cifrar:   ").upper()
    clave=int(input("Digite la clave numérica:   "))
    if validacionCifradoVigenere(frase,clave):
        return cifradoVigenere1(frase,clave)
    else:
        print ("Recuerde que el programa no acepta tildes o la letra 'ñ'. Ingrese una nueva frase")
        return inputCifradoVigenere()


#hacer el decrifrado#
def decifradoVigenere1(frase,clave):
    """
Recibe un string dado por el usuario y una contraseña y lo cifra bajo esa contraseña
"""
    if type(clave)==str:
        print ("La frase debe ser unicamente valores numéros")
        return inputDecifradoVigenere()
    elif (clave//10)//10==0:
        if len(frase)==0:
            return ""
        elif frase[0]==" ":
            return " "+ decifradoVigenere1(frase[1:], clave)
        else:
            buscador=abc.find(frase[0])- clave//10
            formula=int(buscador)%len(abc)
            return str(abc[formula])+decifradoVigenere2(frase[1:],clave)
    else:
        print ("La clave debe tener unicamente dos digitos")
        return inputDecifradoVigenere()
    

def decifradoVigenere2(frase,clave):
    if len(frase)==0:
        return ""
    elif frase[0]==" ":
        return " "+ decifradoVigenere1(frase[1:],clave)
    else:
        buscador1=abc.find(frase[0])- clave%10
        formula1=int(buscador1)%len(abc)
        return str(abc[formula1])+decifradoVigenere1(frase[1:],clave)


def validacionDecifradoVigenere(frase,clave):
    """    
Verifica que la entrada de datos se encuentre dentro del abecedario establecido,
si se encuentra dentro del abecedario procede a cifrar
Si es un integer o un float da el mensaje 'Digite únicamente letras del alfabeto'
"""
    if frase=="":
        return True    
    elif len(str(clave)) != 2:
        print("La clave debe ser de dos dígitos.")
        return False
    elif abc.find(frase[0])==-1:
        if frase[0]== ' ':
            return validacionCifradoVigenere(frase[1:],clave)
        else:
            print("Digite únicamente letras del alfabeto. ")
            return False 
    else:
        return validacionDecifradoVigenere(frase[1:],clave)

#Función que pide los datos al usuario e imprime el mensaje cifrado en caso que los datos sean válidos
def inputDecifradoVigenere(frase):
    print("El mensaje está en cifrado Vigenere.")
    try:
        clave=int(input("Digite la clave numérica en que la frase se encuentra cifrada:   "))
        if validacionDecifradoVigenere(frase,clave):
            return decifradoVigenere1(frase,clave)
        else:
            print("Clave inválida. Intente de nuevo.")
            return inputDecifradoVigenere(frase)
    except:
        print("La clave debe ser un número de dos dígitos.")
        return inputDecifradoVigenere(frase)


