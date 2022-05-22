#Eje para probar POO en Python

class clase1:
    def __init__(self,precio):
        self.precio=precio

    def getPrecio(self):
        return self.precio

    def setPrecio(self,precio):
        self.precio=precio

    def quitarIVA(self):
        return (self.precio - (self.precio*0.21))

