import pygame

class menu(object):
    def __init__(self, window, window_size):
        self.window = window
        self.window_size = window_size

        self.buttons = [button(self.window, [self.window_size[0] / 2 - 150, 100], (300, 60), "Start", (142, 68, 173))]

    def update(self):
        pass

    def draw(self):
        for button in self.buttons:
            button.draw()

class button(object):
    def __init__(self, winodw, position, size, text, color):
        self.window = winodw
        self.position = position
        self.size = size
        self.text = text
        self.color = color

        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
    
    @property
    def get_x(self):
        return self.rect.x
    
    @property
    def get_y(self):
        return self.rect.y
    
    @property
    def get_width(self):
        return self.rect.width
    
    @property
    def get_height(self):
        return self.rect.height