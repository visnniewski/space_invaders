from .menu import menu
from .game import game
import pygame

class scene_manager(object):
    def __init__(self, window, window_size):
        self.window = window
        self.window_size = window_size
        self.scenes = {"menu": menu(self.window, self.window_size), "game": game(self.window, self.window_size)}
        self.scene_name = "menu"
        self.scene = self.scenes[self.scene_name]

    def change_scene(self, scene):
        self.scene = self.scenes[scene]
        self.scene_name = scene

    def update(self):
        self.scene.update()

    def draw(self):
        self.scene.draw()

    @property
    def get_scene_name(self):
        return self.scene_name