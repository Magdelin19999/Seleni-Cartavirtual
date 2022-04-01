from hashlib import md5
from models.empresas import mensaje as sendMensaje,setenciasSQLUsusarios as SQL
from flask import flash

def datosFormulario(nombreEmpresa,descEmpresa,celularEmpresa,
                  direccionEmpresa,correo,contrasenia):
    
    contrasenia = encriptarContraseña(contrasenia)  
    resultado = SQL.insertUsuario(nombreEmpresa,descEmpresa,celularEmpresa,
                                    direccionEmpresa,correo,contrasenia)
    
    if(isinstance(resultado, int)==True):
          print('Enviar mensaje del usuario')
          sendMensaje.mensaje(correo,resultado)
          

def activacion(id):
    print(f'recibio activacion {id}')
    return SQL.obtenerDBID(id)
  
def encriptarContraseña(contrasenia):
    print('Encriptando contraseña')
    
    return md5(contrasenia.encode("utf-8")).hexdigest() 

def inicioSesion(correo, contrasenia):
    mensaje =''
    print('inicio de sesion')
    return (SQL.obtenerEmpresa(correo, encriptarContraseña(contrasenia)))
    

def  cerrarSesion():
    SQL.cerrarSesion()