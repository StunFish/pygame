import pygame

class Car:

    def __init__(self):
       print('ok')


    def move(self, key_input,  p1, p2, p3, p4, step):


        if key_input[pygame.K_LEFT] and p1 >= 0:
            p1 -= step
        if key_input[pygame.K_UP] and p2 >= -50:
            p2 -= step
        if key_input[pygame.K_RIGHT] and p1 <= 980:
            p1 += step
        if key_input[pygame.K_DOWN] and p2 <= 830:
            p2 += step
        # voiture 2 mouvement
        if key_input[pygame.K_q] and p3 >= 0:
            p3 -= step
        if key_input[pygame.K_z] and p4 >= -50:
            p4 -= step
        if (key_input[pygame.K_d]) and p3 <= 980:
            p3 += step
        if key_input[pygame.K_s] and p4 <= 830:
            p4 += step
        return p1, p2, p3, p4