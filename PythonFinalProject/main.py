import random
import sys
import time
import pygame

# Initialize the screen
pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# background holds the image necessary for background use
background = pygame.image.load('background_photo.jpg')

# Control variables for determining whether it's the computers turn or not
moved = [False]
blocked_tiles = [0]
mouse_moves = [0]

# Initialize the numerical value for the score, it's font, and it's location
score_value = 20000
font = pygame.font.Font('freesansbold.ttf', 25)
textX = 10
textY = 10


def show_score():
    """
    Writes the message "Score : value" on the screen. value is the current score of the player.
    """
    score = font.render("Score : ", True, (255, 0, 0))
    screen.blit(score, (textX, textY))
    score = font.render(str(score_value), True, (255, 0, 0))
    screen.blit(score, (textX, textY + 25))


class Tile(pygame.sprite.Sprite):
    """
    Holds information about a certain tile from the board.
    x - the x coordinate of the center of the rect.
    y - the y coordinate of the center of the rect.
    tip - the type of tile that it is (free, blocked, hovered-over, with the mouse).
    i - the row inside the tile_matrix
    j - the column inside the tile_matrix
    """
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
        """
        Function meant to update the image of the tile based on it's type
        """
        if self.tip == 0:
            self.image = self.sprites[0]
        elif self.tip == 1:
            self.image = self.sprites[1]
        elif self.tip == 2:
            self.image = self.sprites[2]
        else:
            self.image = self.sprites[3]

    def check_click(self, mouse):
        """
        Change the type of the tile if a click happened on it and if it's clickable.
        :param mouse: The coordinates of the mouse click
        """
        if self.rect.collidepoint(mouse) and (self.tip == 0 or self.tip == 1):
            self.tip = 2
            moved[0] = True
            blocked_tiles[0] += 1
            return True
        return False

    def check_click_with_turn(self, mouse, turn, tiles):
        """
        Change the type of the tile if a click happened on it and if it's clickable. This function is meant to
        differentiate between two human players.
        :param mouse: The coordinates of the mouse click
        :param turn: A control variable determining whose turn is
        :param tiles: The tile matrix
        """
        if turn[0] == 0:
            if self.rect.collidepoint(mouse) and (self.tip == 0 or self.tip == 1):
                self.tip = 2
                moved[0] = True
                blocked_tiles[0] += 1
                turn[0] = 1
                return True
            return False
        else:
            if self.rect.collidepoint(mouse) and (self.tip == 0 or self.tip == 1):
                if mouse_position[0] % 2 == 1:
                    possible_moves = [(-1, 0), (0, -1), (1, 0), (-1, 1), (0, 1), (1, 1)]
                else:
                    possible_moves = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]
                for t in possible_moves:
                    if self.i == mouse_position[0] + t[0] and self.j == mouse_position[1] + t[1]:
                        tiles[mouse_position[0]][mouse_position[1]].tip = 0
                        self.tip = 3
                        mouse_position[0] = self.i
                        mouse_position[1] = self.j
                        break
                turn[0] = 0
                return True
            return False

    def check_hover(self, mouse):
        """
        Change the type of the tile if the hover action happened above this tile.
        :param mouse: The coordinates of the mouse click
        """
        if self.rect.collidepoint(mouse):
            if self.tip == 0 or self.tip == 1:
                self.tip = 1
        elif self.tip == 1:
            self.tip = 0

    def check_hover_with_turn(self, mouse, rand):
        """
        Check if the tile is a valid moved for the current player, and if it is, highlight that tile.
        :param mouse: The coordinates of the mouse click
        :param rand: A control variable determining whose turn is
        """
        if rand[0] == 0:
            if self.rect.collidepoint(mouse):
                if self.tip == 0 or self.tip == 1:
                    self.tip = 1
            elif self.tip == 1:
                self.tip = 0
        else:
            if self.rect.collidepoint(mouse) and (self.tip == 0 or self.tip == 1):
                if mouse_position[0] % 2 == 1:
                    possible_moves = [(-1, 0), (0, -1), (1, 0), (-1, 1), (0, 1), (1, 1)]
                else:
                    possible_moves = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]
                for t in possible_moves:
                    if self.i == mouse_position[0] + t[0] and self.j == mouse_position[1] + t[1]:
                        self.tip = 1
            elif self.tip == 1:
                self.tip = 0


def grid_position_to_coordinates(x, y):
    """
    Return the position inside the tile matrix based on the coordinates.
    :param x: the x coordinate of the tile
    :param y: the y coordinate of the tile
    :return: tuple - (A, B), where A is the line of the tile and B is the column of the tile
    """
    if x % 2 == 0:
        a = 173 + y * 56
        b = 27 + x * 53
        return a, b
    else:
        a = 200 + y * 56
        b = 27 + x * 53
        return a, b


# Initialize the tile group and the tile matrix necessary
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

