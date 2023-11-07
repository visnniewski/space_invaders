from entities.player import player
from entities.enemy import enemy
from random import randint

class game(object):
    def __init__(self, window, window_size):
        self.window = window
        self.window_size = window_size

        self.scene = "game"

        #init player
        self.player = player(self.window, self.window_size, [0, 0], [30, 30])
        self.enemies = []
        self.create_enemies_fleet()
        self.enemy_dir = 1

        #set player position
        self.player.set_x(self.window_size[0] / 2 - self.player.get_width / 2)
        self.player.set_y(self.window_size[1] - self.player.get_height * 3)
    
    def update(self):
        self.player.update(self.enemies)

        #remove dead enemy from game
        for enemy_destroyed in self.player.enemies_destroyed:
            self.enemies.remove(enemy_destroyed)
            self.player.enemies_destroyed.remove(enemy_destroyed)

        #update all enemies
        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        self.player.draw()

        #draw all enemies
        for enemy in self.enemies:
            enemy.draw()

    def create_enemies_fleet(self):
        start_x = 86
        start_y = 50
        for i in range(0, 10):
            for j in range(0, 6):
                self.enemies.append(enemy(self.window, self.window_size, [start_x + 42 * i, start_y + 42 * j], [30, 30]))

    def enemy_shoot(self):
        if self.enemies:
            self.enemies[randint(0, len(self.enemies) - 1)].shoot()

    def enemy_move(self):
        move_down = False
        for enemy in self.enemies:
            if enemy.get_x + enemy.get_width >= self.window_size[0] - 30:
                self.enemy_dir = -1
                move_down = True
            if enemy.get_x <= 30:
                self.enemy_dir = 1
                move_down = True

        if move_down:
            for enemy in self.enemies:
                enemy.set_y(enemy.get_y + 8)
        for enemy in self.enemies:
            enemy.set_x(enemy.get_x + 10 * self.enemy_dir)
            
        move_down = False