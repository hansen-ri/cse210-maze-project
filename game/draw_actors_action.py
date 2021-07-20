from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_players(cast)
        self._draw_tiles(cast)
        self._draw_goals(cast)
        self._draw_timer(cast)
        self._draw_label(cast)
        
    def _draw_players(self, cast):
        for player in cast.get_actors("players"):
            player.draw()

    def _draw_tiles(self, cast):
        for tile in cast.get_actors("tiles"):
            tile.draw()
    
    def _draw_goals(self, cast):
        for goal in cast.get_actors("goals"):
            goal.draw()
    
    def _draw_timer(self, cast):
        for timer in cast.get_actors("timers"):
            timer.draw()

    def _draw_label(self, cast):
        for label in cast.get_actors("label"):
            label.draw()