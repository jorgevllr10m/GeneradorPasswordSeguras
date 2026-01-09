from flask import Blueprint, render_template, request

from services.ServicePassword import (
    MIN_LEN, MAX_LEN,
    validar_longitud,
    generaContraseña,
    medidorSeguridad
)

web = Blueprint("web", __name__)

@web.get("/")
def home():
    return render_template("index.html",contraseña=None,fuerza=None,error=None,min_len=MIN_LEN,max_len=MAX_LEN)

@web.post("/generar")
def generar():
    contraseña = None
    fuerza = None
    error = None

    longitud, error = validar_longitud(request.form.get("longitud"))

    requerirDigito = "digito" in request.form
    requerirMayuscula = "mayus" in request.form
    requerirMinuscula = "minus" in request.form
    requerirSimbolo = "simbolo" in request.form

    if error is None:
        try:
            contraseña = generaContraseña(longitud, requerirDigito, requerirMayuscula, requerirMinuscula, requerirSimbolo)
            fuerza = medidorSeguridad(contraseña)
        except ValueError as e:
            error = str(e)

    return render_template("index.html",contraseña=contraseña,fuerza=fuerza,error=error,min_len=MIN_LEN,max_len=MAX_LEN)