#Eje 7

def sumaResta(lista):
    for ii in range(0,6):
        print(lista[ii+1:ii+2:2] + lista[ii:ii+2:2])

    print(lista[1::2])
    print(lista[0::2])


sumaResta([10, 20, 30, 40, 50,60])