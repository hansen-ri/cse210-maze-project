from core.actor import Actor
from game import constants


class Goal(Actor):

    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.scale = constants.TILE_SCALE
        self.texture = constants.EXIT_SIGN
        