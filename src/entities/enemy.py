import pygame
from pygame import sprite

class Enemy(sprite.Sprite):
    def __init__(self, x, y, x_change, y_change, image):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.x_change = x_change
        self.y_change = y_change
        self.image = image
        self.is_alive = True

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    
    def update(self):
        self.x += self.x_change

        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change

    def reached_bottom(self, player):
        return self.get_rect().colliderect(player.get_rect())
    
    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.is_alive = True

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))