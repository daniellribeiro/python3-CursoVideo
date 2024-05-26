#Abrir e executar um arquivo mp3

import pygame

pygame.mixer.init()

pygame.mixer.music.load('C:/Users/daniel/Music/Alan Walker - ALONE-1.mp3')

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)