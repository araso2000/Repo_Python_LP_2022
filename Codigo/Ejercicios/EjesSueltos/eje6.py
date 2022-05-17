#Eje 6

def sumaParesImpares(lista):
    sumaPar = 0
    sumaImpar = 0
    for numero in lista[1::2]:
        sumaPar += numero
    for numero in lista[0::2]:
        sumaImpar += numero
    print("Suma de los pares (" + str(lista[1::2]) + "): " + str(sumaPar) + "\nSuma de los impares (" + str(lista[0::2]) + "): " + str(sumaImpar))

sumaParesImpares([10,20,30,40,50,60,45,23,456,3456,3456,2345,345,7654,34567,5,4567,434567,867645,458,65636,67,5557876,745437,65745,5347,58,55,3765,634,76,8546,468,56632,554,745,6435,756,6,756,745,64,7456,4,74,4537,467,437,4537,453734,5473457])