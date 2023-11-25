from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('desafio21.mp3')
mixer.music.play()
print('Pressione qualquer tecla para parar', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
input('')
