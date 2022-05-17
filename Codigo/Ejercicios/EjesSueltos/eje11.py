#Eje 11

def repeLetras(cadena):
    lista = cadena.splitlines()[0].split(' ')
    diccionario = {}
    ii = 0
    for palabras in lista:
        for letra in palabras[0::1]:
            if diccionario.get(letra) == 0:
                diccionario[letra]=1
            else:
                diccionario[letra]+=1
    print(diccionario)

repeLetras(str(input()))
