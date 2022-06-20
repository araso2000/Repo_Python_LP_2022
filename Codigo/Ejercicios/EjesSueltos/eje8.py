#Eje 8

def zipCasero(lista1,*listas):
    union = []
    for y in listas:
        for x in range(len(y)):
            union.append((lista1[x:x+1:1],y[x:x+1:1]))
    print(union)

zipCasero([10, 20,30],'abc','hola','patimicola')