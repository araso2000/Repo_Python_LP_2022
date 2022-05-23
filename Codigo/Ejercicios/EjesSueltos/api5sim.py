#api5sim

import requests
import time

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ4NTEwNjAsImlhdCI6MTY1MzMxNTA2MCwicmF5IjoiZmYxMzI2Nzg4ODI2OWFjYTJmNGIzZjNmNzRmMzAzMTciLCJzdWIiOjM0NTkwMH0.Sr0T-ww6VJ_XCgArJdhPyUsbzlgksVM7OfEvlD3tjoOWToAiroQ2AWuBH-HHcjJNDZ7kof-a0GhD8DvPvaRI19C4YJj8ysgOAz30u5uGTwKp-LpaSgSjGVPRu0aNuH-Yo1ehrnWiaysBiE19ey7d4Uby6cf09ETWex2gkh2oRf-y5maQ-1uVl_RETPkA2ks_LeNIx8AQ9puiIi90Eu3z7DvaktmHVP3XEh6fGJEpLR_egurFXRd7mNbxwxH9NQ2UhoUbRE8gnQngzfdNGGccuHvzzC5T3RD4eFjFFPIZakHNNcNkwOrPAn9KOO6XXZmOG3zP3F_5QBMv7WVjX1gwmA'
headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}

def comprar(producto):
    return requests.get('https://5sim.net/v1/user/buy/activation/' + "spain" + '/' + "any" + '/' + str(producto) ,headers=headers).json()

def saludar():
    print(f"Hola {requests.get('https://5sim.net/v1/user/profile', headers=headers).json()['email']}")

def cancelarPedido(idPedido):
    return requests.get('https://5sim.net/v1/user/cancel/' + str(idPedido), headers=headers)["status"]

def getSMS(idPedido):
    return requests.get('https://5sim.net/v1/user/check/' + str(idPedido), headers=headers).json()


if __name__ == "__main__":
    print(f"Script de Python para comprar en 5-Sim")
    saludar()
    opt = 1
    while(opt!=0):
        print(f"Introduce el producto a comprar")
        producto = str(input())
        print(f"Vas a comprar <{producto}>")
        respuesta = comprar(producto)
        print(f"Telefono: {respuesta['phone']} - Precio: {respuesta['price']}")

        while (getSMS(respuesta['id'])['status'] != "RECEIVED"):
            print("Esperando SMS...")
            time.sleep(5)

        sms = getSMS(respuesta['id'])
        print(sms)
        #print(f"      ->Codigo: {sms['sms.code']}\n      ->Texto: {sms['sms.text']}")

        print("Quieres otro telefono? 1-SI / 0-NO")
        opt = int(input())
    print("ADIOS")