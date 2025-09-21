import pygame

class GameOverScreen:
    def __init__(self, font_path, font_size, color, text = "GAME OVER", sub_text = "Try again? (Press ENTER to continue)"):
        self.font_main = pygame.font.Font(font_path, font_size)
        self.font_sub = pygame.font.Font(font_path, font_size // 2)
        self.color = color
        self.text = text
        self.sub_text = sub_text
    
    def draw(self, surface):
        # main ("GAME OVER" text)
        main_surface = self.font_main.render(self.text, True, self.color)
        main_rect = main_surface.get_rect(midtop=(surface.get_width() // 2, surface.get_height() // 2 - main_surface.get_height()))
        surface.blit(main_surface, main_rect)

        # sub ("try again" text)
        if self.sub_text:
            sub_surface = self.font_sub.render(self.sub_text, True, self.color)
            sub_rect = sub_surface.get_rect(midtop=(main_rect.midbottom[0], main_rect.bottom + 10))
            surface.blit(sub_surface, sub_rect)