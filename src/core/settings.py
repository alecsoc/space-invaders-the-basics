import os

class Settings:
    def __init__(self):
        # Screen
        self.TITLE = f"Space Invaders: The Basics"
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 60

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BG_COLOR = (41, 60, 94)

        self.ASSET_DIR = "assets"

        self.IMAGES = {
            "background": os.path.join(self.ASSET_DIR, "images", "galaxy-bg.png"),
            "player":     os.path.join(self.ASSET_DIR, "images", "space-ship.png"),
            "enemy":      os.path.join(self.ASSET_DIR, "images", "alien.png"),
            "bullet":     os.path.join(self.ASSET_DIR, "images", "bullet.png"),
            "icon":       os.path.join(self.ASSET_DIR, "images", "ufo.png"),
        }

        self.SOUNDS = {
            "main_theme":  os.path.join(self.ASSET_DIR, "sounds", "music", "SITB-Theme.wav"),
            "shoot":     os.path.join(self.ASSET_DIR, "sounds", "sfx", "shoot-ship.wav"),
            "explosion": os.path.join(self.ASSET_DIR, "sounds", "sfx", "hit-enemy.wav"),
        }

        self.FONTS = {
            "pixel": os.path.join(self.ASSET_DIR, "fonts", "score_text.ttf")
        }

        # Game parameters
        self.PLAYER_X = 365
        self.PLAYER_Y = 480
        self.PLAYER_SPEED = 6
        self.BULLET_SPEED = 10

        self.ENEMY_X_CHANGE = 1.5
        self.ENEMY_Y_CHANGE = 30
        self.ENEMY_ROWS = 3
        self.ENEMY_COLS = 6
        self.ENEMY_SPACING_X = 70
        self.ENEMY_SPACING_Y = 60
        self.ENEMY_OFFSET_X = 100
        self.ENEMY_OFFSET_Y = 50
        self.COLLISION_RADIUS = 27