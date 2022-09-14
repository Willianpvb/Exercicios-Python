from tkinter import Button

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
dimensoes = (800, 600)
fonte = pygame.font.SysFont("Arial", 20)
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption("Lista Ligada", "")


def tprint():
    nu = 8 #int(input())
    for i in range(11):
        score = fonte.render("{} vezes {} = {}".format(nu, i, nu * i), True, (255, 255, 255))
        tela.blit(score, [0, i * 20])


bt = Button(tela, width=15, text="Nome")
tela.blit(bt, [0, 140])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tprint()
    pygame.display.update()
