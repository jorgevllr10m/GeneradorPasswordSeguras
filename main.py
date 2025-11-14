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


def main():
    longitud = int(input("Ingrese la longitud de la contraseña deseada: "))

    requerirDigitos = pedir_si_no("¿Requerir al menos un dígito? (S/N) ")

    requerirMayus = pedir_si_no("¿Requerir al menos una mayúscula? (S/N) ")

    requerirMinus = pedir_si_no("¿Requerir al menos una minúscula? (S/N) ")

    requerirSimbolo = pedir_si_no("¿Requerir al menos un símbolo? (S/N) ")
    
    contraseña = generaContraseña(longitud, requerirDigitos, requerirMayus, requerirMinus, requerirSimbolo)
    print(contraseña)

if __name__ == "__main__":
    main()