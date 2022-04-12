import pygame
import sys


lst = []
img = pygame.image.load('assets/car.png')
img2 = pygame.image.load('assets/car2.png')
ing3 = pygame.image.load('assets/balle.png.png')

a = 0
while a < 1170:
    a += 30
    lst.append(((a, 0), (a, 1200)))
lst2 = []

a = 0
while a < 1170:
    a += 30
    lst2.append(((0, a), (1200, a)))
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

        self.ecran = pygame.display.set_mode((1200, 1000))
        pygame.display.set_caption('ex.1')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)

    def fonction_principale(self):

        step = 4

        p1 = 950
        p2 = 830
        p3 = 30
        p4 = 830
        p5 = 370
        p6 = 700

        while self.jeu_encours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.ecran.fill((200, 200, 200))
            self.grille.afficher()
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_LEFT] and p1 >= 0:
                p1 -= step
            if key_input[pygame.K_UP] and p2 >= -50:
                p2 -= step
            if key_input[pygame.K_RIGHT] and p1 <= 980:
                p1 += step
            if key_input[pygame.K_DOWN] and p2 <= 830:
                p2 += step
            #voiture 2 mouvement
            if key_input[pygame.K_q] and p3 >= 0:
                p3 -= step
            if key_input[pygame.K_z] and p4 >= -50:
                p4 -= step
            if (key_input[pygame.K_d]) and p3 <= 980:
                p3 += step
            if key_input[pygame.K_s] and p4 <= 830:
                p4 += step

            self.ecran.blit(img2, (p1, p2))
            self.ecran.blit(img, (p3, p4))
            self.ecran.blit(ing3, (p5, p6))


            pygame.display.update()
            pygame.display.flip()

img = pygame.image.load('assets/car.png')

a = 0
while a < 1170:
    a += 30
    lst.append(((a, 0), (a, 1200)))
lst2 = []

a = 0
while a < 1170:
    a += 30
    lst2.append(((0, a), (1200, a)))
lst3 = (lst + lst2)



if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()





