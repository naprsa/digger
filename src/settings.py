import os

# Color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game settings
WIDTH = 1024  # 16 * 64 / 32 * 32 / 64 * 16
HEIGHT = 768  # 16 * 48 / 32 * 24 / 64 * 12
FPS = 50
CAPTION = "Digger"
BGCOLOR = DARKGREY

# Dirs
BASE_DIR = os.path.dirname(__file__)
MAPS_DIR = os.path.join(BASE_DIR, "assets", "maps")
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")

TILESIZE = 50
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 200
PLAYER_ROT_SPEED = 100
PLAYER_IMAGE = os.path.join(
    IMAGES_DIR, "player", "assets/images/player/digger_front.png"
)
