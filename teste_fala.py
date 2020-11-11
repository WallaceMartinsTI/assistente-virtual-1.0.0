import os
from gtts import gTTS
from playsound import playsound
from random import randint

text = 'Agora está funcionando'
n_random = randint(1, 9999999999)
file_path = 'audio-' + str(n_random) + '.mp3'

while not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    try:
        tts = gTTS(text=text, lang='pt-BR')
        tts.save('audios/' + file_path)
        playsound('audios/' + file_path)
        os.remove('audios/' + file_path)
        break
    except Exception:
        print(Exception)  # Mudar para "Processando..."
