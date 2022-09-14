'''import pygame
pygame.mixer.init()
pygame.mixer.music.load('call-my-name.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()'''

import pygame
pygame.init()
pygame.mixer.music.load('call-my-name.mp3')
pygame.mixer.music.play()
input('Escreva algo para pausar:')
pygame.event.wait()

