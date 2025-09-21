import pygame

class Scoreboard:
    def __init__(self, font_path, font_size, color, start_score = 0, pos = (10, 10)):
        self.score = start_score
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color
        self.pos = pos

    def add_points(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def draw(self, surface):
        text_surface = self.font.render(f"Score: {self.score}", True, self.color)
        surface.blit(text_surface, self.pos)