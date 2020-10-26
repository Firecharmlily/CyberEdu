# requires Pygame 2
import pygame

def perfect_outline(img, surf, loc, color, colorkey=(0,0,0), colorkey2=(0,0,0)):
    img.set_colorkey((0,0,0))
    mask = pygame.mask.from_surface(img)
    mask_surf = mask.to_surface(setcolor=color)
    mask_surf.set_colorkey((0, 0, 0))
    surf.blit(mask_surf,(loc[0]-1,loc[1]))
    surf.blit(mask_surf,(loc[0]+1,loc[1]))
    surf.blit(mask_surf,(loc[0],loc[1]-1))
    surf.blit(mask_surf,(loc[0],loc[1]+1))
