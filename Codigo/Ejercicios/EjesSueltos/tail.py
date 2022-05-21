#Eje Aparte 1

import sys

def tail(path,lines):
    file = open(path)
    lineas = file.readlines()
    numero = len(lineas)
    for x in range((numero-lines), numero):
        print(lineas[x],end=' ')


if len(sys.argv) < 2:
    print("Faltan argumentos")
else:
    if str(sys.argv[1].split('=')[0]) == "--file":
        try:
            if str(sys.argv[2].split('=')[0]) == "--lines":
                tail(sys.argv[1].split('=')[1], int(sys.argv[2].split('=')[1]))
            else:
                print("Formato de argumentos incorrecto")
        except:
            tail(sys.argv[1].split('=')[1], 10)
    else:
        print("Formato de argumentos incorrecto")