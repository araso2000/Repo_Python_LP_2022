#Eje 13

def menu():
    diccionario = {"polla":10,"pene":20}
    total=0;
    opt = 0
    while(opt == 0):
        print("Consultar: ", end=" ")
        plato = str(input())
        plato = plato.lower()
        if diccionario.get(plato):
            total = total + diccionario.get(plato)
            print(plato + " cuesta " + str(diccionario.get(plato)) + ", el total es de: " + str(total))
        elif plato == "" :
            opt = 1
        else:
            print("Ese plato no está disponible")
    print("La cuenta total asciende a: " + str(total))

menu()
