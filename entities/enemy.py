import pygame
from .entity import entity
from .bullet import bullet

class enemy(entity):
    def __init__(self, window, window_size, position, size):
        super().__init__(position, size)
        self.window = window
        self.window_size = window_size
        self.bullets = []

    def update(self):
        for bullet in self.bullets:
            if bullet.out_of_window:
                self.bullets.remove(bullet)        
            else:
                bullet.update()

    def draw(self):
        pygame.draw.rect(self.window, (192, 57, 43), (self.get_x, self.get_y, self.get_width, self.get_height))
        for bullet in self.bullets:
            bullet.draw()

    def shoot(self):
        self.bullets.append(bullet(self.window, self.window_size, (self.get_x, self.get_y), self.size[0], "down", (230, 126, 34)))