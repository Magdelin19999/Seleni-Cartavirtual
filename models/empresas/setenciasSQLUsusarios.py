from flask import session
from config import dataBase

DB = dataBase.DB


def insertUsuario(
    nombreEmpresa, descEmpresa, celularEmpresa, direccionEmpresa, correo, contrasenia
):
    cursor = DB.cursor()
    cursor.execute(
        f"""INSERT INTO usuarios(nombreEmpresa, descEmpresa, celularEmpresa,
                                        direccionEmpresa, correo, contrasenia) 
	                VALUES( '{nombreEmpresa}','{descEmpresa}','{celularEmpresa}',
                            '{direccionEmpresa}', '{correo}','{contrasenia}')"""
    )
    idultimo = cursor.lastrowid
    print(f"El usuario registrado con el id:{idultimo}")
    cursor.close()
    return idultimo


def obtenerDBID(id):
    empresa = []
    cursor = DB.cursor(dictionary=True)
    cursor.execute(f"""SELECT * FROM usuarios WHERE id={id};""")
    empresa = cursor.fetchone()
    cursor.close()
    if empresa:
        print(f"tamaño diccionario {len(empresa)}")
        activarID(empresa["id"])
        return {'estado':True, 'mensaje':f'Registro finalizado, inicia sesion  :)','category':'success' }

    return {'estado':False, 'mensaje':f'Erro al activar Cuenta :(','category':'warning' }


def activarID(id):
    print("ativando id", id)
    cursor = DB.cursor()
    cursor.execute(f"UPDATE usuarios SET estado = 1 WHERE id = {id}")
    cursor.close()
    


def obtenerEmpresa(correo, contrasenia):
    print(correo,contrasenia)
    
    cursor = DB.cursor(dictionary=True)
    cursor.execute(
        f"""SELECT * FROM usuarios   
                   WHERE correo = '{correo}' AND contrasenia = '{contrasenia}';"""
    )
    empresa = cursor.fetchone()
    cursor.close()
    if empresa:
        print(f"tamaño diccionario {len(empresa)}")
        activarID(empresa["id"])
        session["loggedin"] = True
        session["id"] = empresa["id"]
        session["usuario"] = empresa["nombreEmpresa"]
        
        return {'estado':True, 'mensaje':f'Bienvenido {empresa["nombreEmpresa"]}','category':'success' }

    return {'estado':False, 'mensaje':'Error de inicio de sesion :(','category':'warning' }
    #'SELECT * FROM accounts WHERE correo = %s AND contrasenia = ''


def cerrarSesion():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("usuario", None)
