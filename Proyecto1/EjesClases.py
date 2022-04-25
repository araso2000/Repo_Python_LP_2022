import datetime

def shellsMasUsadas():
    file = open("./res/passwd.txt")
    lineas = file.readlines()
    file.close()

    resultado = "Shells más usadas v3\n\n"

    for line in lineas:
        if line.split(':')[6] not in resultado:
            resultado += "-> "
            resultado += line.split(':')[6]

    try:
        file2 = open("./res/resultado.txt", "w")
        file2.writelines(resultado)
        file2.flush()
        file2.close()

    except FileNotFoundError:
        file2 = open("./res/resultado.txt", "x")
        file2.writelines(resultado)
        file2.flush()
        file2.close()

def ultimosTreintaFB():
    file = open("./res/FB.csv")
    lineas = file.readlines()
    file.close()

    resultado = "Ultimos 30 dias\n\n"

    today = datetime.date.today()
    treinta = datetime.date.today() + datetime.timedelta(-30)

    print(today.day)

    print()

    for line in lineas[1:]:
        print(line.split(',')[0].split('-')[2])

    try:
        file2 = open("./res/resultado.txt", "w")
        file2.writelines(resultado)
        file2.flush()
        file2.close()

    except FileNotFoundError:
        file2 = open("./res/resultado.txt", "x")
        file2.writelines(resultado)
        file2.flush()
        file2.close()

ultimosTreintaFB()