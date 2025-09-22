import pygame
from pygame.locals import *
import os

pygame.init()
sizee = (width, height) = (600, 600)
screen = pygame.display.set_mode(sizee)
# insertion de l'image de fond
fond = pygame.transform.scale(pygame.image.load("game.jpg").convert(), sizee)

# insertion du stickman + animation
stickman_sprite = [
    pygame.transform.scale(
        pygame.image.load(os.path.join("fighter_sprites", f"fighter_walk_00{i}.png")).convert_alpha(),
        (300, 300)
    )
    for i in range(10, 17)
]

# créer une horloge pour tracker le temps
clock = pygame.time.Clock()
# FPS
FPS = 5
value = 0

screen.blit(fond, (0, 0))
running = True
while running:
    clock.tick(FPS)

    if value == 6:
        screen.blit(stickman_sprite[value], (-50, 100))
        value = 0
    else:
        screen.blit(stickman_sprite[value], (-50, 100))
        value += 1

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_q) or event.type == QUIT:
            running = False
    pygame.display.update()


pygame.quit() 