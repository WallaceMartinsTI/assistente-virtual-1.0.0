from falas_fixas import iniciando, informe_credenciais
from time import sleep
import getpass


def inicio():
    iniciando()
    sleep(1.2)
    informe_credenciais()


def login():
    credenciais = getpass.getpass('Credenciais: ')
    if credenciais == 'Wallace15975':
        return True
    else:
        return False
