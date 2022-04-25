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


#guessing_name()


#Eje 2
def mySum(*numeros):
    output = 0
    for numero in numeros:
        output = output + numero
    print(output)

#mySum(10,20,30)


#Eje 3
def run_timing():
    contador = 0
    resultado = 0
    while True:
        print("Introduce nuevo tiempo para una carrera de 10 km")
        variable = input()

        if not variable:
            break

        resultado = resultado + float(variable)
        contador = contador+1

    print("Tiempo medio de " + str(contador) + " carreras: " + str(resultado/contador))

#run_timing()


#Eje 4
def pig_latin(cadena):
    primeraLetra = cadena[0]
    if primeraLetra == 'a' or primeraLetra == 'e' or primeraLetra == 'i' or primeraLetra == 'o' or primeraLetra == 'u':
        return cadena + "way"
    else:
        return (cadena + cadena[0] + "ay")[1:]

#print(pig_latin("air"))
#print(pig_latin("python"))