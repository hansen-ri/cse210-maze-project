from core.action import Action
from game.label import Label


class CheckTimerAction(Action,Label):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        timer = cast.first_actor("timers")
        print(timer.ticking)
        if timer.is_ticking():
            timer.tick()
# 600 = 10 seconds
        if timer.total_time >= 900:
            timer.stop()
            Label()
        # timer = cast.first_actor("timers")
 #       timer.tick()
 #       print(timer.get_time())