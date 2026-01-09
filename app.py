import random
import string

from flask import Flask, render_template, request

app = Flask(__name__)

MIN_LEN = 4
MAX_LEN = 32

def generaContraseña(l, requerirDigito, requerirMayuscula, requerirMinuscula, requerirSimbolo):
    
    requeridos = sum([requerirDigito, requerirMayuscula, requerirMinuscula, requerirSimbolo])
    if l < requeridos:
        raise ValueError("No puedes poner más símbolos requeridos que la longitud de la contraseña.")
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = []

    if(requerirDigito):
        contraseña.append(random.choice(string.digits))
    
    if(requerirMayuscula):
        contraseña.append(random.choice(string.ascii_uppercase))

    if(requerirMinuscula):
        contraseña.append(random.choice(string.ascii_lowercase))
    
    if(requerirSimbolo):
        contraseña.append(random.choice(string.punctuation))

    for _ in range(l-len(contraseña)):
        contraseña.append(random.choice(caracteres))

    random.shuffle(contraseña)

    return "".join(contraseña)

def medidorSeguridad(contraseña):
    puntuacion=0
    if(len(contraseña)<6):
        puntuacion+=0
    elif(len(contraseña)>=6 and len(contraseña)<12):
        puntuacion+=1
    else:
        puntuacion+=2
    
    if(any(c.isupper() for c in contraseña)):
        puntuacion+=1
    if(any(c.islower() for c in contraseña)):
        puntuacion+=1
    if(any(c.isdigit() for c in contraseña)):
        puntuacion+=1
    if(any(c in string.punctuation for c in contraseña)):
        puntuacion+=2

    caracteres_unicos = set(contraseña)
    if (len(caracteres_unicos)/len(contraseña)<0.33):
        puntuacion-=1
    elif(len(caracteres_unicos)/len(contraseña)<0.66):
        puntuacion+=1
    else:
        puntuacion+=2

    if(puntuacion<5):
        return "débil"
    elif(puntuacion<8):
        return "segura"
    else:
        return "muy segura"

@app.get("/")
def home():
    # Página inicial
    return render_template("index.html", contraseña=None, fuerza=None, error=None, min_len=MIN_LEN, max_len=MAX_LEN)

@app.post("/generar")
def generar():
    contraseña = None
    fuerza = None
    error = None
    
    longitud = int(request.form["longitud"])
    requerirDigito = "digito" in request.form
    requerirMayuscula = "mayus" in request.form
    requerirMinuscula = "minus" in request.form
    requerirSimbolo = "simbolo" in request.form

    #Validación en el servidor 
    if longitud is None:
        error = "La longitud debe ser un número."
    elif longitud < MIN_LEN or longitud > MAX_LEN:
        error = f"La longitud debe estar entre {MIN_LEN} y {MAX_LEN}."
    else:
        try:
            contraseña = generaContraseña(longitud, requerirDigito, requerirMayuscula, requerirMinuscula, requerirSimbolo)
            fuerza = medidorSeguridad(contraseña)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", contraseña=contraseña, fuerza=fuerza, error=error, min_len=MIN_LEN, max_len=MAX_LEN)

if __name__ == "__main__":
    app.run()