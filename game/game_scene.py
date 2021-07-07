import json
from core.cast import Cast
from core.cue import Cue
from core.scene import Scene
from core.script import Script
from game import check_timer_action, constants
from game import handle_collisions_action
from game.goal import Goal
from game.player import Player
from game.tile import Tile
from game.timer import Timer
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.move_actors_action import MoveActorsAction
from game.check_timer_action import CheckTimerAction


class GameScene(Scene):

    def __init__(self, level_number = 1):
        
        # create the cast
        cast = Cast()
        with open(constants.LEVEL_DATA) as json_file:
            levels = json.load(json_file)
        level = levels[str(level_number)]

        size = constants.TILE_SIZE * constants.TILE_SCALE
        for row in range(constants.TILE_ROWS):
            for column in range(constants.TILE_COLUMNS):
                center_y = (size * (constants.TILE_ROWS - row)) - (size / 2)
                center_x = (size * column) + (size / 2)

                if level[row][column] == 1:
                    tile = Tile(center_x, center_y)
                    cast.add_actor("tiles", tile)

                elif level[row][column] == 2:
                    player = Player(center_x, center_y)
                    cast.add_actor("players", player)
                    
                elif level[row][column] == 3:
                    goal = Goal(center_x, center_y)
                    cast.add_actor("goals", goal)

        timer = Timer()
        cast.add_actor("timers", timer)

        # create the script
        control_actors_action = ControlActorsAction()
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction()
        check_timer_action = CheckTimerAction()
        draw_actors_action = DrawActorsAction()

        script = Script()
        script.add_action(Cue.ON_KEY_PRESS, control_actors_action)
        script.add_action(Cue.ON_KEY_RELEASE, control_actors_action)
        script.add_action(Cue.ON_UPDATE, move_actors_action)
        script.add_action(Cue.ON_UPDATE, handle_collisions_action)
        script.add_action(Cue.ON_UPDATE, check_timer_action)
        script.add_action(Cue.ON_DRAW, draw_actors_action)
        
        # set the scene
        self.set_cast(cast)
        self.set_script(script)