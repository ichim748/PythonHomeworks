import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('background_photo.jpg')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tip, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('default_tile.png'))
        self.sprites.append(pygame.image.load('on_hover_tile.png'))
        self.sprites.append(pygame.image.load('blocked_tile.png'))
        self.sprites.append(pygame.image.load('mouse_tile.png'))
        if tip == 0:
            self.image = self.sprites[0]
        elif tip == 1:
            self.image = self.sprites[1]
        elif tip == 2:
            self.image = self.sprites[2]
        else:
            self.image = self.sprites[3]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


def grid_position_to_coordinates(x, y):
    if x % 2 == 0:
        a = 200 + y * 54
        b = 27 + x * 44
        return a, b
    else:
        a = 227 + y * 54
        b = 27 + x * 44
        return a, b


tile_group = pygame.sprite.Group()

for i in range(11):
    for j in range(11):
        coordinates = grid_position_to_coordinates(i, j)
        tile_group.add(Tile(0, coordinates[0], coordinates[1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    tile_group.draw(screen)
    clock.tick(60)import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('background_photo.jpg')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tip, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('default_tile.png'))
        self.sprites.append(pygame.image.load('on_hover_tile.png'))
        self.sprites.append(pygame.image.load('blocked_tile.png'))
        self.sprites.append(pygame.image.load('mouse_tile.png'))
        if tip == 0:
            self.image = self.sprites[0]
        elif tip == 1:
            self.image = self.sprites[1]
        elif tip == 2:
            self.image = self.sprites[2]
        else:
            self.image = self.sprites[3]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


def grid_position_to_coordinates(x, y):
    if x % 2 == 0:
        a = 200 + y * 54
        b = 27 + x * 44
        return a, b
    else:
        a = 227 + y * 54
        b = 27 + x * 44
        return a, b


tile_group = pygame.sprite.Group()

for i in range(11):
    for j in range(11):
        coordinates = grid_position_to_coordinates(i, j)
        tile_group.add(Tile(0, coordinates[0], coordinates[1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    tile_group.draw(screen)
    clock.tick(60)
