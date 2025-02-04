from gtts import gTTS
from playsound import playsound

# Texto que você quer converter em áudio
texto = "bosta de cachorro"

# Idioma do texto (pt = português)
language = 'de'

# Cria o objeto gTTS com o texto e o idioma
sp = gTTS(text=texto, lang=language, slow=False)

# Salva o áudio em um arquivo MP3
audio_file = "audio.mp3"
sp.save(audio_file)

# Reproduz o arquivo de áudio
playsound(audio_file)