import pygame
import sys
from pygame.locals import*
img = pygame.image.load('car.jpg')
pygame.init()
fps=30
fpsclock=pygame.time.Clock()
sur_obj=pygame.display.set_mode((600,600))
pygame.display.set_caption("Keyboard_Input")
White=(255,255,255)
p1=10
p2=10
step=15
while True:
    sur_obj.fill(White)

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        p1 -= step
    if key_input[pygame.K_UP]:
        p2 -= step
    if key_input[pygame.K_RIGHT]:
        p1 += step
    if key_input[pygame.K_DOWN]:
        p2 += step
    sur_obj.blit(img, (p1, p2))
    pygame.display.update()
    fpsclock.tick(fps)