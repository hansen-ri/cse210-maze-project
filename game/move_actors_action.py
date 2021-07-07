import arcade
from core.action import Action


class MoveActorsAction(Action):
    
    def __init__(self):
        super().__init__()
        self._physics_engine = None

    def execute(self, cast, cue, callback):
        player = self._get_player_as_sprite(cast)
        tiles = self._get_tiles_as_spritelist(cast)
        self._move_player_with_arcade(player, tiles)
        
    def _get_player_as_sprite(self, cast):
        return cast.first_actor("players")

    def _get_tiles_as_spritelist(self, cast):
        tiles = cast.get_actors("tiles")
        spritelist = arcade.SpriteList()
        spritelist.extend(tiles)
        return spritelist

    def _move_player_with_arcade(self, player, tiles):
        if self._physics_engine == None:
            self._physics_engine = arcade.PhysicsEngineSimple(player, tiles)
        self._physics_engine.update()