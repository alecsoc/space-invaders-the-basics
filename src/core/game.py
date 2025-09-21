import pygame
from pygame.event import Event

from core.settings import Settings
from core.soundplayer import SoundPlayer

from hud.scoreboard import Scoreboard
from hud.gameover import GameOverScreen

from entities.player import Player
from entities.enemy import Enemy
from entities.bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.background = pygame.image.load(self.settings.IMAGES["background"])
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.is_game_over = False

        self.player = self.create_player()
        self.enemies = self.create_enemies()
        self.bullet = self.create_bullet()

        self.scoreboard = self.create_scoreboard()
        self.game_over_screen = self.get_game_over_screen()

        self.soundplayer = self.create_sound_player()
        self.soundplayer.play_music(self.settings.SOUNDS["main_theme"])

    def create_scoreboard(self):
        return Scoreboard(
            self.settings.FONTS["pixel"],
            32,
            self.settings.WHITE
        )
    
    def create_sound_player(self):
        return SoundPlayer()
    
    def get_game_over_screen(self):
        return GameOverScreen(
            self.settings.FONTS["pixel"],
            80,
            self.settings.WHITE
        )
    
    def check_game_over(self):
        for enemy in self.enemies:
            if enemy.is_alive and enemy.reached_bottom(self.player):
                self.is_game_over = True
                break

    def reset_game(self):
        self.player = self.create_player()
        self.enemies = self.create_enemies()
        self.bullet = self.create_bullet()
        self.scoreboard = self.create_scoreboard()
        self.is_game_over = False

    def create_player(self):
        return Player(
            self.settings.PLAYER_X, 
            self.settings.PLAYER_Y,
            self.settings.PLAYER_SPEED,
            pygame.image.load(self.settings.IMAGES["player"])
        )
    
    def create_enemies(self):
        enemies = []

        for row in range(self.settings.ENEMY_ROWS):
            for col in range(self.settings.ENEMY_COLS):
                x = self.settings.ENEMY_OFFSET_X + col * self.settings.ENEMY_SPACING_X
                y = self.settings.ENEMY_OFFSET_Y + row * self.settings.ENEMY_SPACING_Y

                enemy = Enemy(
                    x,
                    y,
                    self.settings.ENEMY_X_CHANGE,
                    self.settings.ENEMY_Y_CHANGE,
                    pygame.image.load(self.settings.IMAGES["enemy"])
                )
                
                enemies.append(enemy)

        return enemies
    
    def increase_enemy_speed(self):
        for enemy in self.enemies:
            enemy.x_change += 0.05 if enemy.x_change > 0 else -0.05
    
    def create_bullet(self):
        return Bullet(
            0,
            0,
            abs(self.settings.BULLET_SPEED),
            pygame.image.load(self.settings.IMAGES["bullet"])
        )
    
    def shoot_bullet(self, e: Event):
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            self.bullet.fire(self.player.x, self.player.y, self.player.image)
            self.soundplayer.play_sound(self.settings.SOUNDS["shoot"], 0.15)

    def exit_process(self, e: Event):
        if e.type == pygame.QUIT:
            self.is_running = False

    def retry_process(self, e: Event):
        if self.is_game_over and e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            self.reset_game()

    def handle_events(self):
        for e in pygame.event.get():
            self.exit_process(e)
            self.retry_process(e)

            if not self.is_game_over:
                self.player.get_player_input(e)
                self.shoot_bullet(e)

    def run(self):
        while self.is_running:
            dt = self.clock.tick(self.settings.FPS) / 1000
            current_fps = int(self.clock.get_fps())
            pygame.display.set_caption(f"{self.settings.TITLE} - FPS: {current_fps}")

            self.handle_events()
            self.display.fill(self.settings.BG_COLOR)
            self.display.blit(self.background, (0, 0))

            if not self.is_game_over:
                self.player.update()
                self.player.draw(self.display)

                for enemy in self.enemies:
                    if enemy.is_alive:
                        enemy.update()
                        enemy.draw(self.display)

                for enemy in self.enemies:
                    if enemy.is_alive and self.bullet.is_active:
                        if self.bullet.get_rect().colliderect(enemy.get_rect()):
                            enemy.reset()
                            self.bullet.is_active = False
                            self.scoreboard.add_points(10)
                            self.increase_enemy_speed()
                            self.soundplayer.play_sound(self.settings.SOUNDS["explosion"], 0.25)

                self.bullet.update()
                self.bullet.draw(self.display)

                self.scoreboard.draw(self.display)
                self.check_game_over()
            else:
                self.game_over_screen.draw(self.display)

            pygame.display.flip()

        pygame.quit()