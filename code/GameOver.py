import pygame
import pygame.image
from pygame import Surface
from pygame.locals import Rect
from code.Const import WIN_WIDTH, COLOR_WHITE, COLOR_YELLOW, WIN_HEIGHT, COLOR_RED

class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.surf = pygame.image.load('./gameSprites/score.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.score = score
        self.countdown = 5
        self.last_update_time = pygame.time.get_ticks()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            current_time = pygame.time.get_ticks()

            if current_time - self.last_update_time > 1000:  # 1000ms = 1 segundo
                self.countdown -= 1
                self.last_update_time = current_time

                if self.countdown <= 0:
                    return "Menu"

            self.window.blit(self.surf, self.rect)

            self.game_over_text(60, "GAME OVER", COLOR_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 50))
            self.game_over_text(30, f"Score: {self.score}", COLOR_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20))
            self.game_over_text(25, f"Returning to menu in: {self.countdown}s", COLOR_YELLOW,(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 80))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        return "Menu"

            clock.tick(60)
        return "Menu"

    def game_over_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)