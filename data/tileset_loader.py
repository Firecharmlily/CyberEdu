import pygame
from data.clip import clip

def load_tileset(path):
    tileset_img = pygame.image.load(path + 'tileset.png').convert()
    tileset_img.set_colorkey((0, 0, 0))
    width = tileset_img.get_width()
    tile_size = [16, 16]
    tile_count = int((width + 1) / (tile_size[0] + 1))
    images = [clip(tileset_img, i * (tile_size[0] + 1), 0, tile_size[0], tile_size[1]) for i in range(tile_count)]
    return images
