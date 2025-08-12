import pygame
from code.Level import Level
from code.Menu import Menu
from code.Score import Score
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return:
                    score.save(level.player.score)
            elif menu_return == MENU_OPTION[1]:
                score.show()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass