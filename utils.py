import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from time import sleep
import os


def estou_ouvindo():
    reproduz_audio_fixo('audios/estou_ouvindo.mp3')


def nao_entendi_repita():
    reproduz_audio_fixo('audios/nao_entendi_repita')


def cria_audio_fixo(audio_fixo, nome_arquivo):
    audio = audio_fixo
    file_path = str(nome_arquivo) + '.mp3'
    while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        try:
            tts = gTTS(audio, lang='pt-BR')
            tts.save('audios/' + file_path)
            break
        except Exception:
            pass


def cria_audio_temporario(input_audio, nome_audio):
    audio = input_audio
    arquivo = nome_audio
    file_path = 'audio-' + str(arquivo) + '.mp3'
    while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        try:
            tts = gTTS(audio, lang='pt-BR')
            tts.save('audios/' + file_path)
            break
        except Exception:
            pass


def reproduz_audio_fixo(path):
    playsound(path)


def reproduz_audio(path):
    while not os.path.exists(path) or os.path.getsize(path) == 0:
        try:
            playsound(path)
            os.remove(path)
            break
        except Exception:
            pass


def ouvir_microfone():
    # Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        # Avisa ao usuario que esta pronto para ouvir
        estou_ouvindo()
        # Armazena a informação de audio na variavel
        audio = microfone.listen(source)
        try:
            # Passa o audio para o reconhecedor de padroes(speech_recognition)
            frase = microfone.recognize_google(audio, language='pt-BR')
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            nao_entendi_repita()
            pass
    return frase


def formatar_pedido(string):
    # Formata colocando tudo minúsculo e removendo todos os espaços
    return string.lower().strip().replace(' ', '')


def encerrar_kronos():
    reproduz_audio_fixo('audios/encerrando_kronos.mp3')


def animacao_encerrar_kronos():
    print("Encerrando.")
    sleep(1)
    print("Encerrando..")
    sleep(1)
    print("Encerrando...")
    sleep(1)