# The addition of some blocked tiles from the beginning
number = random.randint(5, 10)
impossible_positions = [(5, 5)]
for i in range(number):
    optiune_x = random.randint(0, 10)
    optiune_y = random.randint(0, 10)
    if (optiune_x, optiune_y) not in impossible_positions:
        impossible_positions.append((optiune_x, optiune_y))
        tile_matrix[optiune_x][optiune_y].tip = 2


def mouse_won():
    """
    Checks if the mouse won the game.
    :return: boolean value for whether the mouse has won the game
    """
    return mouse_position[0] == 0 or mouse_position[0] == 10 or mouse_position[1] == 0 or mouse_position[1] == 10


def player_won():
    """
    Checks if the player won the game.
    :return: boolean value for whether the player has won the game
    """
    if 0 < mouse_position[0] < 10 and 0 < mouse_position[1] < 10:
        if mouse_position[0] % 2 == 1 and tile_matrix[mouse_position[0]][mouse_position[1]-1].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]+1].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]+1].tip == 2 \
                and tile_matrix[mouse_position[0]][mouse_position[1]+1].tip == 2:
            return True
        if mouse_position[0] % 2 == 0 and tile_matrix[mouse_position[0]][mouse_position[1]-1].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]].tip == 2 \
                and tile_matrix[mouse_position[0]+1][mouse_position[1]-1].tip == 2 \
                and tile_matrix[mouse_position[0]-1][mouse_position[1]-1].tip == 2 \
                and tile_matrix[mouse_position[0]][mouse_position[1]+1].tip == 2:
            return True


def mouse_move():
    """
    Function that moves the mouse on a random, possible tile.
    """
    found = False
    while not found:
        optiune_x = random.randint(-1, 1)
        optiune_y = random.randint(-1, 1)
        if (optiune_x, optiune_y) in [(-1, 0), (0, -1), (1, 0), (-1, 1), (0, 1), (1, 1)] \
                and mouse_position[0] % 2 == 1 \
                and tile_matrix[mouse_position[0]+optiune_x][mouse_position[1]+optiune_y].tip != 2 \
                and not found:
            found = True
            tile_matrix[mouse_position[0]][mouse_position[1]].tip = 0
            tile_matrix[mouse_position[0] + optiune_x][mouse_position[1] + optiune_y].tip = 3
            mouse_position[0] += optiune_x
            mouse_position[1] += optiune_y
        elif (optiune_x, optiune_y) in [(-1, 0), (0, -1), (1, 0), (1, -1), (0, 1), (-1, -1)] \
                and mouse_position[0] % 2 == 0 \
                and tile_matrix[mouse_position[0]+optiune_x][mouse_position[1]+optiune_y].tip != 2 \
                and not found:
            found = True
            tile_matrix[mouse_position[0]][mouse_position[1]].tip = 0
            tile_matrix[mouse_position[0] + optiune_x][mouse_position[1] + optiune_y].tip = 3
            mouse_position[0] += optiune_x
            mouse_position[1] += optiune_y


def mouse_move_using_dijkstra():
    """
    Function that moves the mouse taking into consideration the closest winning tile and the path towards it.
    """
    unvisited_tiles = [j for i in tile_matrix for j in i if j.tip != 2]
    shortest_path = {}
    previous_node = {}
    for i in unvisited_tiles:
        shortest_path[i] = sys.maxsize
    shortest_path[tile_matrix[mouse_position[0]][mouse_position[1]]] = 0
    while unvisited_tiles:
        current_min = None
        for i in unvisited_tiles:
            if current_min is None:
                current_min = i
            elif shortest_path[i] < shortest_path[current_min]:
                current_min = i

        if current_min.i % 2 == 1:
            neighbours_positions = [(-1, 0), (0, -1), (1, 0), (-1, 1), (0, 1), (1, 1)]
        else:
            neighbours_positions = [(-1, -1), (0, -1), (1, -1), (1, 0), (0, 1), (-1, 0)]
        neighbours = [tile_matrix[current_min.i + t[0]][current_min.j + t[1]] for t in neighbours_positions if
                      0 <= current_min.i + t[0] <= 10 and 0 <= current_min.j + t[1] <= 10 and
                      tile_matrix[current_min.i + t[0]][current_min.j + t[1]].tip != 2]
        for neighbour in neighbours:
            val_curenta = shortest_path[current_min] + 1
            if val_curenta < shortest_path[neighbour]:
                shortest_path[neighbour] = val_curenta
                previous_node[neighbour] = current_min
        unvisited_tiles.remove(current_min)
    costuri_margini = [t for t in shortest_path if t.i == 0 or t.j == 0 or t.i == 10 or t.j == 10]
    cost_minim = shortest_path[costuri_margini[0]]
    tile_cost_minim = costuri_margini[0]
    for i in range(1, len(costuri_margini)):
        if shortest_path[costuri_margini[i]] < cost_minim:
            cost_minim = shortest_path[costuri_margini[i]]
            tile_cost_minim = costuri_margini[i]
    # recreate the path
    path = [tile_cost_minim]
    while not path.__contains__(tile_matrix[mouse_position[0]][mouse_position[1]]):
        path.append(previous_node[path[len(path)-1]])
    tile_matrix[mouse_position[0]][mouse_position[1]].tip = 0
    tile_matrix[path[len(path)-2].i][path[len(path)-2].j].tip = 3
    mouse_position[0] = path[len(path)-2].i
    mouse_position[1] = path[len(path)-2].j


