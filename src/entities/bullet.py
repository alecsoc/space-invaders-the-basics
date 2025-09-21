import pygame
from pygame import sprite

class Bullet(sprite.Sprite):
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.is_active = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def fire(self, x, y, player_img):
        if not self.is_active:
            player_width = player_img.get_width()
            bullet_width = self.image.get_width()
            bullet_height = self.image.get_height()

            self.x = x + (player_width - bullet_width) // 2
            self.y = y - bullet_height

            self.is_active = True

    def update(self):
        if self.is_active:
            self.y -= self.speed
            if self.y <= 0:
                self.is_active = False
    
    def draw(self, surface):
        if self.is_active:
            surface.blit(self.image, (self.x, self.y))