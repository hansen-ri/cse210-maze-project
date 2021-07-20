import arcade
from core.actor import Actor
from game import constants

class Label(Actor):
    def __init__(self, center_x, center_y):
            super().__init__()
            self.center_x = center_x
            self.center_y = center_y
            self.scale = constants.TILE_SCALE

    def draW(self):
            arcade.draw_text("Game Over!!!", 100, 100, arcade.color.BLUE, 80)