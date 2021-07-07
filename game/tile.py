from core.actor import Actor
from game import constants


class Tile(Actor):

    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture = constants.TILE_STONE
        self.scale = constants.TILE_SCALE
        