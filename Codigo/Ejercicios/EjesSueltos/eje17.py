#Eje 17

def read_sum(path):
    file = open(path)
    lista = file.readlines()
    print(lista)
    palabras = ""
    real = ""
    for x in lista:
        palabras = palabras + str(x.splitlines()[0].split(' ')) + "\n"
        print(x)


read_sum("./ficheros/lorem.txt")