import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')
#police
font = pygame.font.Font('freesansbold.ttf', 32)
#ce qui est écrit et couleur
text = font.render('100', True, (0, 0, 0))
#jsp
textRect = text.get_rect()
#position
textRect.center = (350, 350)

while True:

    display_surface.fill(white)

    display_surface.blit(text, textRect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()