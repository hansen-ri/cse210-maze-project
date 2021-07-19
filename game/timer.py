import arcade
from core.actor import Actor
from game import constants

class Timer(Actor):

        def __init__(self, center_x, center_y):
                super().__init__()
                self.center_x = center_x
                self.center_y = center_y
                self.scale = constants.TILE_SCALE
                self.total_time = 0.0
                self.ticking = False
        
        def draw(self):
                minutes = int(self.total_time) // 60
                seconds = int(self.total_time) % 60
                output = f"Time: {minutes:02d}:{seconds:02d}"
                arcade.draw_text(output, 10, 10, arcade.color.BLUE, 20)

        def start(self):
                self.ticking = True

        def stop(self):
                self.ticking = False

        def tick(self):
                if self.ticking:
                        self.total_time += 1

        def reset(self):
                self.ticking = False
                self.total_time = 0

        def is_ticking(self):
                return self.ticking

        # def on_update(self, delta_time):
        #         """
        #         All the logic to move, and the game logic goes here.
        #         """
        #         self.total_time += delta_time 




#    def __init__(self):
#        self.total_time = 0.0
#
#    def setup(self):
#        """
#        Set up the application.
#        """
#        arcade.set_background_color(arcade.color.BLUE)
#        self.total_time = 0.0
#
#    def on_draw(self):
#        """ Use this function to draw everything to the screen. """

        # Start the render. This must happen before any drawing
        # commands. We do NOT need an stop render command.
#        arcade.start_render()

        # Calculate minutes
#        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
#        seconds = int(self.total_time) % 60

        # Figure out our output
#        output = f"Time: {minutes:02d}:{seconds:02d}"

        # Output the timer text.
#        arcade.draw_text(output, 600, 480, arcade.color.BLACK, 15)
