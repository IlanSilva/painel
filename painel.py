from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import uuid
from relatorio import Relatorio


def alerta_console(txt):
    print('='*40)
    print(str(txt).upper().center(40))
    print('='*40)


class Painel:
    def __init__(self):
        # CONFIGURACOES
        self._options = ChromeOptions()
        self._options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self._options.add_experimental_option('useAutomationExtension', False)

        self.__logado = False
        self.__alertas_fechados = 0
        self.__driver = Chrome(options=self._options)
        self.__relatorio = Relatorio(uuid.uuid4().hex)

    
    def login(self):
        if self.__logado:
            pass
        else:
            campo_usuario = self.__driver.find_element(By.XPATH, "//*[@data-selenium='auth-acess-input-usuario']")
            campo_usuario.send_keys('92028')
            sleep(0.5)
            campo_senha = self.__driver.find_element(By.XPATH, "//*[@data-selenium='auth-acess-input-senha']")
            campo_senha.send_keys('687211')
            sleep(0.5)
            botao_login = self.__driver.find_element(By.XPATH, "//*[@data-selenium='auth-acess-button-entrar']")
            botao_login.click()
            self.__logado = True
    

    def iniciar(self, url):
        texto_informacao = 'INICIANDO O NAVEGADOR'
        self.__relatorio.registrar_informacao(texto_informacao)
        alerta_console(texto_informacao)
        self.__driver.get(url)
        self.__driver.fullscreen_window()

    
    def busca_alerta(self):
        try:
            WebDriverWait(self.__driver, 3).until(EC.alert_is_present())
            texto_aviso = 'NOVO AVISO ENCONTRADO!'
            alerta_console(texto_aviso)
            self.__relatorio.registrar_aviso(texto_aviso)
            alerta = self.__driver.switch_to.alert
            alerta.accept()
            self.__alertas_fechados += 1
            texto_informacao = f'AVISO FECHADO, TOTAL DE AVISOS FECHADOS: {self.__alertas_fechados}'
            alerta_console(texto_informacao)
            self.__relatorio.registrar_informacao(texto_informacao)
            return True
        except:
            return False


    def recarregar_pagina(self):
        self.__driver.refresh()
        self.__driver.fullscreen_window()
        texto_informacao = 'PÁGINA REINICIADA'.encode("utf-8").decode()
        self.__relatorio.registrar_informacao(texto_informacao)
        alerta_console(texto_informacao)

    