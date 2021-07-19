import arcade
from core.director import Director
from game import constants
from game.game_scene import GameScene


def main():
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    game_scene = GameScene()
    director = Director(width, height)
    director.direct_scene(game_scene)
    arcade.run()


if __name__ == "__main__":
    main()

        # #1 create label Class
    #   make sure you can set the text
    # #2Inside Check timer action
    # #3Create an instance of Label to to cast
    # #4Set the text to "Game Over"
    # #5Add the Label class to the cast
    # #6Inside the draw_actors_action make sure that it is being drawn

    # #Add a Game Starting Menu ^^