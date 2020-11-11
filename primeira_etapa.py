import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from random import randint


def reproduz_audio(path):
    playsound(path)


# Funcao responsavel por falar
def cria_audio(input_audio):
    audio = input_audio
    n_random = randint(1, 999999999)
    file_path = 'audio-' + str(n_random) + '.mp3'
    while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        count = 0
        try:
            tts = gTTS(audio, lang='pt-BR')
            tts.save(file_path)
            reproduz_audio(file_path)
            os.remove(file_path)
        except Exception:
            if count % 2 == 0:
                print('Processando..')
            elif count % 3 == 0:
                print('Processando...')


def ouvir_microfone():
    # Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        # Avisa ao usuario que esta pronto para ouvir
        print('Diga alguma coisa: ')
        # Armazena a informação de audio na variavel
        audio = microfone.listen(source)
        try:
            # Passa o audio para o reconhecedor de padroes(speech_recognition)
            frase = microfone.recognize_google(audio, language='pt-BR')
            # Após alguns segundos, retorna a frase falada
            print("Você disse: " + frase)

        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            print("Não entendi")
    return frase


frase = ouvir_microfone()
cria_audio(frase)
