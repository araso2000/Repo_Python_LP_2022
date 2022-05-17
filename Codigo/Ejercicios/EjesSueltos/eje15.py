#Eje 15
import os


def extensiones(path):
    dirs = os.listdir(path)
    resultado = ""
    for x in dirs:
        try:
            resultado = resultado + "." + x.split('.')[1] + "     "
        except:
            print(end="")

    print(resultado)

extensiones("C:/Users/araso/Desktop")