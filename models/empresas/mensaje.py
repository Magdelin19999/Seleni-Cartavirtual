from smtplib import SMTP
from email.message import EmailMessage

def mensaje(correoEmpresa,id):
    # el correo del admin
    username = 'magdelinpai1999@gmail.com'
    password = '1124867339'
    
    msg = EmailMessage()
    msg.set_content(f'!Hola, {correoEmpresa}, Abre este link, para terminar el proceso de activacion: http://localhost:5000/activar-empresa/{id}')
    print('enviando correo')

    msg['Subject']='Asunto de prueba'
    msg['Form']=username
    msg['To']=correoEmpresa

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    #code = server.rcpt(usuario)
    #print(code)
    server.quit()