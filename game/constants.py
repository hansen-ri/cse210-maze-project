import arcade

# TILE CONSTANTS
TILE_SCALE = 0.5
TILE_SIZE = 128
TILE_ROWS = 10
TILE_COLUMNS = 15

# SCREEN CONSTANTS
SCREEN_HEIGHT = int(TILE_ROWS * (TILE_SIZE * TILE_SCALE))
SCREEN_WIDTH = int(TILE_COLUMNS * (TILE_SIZE * TILE_SCALE))
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# LEVEL DATA
LEVEL_DATA = "data/levels.json"

# PLAYER TEXTURES
MOVEMENT_SPEED = 5
PLAYER_PATH = ":resources:images/animated_characters/female_person"
PLAYER_IDLE = arcade.load_texture(f"{PLAYER_PATH}/femalePerson_idle.png")

# TILE TEXTURES
TILE_PATH = ":resources:images/tiles"
TILE_STONE = arcade.load_texture(f"{TILE_PATH}/stoneCenter.png")

# EXIT TEXTURES
EXIT_SIGN = arcade.load_texture(":resources:images/tiles/signExit.png")

#TIME CONSTANTS
TIME_SIZE = 128
TIME_ROWS = 20
TIME_COLUMNS = 30
TIME_TOTAL = 0.0

#TIME DISPLAY
minutes = int(TIME_TOTAL) // 60
seconds = int(TIME_TOTAL) % 60
output = f"Time: {minutes:02d}:{seconds:02d}"
