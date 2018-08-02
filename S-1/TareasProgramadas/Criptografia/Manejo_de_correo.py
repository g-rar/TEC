import smtplib
import imaplib, email

def enviarCorreo(dest, mensaje):
    """Toma el mensaje y se lo envía al correo destinatario."""
    server = smtplib.SMTP('smtp.gmail.com:587') 
    try:
        server.ehlo()   
        server.starttls()
        server.login('estudgera@gmail.com','123abc321')    
        message= 'Subject: {}\n\n{}'.format("Mensaje cifrado.",mensaje)
        server.sendmail('estudgera@gmail.com',dest,message)
        server.quit()
        print('Correo enviado.')
        print('\nRevise la dirección de correo electrónico que ingresó.')
        print('Si no recibió ningún correo, compruebe que la dirección de e-mail que ingresó sea correcta.')
        return True
    except:
        server.quit()
        print('''\nHubo un error con el correo.
Asegúrese de que ingresó una dirección de correo electrónico
válida.''')
        return False

def extraerCuerpo(msg):
    """Cuando se tiene el correo tenemos un código que tiene varias partes,
    pero solo nos interesa la parte que tiene cuerpo o el texto del correo. Ésta
    función extraer esa parte."""
    if msg.is_multipart():
        return extraerCuerpo(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def leerCorreo(usuario, contra):
    """Ésta función utiliza el usuario y la contraseña del usuario para 
    ingresar a su cuenta de gmail y extraer el texto del último correo
    como un string."""
    imap_url='imap.gmail.com'
    try:
        acc = imaplib.IMAP4_SSL(imap_url)   
        acc.login(usuario,contra)           
        acc.select('INBOX')                 
        ultimoCorreo = acc.select('INBOX')[1][0] 
        result, data = acc.fetch(ultimoCorreo, '(RFC822)') 
        crudo = email.message_from_bytes(data[0][1]) 
        mensaje = str(extraerCuerpo(crudo))[2:-5] 
        acc.close()
        return mensaje  
    except:
        acc.close()
        print ('''Algo sucedió al intentar accesar al gmail.
Compruebe que la configuración de su cuenta de gmail permita
el acceso de aplicaciones menos seguras y asegúrese de que la
dirección y contraseña sean correctos.''')
        return False
