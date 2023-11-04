import pygame
from .entity import entity

class enemy(entity):
    def __init__(self, window, position, size):
        super().__init__(position, size)
        self.window = window

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.window, (192, 57, 43), (self.get_x, self.get_y, self.get_width, self.get_height))