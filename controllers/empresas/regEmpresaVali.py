
from math import fabs

from flask import render_template
from models.empresas import setenciasSQLUsusarios as SQL
import re

def validacionForm (nombreEmpresa,descEmpresa,celularEmpresa,direccionEmpresa,correo,contrasenia):
    is_valid = True
    resultado= []
    mensaje =[]
    if nombreEmpresa=="":
        mensaje.append('El nombre es requerido\n')
        is_valid = False
    if descEmpresa =='':
        mensaje.append('Descripcion requerida\n')
        is_valid = False
    if celularEmpresa =='':
        mensaje.append('Celular reuquerido\n')
        is_valid = False
    if direccionEmpresa =='':
        mensaje.append('Direcion requerida\n')
        is_valid = False
    if correo =='':
        mensaje.append('Correo requerido\n')
        is_valid = False
    if contrasenia =='':
        mensaje.append('Contraseña requerida \n')
        print('contra ok')
        is_valid = False
    elif validarContrasenia(contrasenia)==False:
        is_valid = False
        mensaje.append('No cumple con los requisitos :(')
        
    if is_valid ==False:
        return [is_valid,mensaje]
    #validar si el correo esta ya registrado
    # is_valid === True
    #    existe == True 
    #        return [False ,'Correo ya se Encuentra registrado']        
    else:
        return [is_valid,mensaje]

def validarContrasenia(contrasenia):
    ## validar
    if 8 <= len(contrasenia) <= 16:
        if re.search('[a-z]',contrasenia) and re.search('[A-Z]',contrasenia):
            if re.search('[0-9]',contrasenia):
                if re.search('[$@#]',contrasenia):
                    return True
    return False

