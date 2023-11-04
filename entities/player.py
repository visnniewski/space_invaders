from .entity import entity
import pygame

class player(entity):
    def __init__(self, window, position, size):
        super().__init__(position, size)
        self.window = window
        self.bullets = []

    def shoot(self, player_position):
        #shoot bullets
        self.bullets.append(bullet(self.window, player_position, (6, self.get_height/2), self.get_width))

    def update(self):
        #get pygame pressed keys
        keys = pygame.key.get_pressed()

        #if key pressed left arrow move player to the left
        if keys[pygame.K_LEFT]:
            self.set_x(self.get_x - 2)
        #if key pressed right arrow move player to the right
        if keys[pygame.K_RIGHT]:
            self.set_x(self.get_x + 2)

        for bullet in self.bullets:
            #if bullet out of window remove it
            if bullet.out_of_window:
                self.bullets.remove(bullet)
            else:
                bullet.update()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        pygame.draw.rect(self.window, (255, 255, 255), (self.get_x, self.get_y, self.get_width, self.get_height))

class bullet(entity):
    def __init__(self, window, position, size, player_width):
        super().__init__(position, size)

        self.window = window

        #center to player width
        self.set_x(self.get_x + player_width / 2 - self.get_width / 2)
        self.set_y(position[1] - 10)

    def update(self):
        self.set_y(self.get_y - 4)

    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.get_x, self.get_y, self.get_width, self.get_height))

    @property
    def out_of_window(self):
        if self.get_y + self.get_height <= 0:
            return True
        
        return False
