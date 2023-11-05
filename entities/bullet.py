import pygame
from .entity import entity

class bullet(entity):
    def __init__(self, window, position, size, player_width):
        super().__init__(position, size)

        self.window = window

        #center to player width
        self.set_x(self.get_x + player_width / 2 - self.get_width / 2)
        self.set_y(position[1] - 10)

    def update(self):
        #move bullet up
        self.set_y(self.get_y - 8)

    def draw(self):
        pygame.draw.rect(self.window, (46, 204, 113), self.rect)

    #return True if bullet is out of window
    @property
    def out_of_window(self):
        if self.get_y + self.get_height <= 0:
            return True
        return False