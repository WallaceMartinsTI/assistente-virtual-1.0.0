from utils import reproduz_audio_fixo
from time import sleep


def iniciando():
    reproduz_audio_fixo('audios/iniciando.mp3')


def informe_credenciais():
    reproduz_audio_fixo('audios/informe_credenciais.mp3')


def login_negado():
    reproduz_audio_fixo('audios/login_negado.mp3')


def login_permitido():
    reproduz_audio_fixo('audios/bv_senhor.mp3')
    sleep(2)
    reproduz_audio_fixo('audios/oque_deseja.mp3')


