textoEntrada = str(input())
print(f"{textoEntrada} \n\n")
todasPalabras = textoEntrada.split(' ')
print(f"{todasPalabras} \n\n")
palabrasUnicas = []
contador = 0

for x in todasPalabras:
    if x not in palabrasUnicas:
        palabrasUnicas.append(x)
        contador += 1

print(f"Numero de palabras DIFERENTES en total: {contador}\n\nLista de palabras sueltas:\n {palabrasUnicas}")