import pygame, sys
from entities.player import player

class space_invaders:
    def __init__(self, window_size):
        pygame.init()
        self.window_size = window_size

        #create window and set it caption
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Space Invaders")

        #init player
        self.player = player(self.window, [0, 0], [30, 30])
        
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
        self.player.update()

    def draw(self):
        self.window.fill((0, 0, 0), (0, 0, self.window_size[0], self.window_size[1]))
        self.player.draw()
        pygame.display.update()

if __name__ == "__main__":
    game = space_invaders((480, 360))
    game.game_loop()
    