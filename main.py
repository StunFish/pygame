import pygame
import sys

lst = []

a = 0
while a < 570:
    a += 30
    lst.append(((a, 0), (a, 600)))
print(lst)
lst2 = []

a = 0
while a < 570:
    a += 30
    lst2.append(((0, a), (600, a)))
print(lst2)
lst3 = (lst + lst2)


class Grille:

    def __init__(self, ecran):
        self.ecran = ecran
        self.lignes = lst3

    def afficher(self):
        for ligne in self.lignes:
            pygame.draw.line(self.ecran, (0, 0, 0), ligne[0], ligne[1], 2)


class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('ex.1')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)

    def fonction_principale(self):

        while self.jeu_encours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.ecran.fill((240, 240, 240))
            self.grille.afficher()

            pygame.display.flip()


if __name__ != '__main__':
    pass
else:
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
