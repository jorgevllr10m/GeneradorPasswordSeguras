import random
import string

def generaContraseña(l):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    contraseña = ""

    for _ in range(l):
        contraseña += random.choice(caracteres)
    return contraseña

def main():
    longitud = int(input("Ingrese la longitud de la contraseña deseada: "))
    contraseña = generaContraseña(longitud)
    print()
    print(contraseña)

if __name__ == "__main__":
    main()