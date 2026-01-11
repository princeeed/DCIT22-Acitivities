import pygame
# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )

# Tile class
class Tile:
    def __init__(self, i, j):
        self.position = (i,j)
        self.status = 0 # 1 for circle, 2 for cross

    def is_inside_the_tile(self, pos: tuple):
        return (self.position[0] - 0.5 < pos[0] < self.position[0] + 0.5 and
                self.position[1] - 0.5 < pos[1] < self.position[1] + 0.5)

    def reset(self):
        self.status = 0

# Tic tac toe class
class TicTacToe:
    def __init__(self, size=200, position=(0,0), destroy_on_finished=False, transparent_on_finished=False):
        self.size = size

        self.winner = 0
        self.finished = False

        self.position = position

        self.destroy_on_finished = destroy_on_finished
        self.transparent_on_finished = transparent_on_finished

        self.tiles = []
        for i in range(-1,2):
            for j in range(-1,2):
                self.tiles.append(Tile(i, j))

        self.put_circle = True
        
        self.grid_color = (0,0,0)
        self.circle_color = (0,0,255)
        self.cross_color = (255,0,0)
        self.matched_color = (0,255,0)
        
        self.line_thickness = 5

    def get_tile_from_mouse(self, screen): # O(n)
        x, y = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()
        offset_center = (x / 2 + self.position[0], y / 2 + self.position[1])

        rel_mouse_pos = (
            (mouse_pos[0] - offset_center[0]) / (self.size * 2/3),
            (mouse_pos[1] - offset_center[1]) / (self.size * 2/3)
        )

        for tile in self.tiles:
            if tile.is_inside_the_tile(rel_mouse_pos):
                return tile

        return None

    def put_object_on_tile(self, screen, tile_index=None, shape=0): # when mouse is left-clicked.
        if shape != 0:
            if shape == 1:
                self.put_circle = True
            else:
                self.put_circle = False

        if tile_index is not None:
            clicked_tile = self.tiles[tile_index]
            if clicked_tile.status == 0:
                if self.put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2
        else:
            clicked_tile = self.get_tile_from_mouse(screen)
            if clicked_tile and clicked_tile.status == 0:
                if self.put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2


        self.put_circle = not self.put_circle

    def draw(self, screen):
        x, y = screen.get_size()
        offset_center = (x / 2 + self.position[0], y / 2 + self.position[1])

        alpha = 255
        if self.finished and self.transparent_on_finished:
            alpha = 50

        # create grid
        for x in (-1, 1):
            pygame.draw.line(
                screen,
                self.grid_color + (alpha,),
                (self.size * x / 3 + offset_center[0], self.size + offset_center[1]),
                (self.size * x / 3 + offset_center[0], -self.size + offset_center[1]),
                width=self.line_thickness
            )

        for y in (-1, 1):
            pygame.draw.line(
                screen,
                self.grid_color + (alpha,),
                (self.size + offset_center[0], self.size * y / 3 + offset_center[1]),
                (-self.size + offset_center[0], self.size * y / 3 + offset_center[1]),
                width=self.line_thickness
            )

        # create circles or cross on the grid
        occupied_tile_count = 0
        for tile in self.tiles:
            if tile.status == 1:
                pos = (tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       tile.position[1] * self.size * (2 / 3) + offset_center[1])
                pygame.draw.circle(screen, self.circle_color + (alpha,), pos, self.size / 4, self.line_thickness)

                occupied_tile_count += 1

            elif tile.status == 2:
                pos = (tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       tile.position[1] * self.size * (2 / 3) + offset_center[1])
                pygame.draw.line(
                    screen,
                    self.cross_color + (alpha,),
                    (pos[0] + self.size / 4, pos[1] + self.size / 4),
                    (pos[0] - self.size / 4, pos[1] - self.size / 4),
                    width=self.line_thickness
                )
                pygame.draw.line(
                    screen,
                    self.cross_color + (alpha,),
                    (pos[0] - self.size / 4, pos[1] + self.size / 4),
                    (pos[0] + self.size / 4, pos[1] - self.size / 4),
                    width=self.line_thickness
                )

                occupied_tile_count += 1


        #Create line in case tiles are connected
        #vertical
        matched_tiles: list = []
        for i in range(3):
            if self.tiles[i*3].status == 0:
                continue
            if self.tiles[i*3].status == self.tiles[1 + i*3].status and self.tiles[1 + i*3].status == self.tiles[2 + i*3].status:
                matched_tiles = [self.tiles[i*3], self.tiles[1 + i*3], self.tiles[2 + i*3]]
                break

        #Horizontal
        if len(matched_tiles) == 0:
            for i in range(3):
                if self.tiles[i].status == 0:
                    continue
                if self.tiles[i].status == self.tiles[i+3].status and self.tiles[i+3].status == self.tiles[i+6].status:
                    matched_tiles = [self.tiles[i], self.tiles[i+3], self.tiles[i+6]]
                    break

        # diagonal
        if len(matched_tiles) == 0:
            if self.tiles[0].status != 0 and self.tiles[0].status == self.tiles[4].status and self.tiles[4].status == self.tiles[8].status:
                matched_tiles = [self.tiles[0], self.tiles[4], self.tiles[8]]
            elif self.tiles[2].status != 0 and self.tiles[2].status == self.tiles[4].status and self.tiles[4].status == self.tiles[6].status:
                matched_tiles = [self.tiles[2], self.tiles[4], self.tiles[6]]

        if len(matched_tiles) > 0:
            start_tile = matched_tiles[0]
            end_tile = matched_tiles[-1]
            start_pos = (start_tile.position[0] * self.size * (2/3) + offset_center[0],
                       start_tile.position[1] * self.size * (2/3) + offset_center[1])
            end_pos = (end_tile.position[0] * self.size * (2/3) + offset_center[0],
                       end_tile.position[1] * self.size * (2/3) + offset_center[1])

            pygame.draw.line(
                screen,
                self.matched_color + (alpha,),
                start_pos,
                end_pos,
                width=self.line_thickness
            )

            self.winner = start_tile.status
            self.finished = True
        elif occupied_tile_count == len(self.tiles):
            self.finished = True
            

# initialize
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")

draw_surf = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
draw_surf.fill(pygame.Color('#FFFFFF'))

tic_tac_toe_objects = []

main_tic_tac_toe = TicTacToe()

for i in range(-1,2):
    for j in range(-1,2):
        mini_tic_tac_toe = TicTacToe(size=50, position=(133*i, 133*j), transparent_on_finished=True)
        tic_tac_toe_objects.append(mini_tic_tac_toe)

running = True

# loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # main_tic_tac_toe.put_object_on_tile(screen)
            if main_tic_tac_toe.winner == 0:
                for t_obj in tic_tac_toe_objects:
                    if not t_obj:
                        continue
                    t_obj.put_object_on_tile(screen)

    alpha_surface = screen.convert_alpha()
    alpha_surface.fill([0, 0, 0, 0])

    for index, t_obj in enumerate(tic_tac_toe_objects):
        if not t_obj:
            continue

        t_obj.draw(alpha_surface)
        if t_obj and t_obj.finished:
            if main_tic_tac_toe.tiles[index].status == 0:
                main_tic_tac_toe.put_object_on_tile(screen, index, shape=t_obj.winner)
            if t_obj.destroy_on_finished:
                tic_tac_toe_objects[index] = None

    main_tic_tac_toe.draw(alpha_surface)

    screen.fill([255, 255, 255])  # white background
    screen.blit(alpha_surface, (0, 0))

    pygame.display.flip()
# quit
pygame.quit()