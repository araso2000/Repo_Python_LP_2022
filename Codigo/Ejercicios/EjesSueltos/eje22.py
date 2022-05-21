#Eje 22

import random

def create_password_generator(cadena):
    def contador(numero):
        lista = []
        password = ""
        for x in cadena:
            lista += x
        for x in range(numero):
            password += random.choice(lista)
        return password
    return(contador)

nueva1 = create_password_generator("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!·$%&/()=?¿|@#~€¬¡'`+´ç,.-^*Ç¨_:;}{][-+*/ºª")

print(nueva1(20))