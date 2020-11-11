import webbrowser as wb
from datetime import date, datetime
from utils import reproduz_audio_fixo
from time import sleep


# Páginas Web
def abrir_youtube():
    reproduz_audio_fixo('audios/abrindo_youtube.mp3')
    sleep(1.5)
    wb.open_new_tab('www.youtube.com.br')


def abrir_facebook():
    reproduz_audio_fixo('audios/abrindo_facebook.mp3')
    sleep(1.5)
    wb.open_new_tab('www.facebook.com.br')


def abrir_vagas():
    reproduz_audio_fixo('audios/abrindo_vagas.mp3')
    sleep(1.5)
    wb.open_new_tab('www.vagas.com.br')


def abrir_chrome():
    reproduz_audio_fixo('audios/abrindo_chrome.mp3')
    sleep(1.5)
    wb.open('chrome')


# Outros
def horas_atual():
    horas = datetime.now().hour
    minutos = datetime.now().minute
    segundos = datetime.now().second
    horario_atual = f'{horas}:{minutos}:{segundos}'
    return horario_atual


def data_atual():
    pass


def aguardando_ordem():
    reproduz_audio_fixo('audios/aguardando_ordem.mp3')
    sleep(2)
