from painel import Painel
from os import path
from time import sleep

painel = Painel()
painel.iniciar('http://10.30.5.249/Painel/Privado/Default.aspx')
sleep(2)
painel.login()
while True:
    alerta = painel.busca_alerta()
    if alerta:
        painel.recarregar_pagina()