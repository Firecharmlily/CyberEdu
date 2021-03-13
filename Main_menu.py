import pygame
import data.engine as engine
import data.text as text
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Aeroblaster')
screen = pygame.display.set_mode((894, 594), 0, 32)
display = pygame.Surface((300, 200))

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

splash_image = engine.load_img("Title_of_Game")
cursor = engine.load_img("cursor")

font = text.generate_font('data/font/small_font.png', engine.font_dat, 5, 8, (255, 255, 255))

name = ""
text_active = False

# start button positioning
startx = 60
starty = 125
start_width = 50
start_height = 25

# end button positioning
endx = 200
endy = 125
end_width = 50
end_height = 25

# name entry positioning
namex = 90
namey = 165
name_width = 120
name_height = 25
text_offset = 0

while True:
    click = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mx = int(mx / 3)
    my = int(my / 3)

    # displays splash image
    display.fill((0, 0, 0))
    display.blit(splash_image, (0, 0))

    # creates start button
    start_button = engine.Button(startx, starty, start_width, start_height, font, "start", display)
    if start_button.check_button(mx, my, click):
        sys.argv = ["text", name]
        exec(open("Aeroblaster.py").read())

    # creates end button
    end_button = engine.Button(endx, endy, end_width, end_height, font, "end", display)
    if end_button.check_button(mx, my, click):
        quit()

    # creates name entry box
    display.fill((34, 23, 36), (namex, namey, name_width, name_height))
    if namex + name_width > mx > namex and namey + name_height > my > namey:
        display.fill((104, 93, 106), (namex, namey, name_width, name_height))
        if click[0] == 1:
            text_active = True
    else:
        if click[0] == 1:
            text_active = False
    text.show_text(name[text_offset:], 90, 170, 1, name_width, font, display, 2)

    # displays cursor on screen
    engine.blit_center(display, cursor, (mx, my))

    # obtains button inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == KEYDOWN:
            if text_active:
                if event.key == pygame.K_RETURN or event.key == K_ESCAPE:
                    text_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                    if text_offset > 0:
                        text_offset -= 1
                else:
                    name += event.unicode
                    if engine.get_text_width(name, 1, font) * 2 > name_width:
                        text_offset += 1

            elif event.key == K_ESCAPE:
                quit()

    # scales surface to game window
    screen.blit(pygame.transform.scale(display, (900, 600)), (-6, -6))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
