import pygame
from datetime import datetime
from msilib.schema import Font
from pygame import Surface
from pygame.locals import Rect
from code.Const import COLOR_ORANGE, WIN_WIDTH, COLOR_YELLOW, COLOR_WHITE
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./gameSprites/score.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.db = DBProxy('jogo_lontra')

    def save(self, player_score):
        name = ""
        font = pygame.font.SysFont("Lucida Sans Typewriter", 25)
        input_active = True

        while input_active:
            self.window.fill((0, 105, 148))
            self.score_text(40, "Type your name (3 letters):", COLOR_ORANGE, (WIN_WIDTH // 2, 150))

            name_surface = font.render(name, True, COLOR_WHITE)
            name_rect = name_surface.get_rect(center=(WIN_WIDTH // 2, 200))
            pygame.draw.rect(self.window, COLOR_WHITE, name_rect.inflate(20, 10), 2)
            self.window.blit(name_surface, name_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 3:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.unicode.isalpha() and len(name) < 3:
                        name += event.unicode.upper()

        self.db.save({
            'name': name,
            'score': player_score,
            'date': datetime.now().strftime('%d/%m/%Y')
        })

        self.window.blit(self.surf, self.rect)
        self.score_text(40, "SCORE SAVED!", COLOR_YELLOW, (WIN_WIDTH // 2, 100))
        self.score_text(30, f"{name}: {player_score}", COLOR_WHITE, (WIN_WIDTH // 2, 200))

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
            pygame.display.flip()

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(40, "HIGH SCORES", COLOR_ORANGE, (WIN_WIDTH / 2, 80))

        scores = self.db.retrieve_top10()

        y_pos = 150
        for idx, score in enumerate(scores):
            _, name, points, date = score
            self.score_text(20, f"{idx + 1}. {name}: {points} - {date}", COLOR_WHITE, (WIN_WIDTH // 2, y_pos))
            y_pos += 30

        self.score_text(20, "Press ENTER to continue", COLOR_WHITE, (WIN_WIDTH // 2, y_pos + 20))

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.db.close()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)