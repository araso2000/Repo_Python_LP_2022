#Eje 7

def sumaResta(lista: object):
    operacion = 0 #0 es suma y 1 es resta
    suma = lista[0]
    for x in range(1,len(lista)):
        if operacion == 0:
            suma = suma + lista[x]
            operacion = 1
        else:
            suma = suma - lista[x]
            operacion = 0
    print(suma)

sumaResta([10, 20, 30, 40, 50,60])