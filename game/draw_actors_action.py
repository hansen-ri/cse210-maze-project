from core.action import Action


class DrawActorsAction(Action):
    
    def __init__(self):
        super().__init__()

    def execute(self, cast, cue, callback):
        self._draw_players(cast)
        self._draw_tiles(cast)
        self._draw_goals(cast)
        
    def _draw_players(self, cast):
        for player in cast.get_actors("players"):
            player.draw()

    def _draw_tiles(self, cast):
        for tile in cast.get_actors("tiles"):
            tile.draw()
    
    def _draw_goals(self, cast):
        for goal in cast.get_actors("goals"):
            goal.draw()