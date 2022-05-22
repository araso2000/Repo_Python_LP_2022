#Main

from ejePOO1 import clase1

if __name__ == "__main__":
    objeto = clase1(25)
    print(objeto)
    print(objeto.getPrecio())
    objeto.setPrecio(int(input()))
    print(objeto.getPrecio())
    print(objeto.quitarIVA())