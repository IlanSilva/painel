from datetime import datetime
from os import path
from pathlib import Path

import logging
class Relatorio:
    def __init__(self, nome_arquivo):
        self._nome = nome_arquivo
        verifica_existe_pasta_relatorios = path.exists('relatorios')
        if not verifica_existe_pasta_relatorios:
            Path('relatorios').mkdir()
        logging.basicConfig(filename=f'relatorios/{datetime.now().strftime("%d_%m_%y")}_{nome_arquivo}.log', filemode='w', level=logging.INFO,)

    
    def registrar_aviso(self, txt):
        logging.warning(f'{datetime.now().strftime("%d/%m/%y - %H:%M:%S")} | {txt}')
    
    
    def registrar_erro(self, txt):
        logging.error(f'{datetime.now().strftime("%d/%m/%y - %H:%M:%S")} | {txt}')


    def registrar_informacao(self, txt):
        logging.info(f'{datetime.now().strftime("%d/%m/%y - %H:%M:%S")} | {txt}')
