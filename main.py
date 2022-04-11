import pygame
import sys

lst = []
img = pygame.image.load('car.png')

a = 0
while a < 570:
    a += 30
    lst.append(((a, 0), (a, 600)))
lst2 = []

a = 0
while a < 570:
    a += 30
    lst2.append(((0, a), (600, a)))
lst3 = (lst + lst2)


class Grille:

    def __init__(self, ecran):
        self.ecran = ecran
        self.lignes = lst3

    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (100, 100, 100), ligne[0], ligne[1], 2)


class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('ex.1')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)

    def fonction_principale(self):
        step = 1
        p1 = 10
        p2 = 10
        while self.jeu_encours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.ecran.fill((200, 200, 200))
            self.grille.afficher()
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_LEFT]:
                p1 -= step
            if key_input[pygame.K_UP]:
                p2 -= step
            if key_input[pygame.K_RIGHT]:
                p1 += step
            if key_input[pygame.K_DOWN]:
                p2 += step
            self.ecran.blit(img, (p1, p2))
            pygame.display.update()
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
