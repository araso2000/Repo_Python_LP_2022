#Eje 3
def run_timing():
    contador = 0
    resultado = 0
    while True:
        print("Introduce nuevo tiempo para una carrera de 10 km")
        variable = input()

        if not variable:
            break

        resultado = resultado + float(variable)
        contador = contador+1

    print("Tiempo medio de " + str(contador) + " carreras: " + str(resultado/contador))

#run_timing()