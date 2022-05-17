#Eje 16

def tail(path):
    file = open(path)
    lineas = file.readlines()
    numero = len(lineas)
    print(lineas[(numero-10):numero+1])

tail("C:/Users/araso/Desktop/lorem.txt")