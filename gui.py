import pygame
import math


class Window:

    def __init__(self):
        self.height = 1000
        self.width = 1000

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_white_cell(self, coordinates):
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (coordinates[0] * 10, coordinates[1] * 10, 10, 10))

    def update_display(self, white_cells, isrunning):
        self.screen.fill((0, 0, 0))

        if not isrunning:
            for i in range(1, 101):
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (i * 10, 0), (i * 10, 1000), 1)
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (0, i * 10), (1000, i * 10), 1)

        for element in white_cells:
            self.draw_white_cell(element)
        pygame.display.flip()

    def change_game_mode(self, running, white_cells):
        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                return not running
        return running
        
    def get_clicks(self):
        list_of_clicks = []
        for event in pygame.event.get(eventtype=pygame.MOUSEBUTTONDOWN):
            x = math.floor(event.pos[0] / 10)
            y = math.floor(event.pos[1] / 10)

            list_of_clicks.append((x, y))
        return list_of_clicks
