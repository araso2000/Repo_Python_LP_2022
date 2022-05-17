#Eje 12

def format_sort_records(lista):
    texto = "Asistentes:\n"
    for elemento in lista:
        texto = texto + str(elemento[1])[0:11] + "\t" + str(elemento[0])[0:11] + "\t" + str(round(elemento[2],2)) + "\n"
    print(texto)


PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]
format_sort_records(PEOPLE)