if __name__ == '__main__':
    # Checks if we have gotten one of the computer difficulty expected command line arguments.
    if len(sys.argv) >= 2 and (sys.argv[1] == 'easy' or sys.argv[1] == 'medium' or sys.argv[1] == 'hard'):
        while not mouse_won() and not player_won():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in tile_group:
                        if i.check_click(event.pos):
                            score_value -= 50
                            break
                elif event.type == pygame.MOUSEMOTION:
                    for i in tile_group:
                        i.check_hover(event.pos)
            contor = 0
            """
            Based on whether the game has ended and the difficulty chosen by the user, call the necessary 
            function for the mouse move.
            """
            if not player_won() and moved[0] and blocked_tiles[0] > mouse_moves[0] and sys.argv[1] == 'hard':
                moved[0] = False
                mouse_moves[0] += 1
                mouse_move_using_dijkstra()
            elif not player_won() and moved[0] and blocked_tiles[0] > mouse_moves[0] and sys.argv[1] == 'easy':
                moved[0] = False
                mouse_moves[0] += 1
                mouse_move()
            elif not player_won() and moved[0] and blocked_tiles[0] > mouse_moves[0] and sys.argv[1] == 'medium':
                moved[0] = False
                mouse_moves[0] += 1
                if contor < 1:
                    mouse_move_using_dijkstra()
                    contor += 1
                elif contor < 4:
                    mouse_move()
                    contor += 1
                else:
                    contor = 0
            # Update the image on the screen based on the current state of the tile group
            pygame.display.flip()
            screen.blit(background, (0, 0))
            show_score()
            tile_group.draw(screen)
            tile_group.update()
            clock.tick(60)
        else:
            # If the mouse won, show the appropriate message and end the game
            if mouse_won():
                font = pygame.font.Font('freesansbold.ttf', 35)
                pygame.display.flip()
                screen.blit(background, (0, 0))
                text = font.render("Game Over!", True, (255, 0, 0))
                screen.blit(text, (305, 232))
                text = font.render("The mouse has won!", True, (255, 0, 0))
                screen.blit(text, (240, 232+45))
                text = font.render("Your score was " + str(score_value) + "!", True, (255, 0, 0))
                screen.blit(text, (230, 232+45+45))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                print('The mouse won!')
                sys.exit()
            # If the player won, show the appropriate message and end the game
            else:
                font = pygame.font.Font('freesansbold.ttf', 35)
                pygame.display.flip()
                screen.blit(background, (0, 0))
                text = font.render("You Won!", True, (255, 0, 0))
                screen.blit(text, (315, 232))
                text = font.render("Your score was " + str(score_value) + "!", True, (255, 0, 0))
                screen.blit(text, (210, 232 + 45))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                print('You won!')
                sys.exit()

    # Checks if we have gotten the expected command line arguments for playing human vs. human.
    elif len(sys.argv) >= 2 and sys.argv[1] == 'human':
        turn = [0]
        while not mouse_won() and not player_won():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in tile_group:
                        if i.check_click_with_turn(event.pos, turn, tile_matrix):
                            score_value -= 50
                            break
                elif event.type == pygame.MOUSEMOTION:
                    for i in tile_group:
                        i.check_hover_with_turn(event.pos, turn)
            pygame.display.flip()
            screen.blit(background, (0, 0))
            show_score()
            tile_group.draw(screen)
            tile_group.update()
            clock.tick(60)
        else:
            # If the mouse player won, show the appropriate message and end the game
            if mouse_won():
                font = pygame.font.Font('freesansbold.ttf', 35)
                pygame.display.flip()
                screen.blit(background, (0, 0))
                text = font.render("The mouse player won!", True, (255, 0, 0))
                screen.blit(text, (210, 232 + 45))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                print('The mouse player won!')
                sys.exit()
            # If the human player won (mouse catching player), show the appropriate message and end the game
            else:
                font = pygame.font.Font('freesansbold.ttf', 35)
                pygame.display.flip()
                screen.blit(background, (0, 0))
                text = font.render("The human player won!", True, (255, 0, 0))
                screen.blit(text, (210, 232 + 45))
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                print('The human player won!')
                sys.exit()
    else:
        # If we received any other command line arguments other than the expected ones.
        if len(sys.argv) >= 2:
            print("The argument you provided ("
                + sys.argv[1]
                + ") is not a valid argument for this application. "
                + "Please try one of the following:\n-easy\n-mediu\n-hard\n-human")
        else:
            print("Please try one of the following command line arguments:\n-easy\n-mediu\n-hard\n-human")
