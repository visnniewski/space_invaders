import pygame

class entity(object):
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])

    #return x pos of entity on window
    @property
    def get_x(self):
        return self.rect.x
    
    #return y pos of entity on window
    @property
    def get_y(self):
        return self.rect.y
    
    #return width of entity
    @property
    def get_width(self):
        return self.size[0]

    #return height of entity
    @property
    def get_height(self):
        return self.size[1]
    
    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y