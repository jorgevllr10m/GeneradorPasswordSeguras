import random
import string

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

def pedir_si_no(mensaje):
    """
    Solicita al usuario una respuesta 'S' o 'N' y valida la entrada.

    Args:
        mensaje (str): Texto que se mostrará al pedir la respuesta.

    Returns:
        bool: True si el usuario introduce 'S', False si introduce 'N'.
    """
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta in ("S", "N"):
            return respuesta == "S"
        print("\nEntrada no válida. Escribe 'S' o 'N'.")

def medidorSeguridad(contraseña):
    puntuacion=0
    if(len(contraseña)<6):
        puntuacion+=0
    elif(len(contraseña)>=6 & len(contraseña)<12):
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
            


def main():
    longitud = int(input("Ingrese la longitud de la contraseña deseada: "))

    requerirDigitos = pedir_si_no("¿Requerir al menos un dígito? (S/N) ")

    requerirMayus = pedir_si_no("¿Requerir al menos una mayúscula? (S/N) ")

    requerirMinus = pedir_si_no("¿Requerir al menos una minúscula? (S/N) ")

    requerirSimbolo = pedir_si_no("¿Requerir al menos un símbolo? (S/N) ")
    
    contraseña = generaContraseña(longitud, requerirDigitos, requerirMayus, requerirMinus, requerirSimbolo)
    print("\nLa contraseña generada es: " + contraseña)
    print("\nEl nivel de seguridad de la contraseña es: " + medidorSeguridad(contraseña))

if __name__ == "__main__":
    main()