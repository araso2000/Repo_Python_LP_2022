def listing(coleccion):
    listaFinal = []
    for x in range(0,len(coleccion)): listaFinal.append(((x+1),(coleccion[x])))
    return listaFinal

print(listing(["examen", "de", "python"]))