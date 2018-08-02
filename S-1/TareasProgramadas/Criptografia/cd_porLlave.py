
abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cifradoporLlave(frase,clave, claveReset='',cadena=""):
    if claveReset == "":
        claveReset = clave
        return cifradoporLlave(frase,clave,claveReset)
    elif frase=="":
        cadena += 'll'
        return cadena
    elif clave == "":
        clave = claveReset
        return cifradoporLlave(frase,clave,claveReset,cadena)
    elif frase[0]==" ":
        clave = claveReset
        cadena += ' '
        return cifradoporLlave(frase[1:],clave, claveReset, cadena)
    else:
        suma=abcd.index(frase[0])+ abcd.index(clave[0])+2
        if 1<=suma<=26:
            cadena += abcd[suma-1]
            return cifradoporLlave(frase[1:], clave[1:], claveReset,cadena)
        else:
            suma-=26
            cadena += abcd[suma-1]
            return cifradoporLlave(frase[1:], clave[1:],claveReset,cadena)
            
def inputCifradoporLlave():
    try:
        frase=input("Digite la frase a cifrar:   ")
        clave=input("Digite la clave:   ")
        return cifradoporLlave(frase,clave, claveReset='',cadena="")
    except:
        print ("Ingrese unicamente letras en la frase y clave \n")
        return inputCifradoporLlave()



########

def decifradoporLlave(frase,clave, claveReset='',cadena=""):
    if claveReset == "":
        claveReset = clave
        return decifradoporLlave(frase,clave,claveReset)
    elif frase=="":
        cadena += ''
        return cadena
    elif clave == "":
        clave = claveReset
        return decifradoporLlave(frase,clave,claveReset,cadena)
    elif frase[0]==" ":
        clave = claveReset
        cadena += ' '
        return decifradoporLlave(frase[1:],clave, claveReset, cadena)
    else:
        resta=abcd.index(frase[0])- abcd.index(clave[0])
        if 1<=resta<=26:
            cadena += abcd[resta-1]
            return decifradoporLlave(frase[1:], clave[1:], claveReset,cadena)
        else:
            resta+=26
            cadena += abcd[resta-1]
            return decifradoporLlave(frase[1:], clave[1:],claveReset,cadena)
            
def inputDecifradoporLlave(frase):
    try:
        clave=input("Digite la clave en que se encuentra cifrado el mensaje:   ")
        return decifradoporLlave(frase,clave, claveReset='',cadena="")
    except:
        print ("Ingrese unicamente letras en la frase y clave \n")
        return inputDecifradoporLlave()




    
