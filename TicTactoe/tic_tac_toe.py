import pygame

# Tile class
class Tile:
    def __init__(self, i, j):
        self.position = (i, j)
        self.status = 0  # 1 for circle, 2 for cross

    def is_inside_the_tile(self, pos: tuple):
        return (self.position[0] - 0.5 < pos[0] < self.position[0] + 0.5 and
                self.position[1] - 0.5 < pos[1] < self.position[1] + 0.5)

# Tic tac toe class
class TicTacToe:
    def __init__(self, size=200, position=(0, 0), destroy_on_finished=False, transparent_on_finished=False):
        self.size = size

        self.winner = 0
        self.finished = False

        self.position = position

        self.destroy_on_finished = destroy_on_finished
        self.transparent_on_finished = transparent_on_finished

        self.tiles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.tiles.append(Tile(i, j))

        self.matched_tiles = []
        self.occupied_tiles = 0

        self.grid_color = (255, 255, 255)
        self.circle_color = (0, 0, 255)
        self.cross_color = (255, 0, 0)
        self.matched_color = (0, 255, 0)

        self.line_thickness = 5

    def get_tile_from_mouse(self, screen):  # O(n)
        x, y = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()
        offset_center = (x / 2 + self.position[0], y / 2 + self.position[1])

        rel_mouse_pos = (
            (mouse_pos[0] - offset_center[0]) / (self.size * 2 / 3),
            (mouse_pos[1] - offset_center[1]) / (self.size * 2 / 3)
        )

        for tile in self.tiles:
            if tile.is_inside_the_tile(rel_mouse_pos):
                return tile

        return None

    def put_object_on_tile(self, screen, put_circle, tile_index=None):  # when mouse is left-clicked.
        if tile_index is not None:
            clicked_tile = self.tiles[tile_index]
            if clicked_tile and clicked_tile.status == 0:
                if put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2

                self.occupied_tiles += 1
                self.check_game()

                return True
            elif clicked_tile:
                return "occupied"
        else:
            clicked_tile = self.get_tile_from_mouse(screen)
            if clicked_tile and clicked_tile.status == 0:
                if put_circle:
                    clicked_tile.status = 1
                else:
                    clicked_tile.status = 2

                self.occupied_tiles += 1
                self.check_game()

                return True
            elif clicked_tile:
                return "occupied"

        return None

    def check_game(self):
        # vertical
        matched_tiles: list = []
        for i in range(3):
            if self.tiles[i * 3].status == 0:
                continue
            if self.tiles[i * 3].status == self.tiles[1 + i * 3].status and self.tiles[1 + i * 3].status == self.tiles[
                2 + i * 3].status:
                matched_tiles = [self.tiles[i * 3], self.tiles[1 + i * 3], self.tiles[2 + i * 3]]
                break

        # Horizontal
        if len(matched_tiles) == 0:
            for i in range(3):
                if self.tiles[i].status == 0:
                    continue
                if self.tiles[i].status == self.tiles[i + 3].status and self.tiles[i + 3].status == self.tiles[
                    i + 6].status:
                    matched_tiles = [self.tiles[i], self.tiles[i + 3], self.tiles[i + 6]]
                    break

        # diagonal
        if len(matched_tiles) == 0:
            if self.tiles[0].status != 0 and self.tiles[0].status == self.tiles[4].status and self.tiles[4].status == \
                    self.tiles[8].status:
                matched_tiles = [self.tiles[0], self.tiles[4], self.tiles[8]]
            elif self.tiles[2].status != 0 and self.tiles[2].status == self.tiles[4].status and self.tiles[4].status == \
                    self.tiles[6].status:
                matched_tiles = [self.tiles[2], self.tiles[4], self.tiles[6]]

        self.matched_tiles = matched_tiles

        if len(matched_tiles) > 0:
            start_tile = matched_tiles[0]
            self.winner = start_tile.status
            self.finished = True
        elif self.occupied_tiles == len(self.tiles):
            self.finished = True

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
        for tile in self.tiles:
            if tile.status == 1:
                pos = (tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       tile.position[1] * self.size * (2 / 3) + offset_center[1])
                pygame.draw.circle(screen, self.circle_color + (alpha,), pos, self.size / 4, self.line_thickness)

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

        # draw line when game ended
        if len(self.matched_tiles) > 0:
            start_tile = self.matched_tiles[0]
            end_tile = self.matched_tiles[-1]
            start_pos = (start_tile.position[0] * self.size * (2 / 3) + offset_center[0],
                         start_tile.position[1] * self.size * (2 / 3) + offset_center[1])
            end_pos = (end_tile.position[0] * self.size * (2 / 3) + offset_center[0],
                       end_tile.position[1] * self.size * (2 / 3) + offset_center[1])

            pygame.draw.line(
                screen,
                self.matched_color + (alpha,),
                start_pos,
                end_pos,
                width=self.line_thickness
            )

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.mode = None

        self.main_tic_tac_toe = None
        self.mini_tic_tac_toe = None

        self.put_circle_main = True
        self.put_circle_mini = True

    def normal_mode_init(self):
        self.main_tic_tac_toe = TicTacToe(size=150, position=(0,50))
        self.mode = "normal"

    def ultimate_mode_init(self):
        data = {"size": 200, "position": (0,50)}

        tic_tac_toe_objects = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                mini_tic_tac_toe = TicTacToe(size=data["size"]/4, position=(data["size"] * 2/3 * i + data["position"][0], data["size"] * 2/3 * j + data["position"][1]), transparent_on_finished=True)
                tic_tac_toe_objects.append(mini_tic_tac_toe)

        self.main_tic_tac_toe = TicTacToe(size=data["size"], position=data["position"])
        self.mini_tic_tac_toe = tic_tac_toe_objects
        self.mode = "ultimate"

    def input(self):
        if self.main_tic_tac_toe.finished:
            return

        def put_on_main_tile(put_circle: bool = self.put_circle_main):
            has_put = self.main_tic_tac_toe.put_object_on_tile(self.screen, put_circle)
            if has_put and has_put != "occupied":
                self.put_circle_main = not put_circle

        if self.mode == "normal":
            put_on_main_tile()

        elif self.mode == "ultimate":
            for i, t in enumerate(self.mini_tic_tac_toe):
                if t.finished:
                    continue

                has_put_in_tile = t.put_object_on_tile(self.screen, self.put_circle_mini)
                if has_put_in_tile:
                    if has_put_in_tile == "occupied":
                        break

                    self.put_circle_mini = not self.put_circle_mini
                    if t.finished:
                        if t.winner == 1:
                            put_on_main_tile(True)
                        elif t.winner == 2:
                            put_on_main_tile(False)
                        else:
                            put_on_main_tile()

                    break

    def update(self):
        if self.main_tic_tac_toe:
            self.main_tic_tac_toe.draw(self.screen)

        if self.mini_tic_tac_toe:
            for t in self.mini_tic_tac_toe:
                t.draw(self.screen)

            self.main_tic_tac_toe.draw(self.screen)

