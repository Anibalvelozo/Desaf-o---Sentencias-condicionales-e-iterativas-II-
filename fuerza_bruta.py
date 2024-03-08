import sys
from string import ascii_lowercase
from getpass import getpass

password = getpass("Ingrese la contraseña: ").lower()
contador = 0

print("Lo ingresado es [" + password + "]")
for letra in password:
    for elemento in ascii_lowercase:
        contador += 1
        if letra == elemento:
            break

print("La contraseña fue forzada en ", contador, " intentos")