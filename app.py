import gtts
from playsound import playsound

with open('Frase.txt','r') as arquivo:
    for linha in arquivo:
       Frase = gtts.gTTS(linha,lang='en')
       Frase.save('Frase.mp3')
       playsound('Frase.mp3')