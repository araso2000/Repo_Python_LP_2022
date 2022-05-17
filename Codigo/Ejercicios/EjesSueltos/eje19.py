#Eje 19

def encriptador(path):
    file = open(path)
    lineas = file.readlines()
    palabras = ""
    numeros = ""

    for x in lineas:
        palabras = palabras + str(x.splitlines()[0].split(' '))

    for y in palabras:
        numeros = numeros + str(ord(y)) + "\n"

    nuevofichero = "C:/Users/araso/Desktop/resultado.txt"

    try:
        file2 = open(nuevofichero, "w")
        file2.writelines(numeros)
        file2.flush()
        file2.close()

    except FileNotFoundError:
        file2 = open(nuevofichero, "x")
        file2.writelines(numeros)
        file2.flush()
        file2.close()

encriptador("C:/Users/araso/Desktop/lorem.txt")

def desencriptador(path):
    file = open(path)
    lineas = file.readlines()
    texto = " "
    for x in lineas:
        texto = texto + chr(int(x)) 

    print(texto)

desencriptador("C:/Users/araso/Desktop/resultado.txt")