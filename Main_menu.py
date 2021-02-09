import pygame
import data.engine as engine
import data.text as text

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Aeroblaster')
screen = pygame.display.set_mode((894, 594), 0, 32)
display = pygame.Surface((300, 200))

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

splash_image = engine.load_img("Title_of_Game_1")
cursor = engine.load_img("cursor")

font = text.generate_font('data/font/small_font.png', engine.font_dat, 5, 8, (255, 255, 255))

while True:
    click = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mx = int(mx / 3)
    my = int(my / 3)

    # displays splash image
    display.fill((0, 0, 0))
    display.blit(splash_image, (25, 0))

    # creates start button
    display.fill((34, 23, 36), (60, 125, 50, 25))
    if 110 > mx > 60 and 150 > my > 125:
        display.fill((104, 93, 106), (60, 125, 50, 25))
        if click[0] == 1:
            exec(open("Aeroblaster.py").read())
    text.show_text('start', 68, 130, 1, 9999, font, display, 2)

    # creates end button
    display.fill((34, 23, 36), (200, 125, 50, 25))
    if 250 > mx > 200 and 150 > my > 125:
        display.fill((104, 93, 106), (200, 125, 50, 25))
        if click[0] == 1:
            quit()
    text.show_text('end', 215, 130, 1, 9999, font, display, 2)

    engine.blit_center(display, cursor, (mx, my))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()

    # scales surface to game window
    screen.blit(pygame.transform.scale(display, (900, 600)), (-6, -6))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
