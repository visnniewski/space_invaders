import pygame, sys
from entities.player import player
from entities.enemy import enemy

class space_invaders:
    def __init__(self, window_size):
        pygame.init()
        self.window_size = window_size

        #create window and set it caption
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Space Invaders")

        #init player
        self.player = player(self.window, [0, 0], [30, 30])
        self.enemies = []
        self.create_enemies_fleet()
        
        #set player position
        self.player.set_x(self.window_size[0] / 2 - self.player.get_width / 2)
        self.player.set_y(self.window_size[1] - self.player.get_height * 3)

        self.running = True

    def game_loop(self):
        #init pygame clock
        clock = pygame.time.Clock()

        #start game loop
        while self.running:
            #look for events in pygame
            for event in pygame.event.get():
                #end loop when window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                #shoot bullet (its not in player class because i could get key up only here)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot([self.player.get_x, self.player.get_y])

            #if statement to remove lag when closing window
            if self.running != False:
                self.update()
                self.draw()
                clock.tick(60)

        sys.exit()

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
        self.window.fill((0, 0, 0), (0, 0, self.window_size[0], self.window_size[1]))
        self.player.draw()

        #draw all enemies
        for enemy in self.enemies:
            enemy.draw()

        pygame.display.update()

    def create_enemies_fleet(self):
        start_x = 66
        for i in range(0, 10):
            for j in range(0, 6):
                self.enemies.append(enemy(self.window, [start_x + 42 * i, 20 + 42 * j], [30, 30]))

if __name__ == "__main__":
    game = space_invaders((540, 600))
    game.game_loop()
    