import pygame
from pygame import sprite

class Player(sprite.Sprite):
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.moving_left = False
        self.moving_right = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def get_player_input(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.moving_left = True
            if e.key == pygame.K_RIGHT:
                self.moving_right = True

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                self.moving_left = False
            if e.key == pygame.K_RIGHT:
                self.moving_right = False

    def update(self):
        if self.moving_left and not self.moving_right:
            self.x -= self.speed
        elif self.moving_right and not self.moving_left:
            self.x += self.speed 
        
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
