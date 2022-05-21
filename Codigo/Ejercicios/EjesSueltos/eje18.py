#Eje 18

def passToDict(path):
    file = open(path)
    lineas = file.readlines()
    users = []
    numId = []
    diccionario = {}
    for x in lineas:
        users.append(str(x.splitlines()[0].split(':')[0]))
        numId.append(str(x.splitlines()[0].split(':')[2]))

    for x in range(len(users)):
        diccionario[users[x]] = numId[x]
    print(diccionario)

passToDict("./ficheros/passwd.txt")