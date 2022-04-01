
from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS
from controllers.empresas import regEmpresaVali 
import re
# from models.empresas import mensaje
app = Flask(__name__)
app.secret_key = "magdelinpai"

@app.get("/")
def home():
    # mensaje.mensaje()
    '''     
    if "loggedin" in session:
        print(session["usuario"])
        return render_template("productos/empresa-producto.html")

    else:
        print("nada")
        return render_template("productos/index.html") 
    '''
    return render_template("productos/index.html")

"""
    registro y activacion de empresa 
"""

@app.get("/registro-empresa/")
def registroEmpresa():
    return render_template("empresas/registro.html")

@app.post("/registro-empresa/")
def registroEmpresaForm():
    print("holaaa")
    is_valid = True
    nombreEmpresa = request.form.get("nombreEmpresa")
    descEmpresa = request.form.get("descEmpresa")
    celularEmpresa = request.form.get("celularEmpresa")
    direccionEmpresa = request.form.get("direccionEmpresa")
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    
    resultado = regEmpresaVali.validacionForm(nombreEmpresa,descEmpresa,celularEmpresa,direccionEmpresa,correo,contrasenia)
    if (resultado[0]==False):
        #flash("".join(resultado[1]))
        flash("".join(resultado[1]),'warning ')
        return redirect(url_for("registroEmpresa"))

    USUARIOS.datosFormulario(
        nombreEmpresa,
        descEmpresa,
        celularEmpresa,
        direccionEmpresa,
        correo,
        contrasenia,
    )         

    flash('Usuario registrado.... Revisa tu correo Para completar el registro','success') 
    
    return redirect(url_for("home"))
    #return render_template("empresas/sing.html")

@app.get("/activar-empresa/<int:id>")
def activarEmpresa(id):
    print(f"activacion {id}")

    resultadiActivacion =  USUARIOS.activacion(id)
    
    ## el resultadiActivacion['estado], es para pasar a la vista la clase como atributo al alert y redireccionar 
    print(resultadiActivacion)
    flash(resultadiActivacion['mensaje'],resultadiActivacion['category'])
    '''  '''
    if resultadiActivacion['estado']:
        return render_template('empresas/sing.html')
    else:
        return render_template('empresas/resgistro.html') 
    
""" parte del inicio de sesion y cerrar sesion """

@app.get("/inicio-sesion/")
def inicioSesion():
    return render_template("empresas/sing.html")

@app.post("/inicio-sesion/")
def inicioSesionForm():
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    resultadoInicio = USUARIOS.inicioSesion(correo, contrasenia)
    print(resultadoInicio)
    # mensaje de estado de sesion 
    flash(resultadoInicio['mensaje'],resultadoInicio['category'])
    
    if(resultadoInicio['estado']):
        print('Ya se inicio de sesion activa')
        return render_template("productos/empresa-producto.html")
        
    else:
        print('aun no esta iniciadaa ')
        return render_template("empresas/sing.html")

@app.get("/inicio-sesion/out")
def logout():
    USUARIOS.cerrarSesion()
    return redirect(url_for("home"))

""" manipulacion productos """

@app.get("/administracion/mis-productos")
def misProductos():
    return render_template("productos/empresa-producto.html")


@app.get("/administracion/registro-producto")
def registroProducto():
    return render_template("productos/empresa-registro-prod.html")

app.run(app.run(debug=True))
