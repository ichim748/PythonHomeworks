import random
import sys
import time

import pygame

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('background_photo.jpg')
moved = [False]
blocked_tiles = [0]
mouse_moves = [0]


class Tile(pygame.sprite.Sprite):
    def __init__(self, tip, x, y, i, j):
        super().__init__()
        self.tip = tip
        self.i = i
        self.j = j
        self.sprites = []
        self.sprites.append(pygame.image.load('default_tile.png'))
        self.sprites.append(pygame.image.load('on_hover_tile.png'))
        self.sprites.append(pygame.image.load('blocked_tile.png'))
        self.sprites.append(pygame.image.load('mouse_tile.png'))
        if self.tip == 0:
            self.image = self.sprites[0]
        elif self.tip == 1:
            self.image = self.sprites[1]
        elif self.tip == 2:
            self.image = self.sprites[2]
        else:
            self.image = self.sprites[3]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        if self.tip == 0:
            self.image = self.sprites[0]
        elif self.tip == 1:
            self.image = self.sprites[1]
        elif self.tip == 2:
            self.image = self.sprites[2]
        else:
            self.image = self.sprites[3]

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and (self.tip == 0 or self.tip == 1):
            self.tip = 2
            moved[0] = True
            blocked_tiles[0] += 1

    def check_hover(self, mouse):
        if self.rect.collidepoint(mouse):
            if self.tip == 0 or self.tip == 1:
                self.tip = 1
        elif self.tip == 1:
            self.tip = 0


def grid_position_to_coordinates(x, y):
    if x % 2 == 0:
        a = 173 + y * 56
        b = 27 + x * 53
        return a, b
    else:
        a = 200 + y * 56
        b = 27 + x * 53
        return a, b


tile_group = pygame.sprite.Group()
tile_matrix = []

for i in range(11):
    temp = []
    for j in range(11):
        coordinates = grid_position_to_coordinates(i, j)
        if i == 5 and j == 5:
            mouse_position = [i, j]
            tile = Tile(3, coordinates[0], coordinates[1], i, j)
            tile_group.add(tile)
            temp.append(tile)
        else:
            tile = Tile(0, coordinates[0], coordinates[1], i, j)
            tile_group.add(tile)
            temp.append(tile)
    tile_matrix.append(temp)


def mouse_won():
    return mouse_position[0] == 0 or mouse_position[0] == 10 or mouse_position[1] == 0 or mouse_position[1] == 10


def player_won():
    if 0 < mouse_position[0] < 10 and 0 < mouse_position[1] < 10:
        if tile_matrix[mouse_position[0]][mouse_position[1]-1].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]+1].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]+1].tip == 2 \
                and tile_matrix[mouse_position[0]][mouse_position[1]+1].tip == 2:
            return True


def mouse_move():
    found = False
    while not found:
        optiune_x = random.randint(-1, 1)
        optiune_y = random.randint(-1, 1)
        if (optiune_x, optiune_y) in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            if tile_matrix[mouse_position[0]+optiune_x][mouse_position[1]+optiune_y].tip != 2:
                if not found:
                    found = True
                    tile_matrix[mouse_position[0]][mouse_position[1]].tip = 0
                    tile_matrix[mouse_position[0] + optiune_x][mouse_position[1] + optiune_y].tip = 3
                    mouse_position[0] += optiune_x
                    mouse_position[1] += optiune_y


while not mouse_won() and not player_won():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in tile_group:
                i.check_click(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            for i in tile_group:
                i.check_hover(event.pos)

    if not player_won() and moved[0] and blocked_tiles[0] > mouse_moves[0]:
        moved[0] = False
        mouse_moves[0] += 1
        mouse_move()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    tile_group.draw(screen)
    tile_group.update()
    clock.tick(60)
else:
    if mouse_won():
        print('The mouse won')
    else:
        print('The player won')
