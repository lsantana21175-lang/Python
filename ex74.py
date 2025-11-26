import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mini Arkanoid")
rellotge = pygame.time.Clock()

# Raqueta i pilota
raqueta = pygame.Rect(250, 350, 100, 10)
pilota = pygame.Rect(300, 200, 10, 10)
vel_pilota = [4, -4]
jugant = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jugant = True

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_LEFT]:
        raqueta.x -= 5
    if tecla[pygame.K_RIGHT]:
        raqueta.x += 5

    if jugant:
        pilota.x += vel_pilota[0]
        pilota.y += vel_pilota[1]

    # Col·lisions amb parets
    if pilota.left <= 0 or pilota.right >= 600:
        vel_pilota[0] = -vel_pilota[0]
    if pilota.top <= 0:
        vel_pilota[1] = -vel_pilota[1]
    if pilota.colliderect(raqueta):
        vel_pilota[1] = -vel_pilota[1]

    pantalla.fill((0,0,0))
    pygame.draw.rect(pantalla, (255,0,0), raqueta)
    pygame.draw.ellipse(pantalla, (0,255,0), pilota)
    pygame.display.flip()
    rellotge.tick(60)