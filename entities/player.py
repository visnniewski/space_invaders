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
        
        self.speed = 3

    def shoot(self):
        #shoot bullets
        self.bullets.append(bullet(self.window, self.window_size, (self.get_x, self.get_y), self.get_width))

    def update(self, enemies):
        #get pygame pressed keys
        keys = pygame.key.get_pressed()

        #if key pressed left arrow move player to the left
        if keys[pygame.K_LEFT] and self.can_move("left"):
            self.set_x(self.get_x - self.speed)
        #if key pressed right arrow move player to the right
        if keys[pygame.K_RIGHT] and self.can_move("right"):
            self.set_x(self.get_x + self.speed)

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

    def can_move(self, dir):
        if dir == "right":
            if self.get_x + self.get_width >= self.window_size[0]:
                self.set_x(self.window_size[0] - self.get_width)
                return False
        elif dir == "left":
            if self.get_x <= 0:
                self.set_x(0)
                return False
        
        return True

    def enemy_hit(self, enemies, bullet):
        result = []
        for enemy in enemies:
            collided = pygame.Rect.colliderect(bullet.rect, enemy.rect)
            if collided:
                result = [collided, enemy]
        if result:
            return result
        return [False]