import pygame
from code.Entity import Entity
from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED['player']

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= self.speed
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed
        pass