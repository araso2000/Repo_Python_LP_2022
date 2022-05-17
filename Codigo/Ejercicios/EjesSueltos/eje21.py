#Eje 21

def copyfile(origen, *destinos):
    file = open(("./ficheros/" + origen))
    lineas = file.readlines()

    for x in destinos:
        try:
            file2 = open(("./ficheros/" + x))
            file2.write(lineas)
            file2.flush()
            file2.close()
        except FileNotFoundError:
            file2 = open(("./ficheros/" + x), "x")
            file2.writelines(lineas)
            file2.flush()
            file2.close()

    print("Copia completada!")

copyfile("origen.txt","copia1.txt","copia2.txt")