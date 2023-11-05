import pygame, sys
# from entities.player import player
# from entities.enemy import enemy
from scenes.scene_manager import scene_manager

class space_invaders:
    def __init__(self, window_size):
        pygame.init()
        self.window_size = window_size

        #create window and set it caption
        self.window = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Space Invaders")

        self.scene_manager = scene_manager(self.window, self.window_size)

        self.running = True

    def game_loop(self):
        #init pygame clock
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT + 1, 500)
        can_shoot = True
        timer_event = pygame.USEREVENT + 1
        #start game loop
        while self.running:
            #look for events in pygame
            for event in pygame.event.get():
                #end loop when window is closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                elif event.type == timer_event and can_shoot == False:
                    can_shoot = True
                #shoot bullet (its not in player class because i could get key up only here)
                elif event.type == pygame.KEYUP and can_shoot:
                    if event.key == pygame.K_SPACE and self.scene_manager.get_scene_name == "game":
                        self.scene_manager.scene.player.shoot()
                        can_shoot = False

            #if statement to remove lag when closing window
            if self.running != False:
                self.update()
                self.draw()
                clock.tick(60)

        sys.exit()

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.window.fill((0, 0, 0), (0, 0, self.window_size[0], self.window_size[1]))

        self.scene_manager.draw()

        pygame.display.update()

if __name__ == "__main__":
    game = space_invaders((580, 700))
    game.game_loop()
    