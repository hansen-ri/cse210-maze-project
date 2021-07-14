from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self):
        super().__init__()
        self._finished = False
        
    def execute(self, cast, cue, callback):
        player = cast.first_actor("players")
        goal = cast.first_actor("goals")
        if arcade.check_for_collision(player, goal) and not self._finished:
            self._finished = True
            # todo: do something useful here instead of printing to console
            print("I made it to the goal!")
            #Hard code level and increment
            current_level = player.level + 1
            scene = callback.get_scene()
            scene.update_level(current_level)
            print(player.level)
            
            