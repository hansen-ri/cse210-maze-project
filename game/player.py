from core.actor import Actor
from game import constants


class Player(Actor):

    IDLE = "idle"
    JUMPING = "jumping"
    FALLING = "falling"
    WALKING = "walking"

    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture = constants.PLAYER_IDLE
        self.scale = constants.TILE_SCALE
        self._current_frame = 0
        self._texture_index = 0
        
    # def move_left(self):
    #     if not self._is_jumping and not self._is_falling:
    #         self.change_x = -constants.MOVEMENT_SPEED
    #         self.change_y = 0

    # def move_right(self):
    #     if not self._is_jumping and not self._is_falling:
    #         self.change_x = constants.MOVEMENT_SPEED
    #         self.change_y = 0

    # def halt_left(self):
    #     self.change_x = 0

    # def halt_right(self):
    #     self.change_x = 0

    # def update(self):
    #     self.center_x += self.change_x
    #     self.center_y += self.change_y

        
    # def jump(self):
    #     if not self._is_jumping:
    #         self._is_jumping = True
    #         self._is_walking = False
    #         self.change_y = constants.PLAYER_JUMP_SPEED
    
    # def walk(self):
    #     self._is_jumping = False
    #     self._is_walking = True
    #     self.change_y = 0
        
    # def update(self):
    #     self._update_position()
    #     self._check_jumping()
    #     self._check_walking()
    #     self._check_falling()
        
    # def _check_falling(self):
    #     if self.change_y < -1:
    #         self.texture = constants.PLAYER_FALLING

    # def _check_jumping(self):
    #     if self.change_y > 0:
    #         self.texture = constants.PLAYER_JUMPING

    # def _check_walking(self):
    #     if self._is_walking:
    #         self._current_frame += 1
    #         if self._current_frame >= constants.PLAYER_ANIMATION_RATE:
    #             num_textures = len(constants.PLAYER_WALKING)
    #             self._current_frame = 0
    #             self._texture_index = (self._texture_index + 1) % num_textures
    #             self.texture = constants.PLAYER_WALKING[self._texture_index]

    # def _update_position(self):
    #     self.change_y = self.change_y - constants.GRAVITY   
    #     self.change_x = min(0, self.change_x - constants.FRICTION)
    #     self.center_y += self.change_y
    #     self.center_x += self.change_x