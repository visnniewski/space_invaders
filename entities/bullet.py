import pygame
from .entity import entity

class bullet(entity):
    def __init__(self, window, window_size, position, player_width, dir="up", color=(46, 204, 113)):
        self.size = (4, 15)
        super().__init__(position, self.size)

        self.window = window
        self.window_size = window_size
        self.dir = dir
        self.color = color

        #center to player width
        self.set_x(self.get_x + player_width / 2 - self.get_width / 2)
        self.set_y(position[1] - 10)

    def update(self):
        #move bullet up
        if self.dir == "up":
            self.set_y(self.get_y - 8)
        elif self.dir == "down":
            self.set_y(self.get_y + 8)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    #return True if bullet is out of window
    @property
    def out_of_window(self):
        if self.get_y + self.get_height <= 0 or self.get_y >= self.window_size[1]:
            return True
        return False