#Eje 8

def zipCasero(lista1,lista2):
    union = []
    for x in range(len(lista1)):
        union.append(((lista1[x:x+1:1]),lista2[x:x+1:1]))
    print(union)

zipCasero([10, 20,30],'abc')