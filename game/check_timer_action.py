from core.action import Action


class CheckTimerAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        pass
        # timer = cast.first_actor("timers")
 #       timer.tick()
 #       print(timer.get_time())