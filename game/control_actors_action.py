import arcade
from core.action import Action
from core.cue import Cue
from game import constants


class ControlActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        player = cast.first_actor("players")
        cue_name = cue.get_name()
        cue_info = cue.get_info()
        key = cue_info["key"]

        if cue_name == Cue.ON_KEY_PRESS:
            if key == arcade.key.UP:
                player.change_y = constants.MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                player.change_y = -constants.MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                player.change_x = -constants.MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                player.change_x = constants.MOVEMENT_SPEED
        
        if cue_name == Cue.ON_KEY_RELEASE:
            if key == arcade.key.UP:
                player.change_y = 0
            elif key == arcade.key.DOWN:
                player.change_y = 0
            elif key == arcade.key.LEFT:
                player.change_x = 0
            elif key == arcade.key.RIGHT:
                player.change_x = 0