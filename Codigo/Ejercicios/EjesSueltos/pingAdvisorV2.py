#PingAdvisorV2
#Programa que monitoriza mediante ping un servidor y te avisa por email cada 10 testeos si sigue funcionando

import sys
import time
import os
import argparse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import dns.resolver

def ping(host):
    print("Dominio: " + host + " - IPv4: " + str(dns.resolver.resolve(host, 'A')[0]))
    response = os.system("ping -n 1 " + str(dns.resolver.resolve(host, 'A')[0]))

    if response == 0:
        return True
    else:
        return False

def email(texto,host):
    msg = MIMEMultipart()
    msg['Subject'] = "PING -> " + host
    msg.attach(MIMEText(texto,'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login("grooveip634@gmail.com","")

    server.sendmail("grooveip634@gmail.com","",msg.as_string())

    server.quit()

    print("\n\nEmail informativo mandado correctamente\n\n")


parser = argparse.ArgumentParser(description="PingAdvisor: Script de Python que consulta el ping a un host dado por consola y manda un email con el resultado")
parser.add_argument('-host','--direccion_del_host',type=str,help='Introduce la direccion del host',required=True)

args = parser.parse_args()

aciertos = 0
contador = 0
fallos = 0
while(1):
    texto = ""
    if contador == 5:
        if aciertos == contador:
            texto = "\n\nTodos los PING han sido resueltos CORRECTAMENTE.\n\n"
        elif fallos == contador:
            texto = "\n\nTodos los PING han sido resueltos INCORRECTAMENTE.\n\n"
        else:
            texto = "\n\nHan habido " + str(aciertos) + " aciertos y " + str(fallos) + " fallos. \n"
        email(texto,args.direccion_del_host)
        contador = 0
        aciertos = 0
        fallos = 0
    else:
        if ping(str(args.direccion_del_host)):
            aciertos += 1
        else:
            fallos += 1
        contador += 1
        time.sleep(1)
