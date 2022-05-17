#Eje 4
def pig_latin(cadena):
    primeraLetra = cadena[0]
    if primeraLetra == 'a' or primeraLetra == 'e' or primeraLetra == 'i' or primeraLetra == 'o' or primeraLetra == 'u':
        return cadena + "way"
    else:
        return (cadena + cadena[0] + "ay")[1:]

print(pig_latin("air"))
print(pig_latin("python"))