import pygame

red = (200, 0, 0)
azul = (50, 100, 213)
dimensao = (400, 400)

tela = pygame.display.set_mode((dimensao))
pygame.display.set_caption('Cobrinha')

tela.fill(azul)

clock = pygame.time.Clock()


def desenho_cobra():
    pygame.draw.rect(tela, red, [300, 200, 20, 20])


while True:
    pygame.display.update()
    desenho_cobra()
    # mover_cobra()
    clock.tick(5)
