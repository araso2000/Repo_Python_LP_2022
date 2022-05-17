import random

# Eje 1
def guessing_name():
    temp = random.randrange(1, 100)
    nombre = 0
    while nombre == 0:
        print("Introduce un numero")
        adivino = int(input())
        if adivino == temp:
            print("HAS ACERTADO!!!")
            nombre = 1
        elif adivino<temp:
            print("El numero a adivinar es mayor que el que has introducido")
        else:
            print("El numero a adivinar es menor que el que has introducido")

guessing_name()