from .entity import entity
from .bullet import bullet
import pygame

class player(entity):
    def __init__(self, window, window_size, position, size):
        super().__init__(position, size)
        self.window = window
        self.window_size = window_size
        self.bullets = []
        self.enemies_destroyed = []

    def shoot(self, player_position):
        #shoot bullets
        self.bullets.append(bullet(self.window, self.window_size, player_position, (4, self.get_height/2), self.get_width))

    def update(self, enemies):
        #get pygame pressed keys
        keys = pygame.key.get_pressed()

        #if key pressed left arrow move player to the left
        if keys[pygame.K_LEFT]:
            self.set_x(self.get_x - 2)
        #if key pressed right arrow move player to the right
        if keys[pygame.K_RIGHT]:
            self.set_x(self.get_x + 2)

        for bullet in self.bullets:
            bullet_collision = self.enemy_hit(enemies, bullet)

            #if bullet out of window remove it
            if bullet.out_of_window:
                self.bullets.remove(bullet)        
            elif bullet_collision[0]:
                self.bullets.remove(bullet)
                self.enemies_destroyed.append(bullet_collision[1])
            else:
                bullet.update()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        pygame.draw.rect(self.window, (255, 255, 255), self.rect)

    
    def enemy_hit(self, enemies, bullet):
        result = []
        for enemy in enemies:
            collided = pygame.Rect.colliderect(bullet.rect, enemy.rect)
            if collided:
                result = [collided, enemy]
        if result:
            return result
        return [False]