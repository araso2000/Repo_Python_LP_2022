#Eje 17

def read_sum(path):
    file = open(path)
    lista = file.readlines()
    palabras = ""
    real = ""
    for x in lista:
        palabras = palabras + str(x.splitlines()[0].split(' ')) + "\n"

    print(real)

read_sum("C:/Users/araso/Desktop/lorem.txt")