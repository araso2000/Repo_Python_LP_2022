#Eje 5

def cadenaCaracteres(cadena):
    lista = cadena.splitlines()[0].split(' ')
    numero = 0
    palabraLarga = "none"
    lista.sort()
    print("PALABRAS:")
    for palabras in lista:
        if len(palabras) > numero:
            numero=len(palabras)
            palabraLarga=palabras
        print(palabras + " ",end=" ")

    print("\n\nLa palabra más larga es: " + palabraLarga)

cadenaCaracteres(str(input()))