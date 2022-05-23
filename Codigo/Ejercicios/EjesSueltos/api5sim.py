#api5sim

import requests
import time

token = ''
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

        while (len(getSMS(respuesta['id'])['sms'])==0):
            print("Esperando SMS...")
            time.sleep(5)

        sms = getSMS(respuesta['id'])
        print(sms)
        print(f"      ->Codigo: {sms['sms'][0]['code']}\n      ->Texto: {sms['sms']['text']}")

        print("Quieres otro telefono? 1-SI / 0-NO")
        opt = int(input())
    print("ADIOS")