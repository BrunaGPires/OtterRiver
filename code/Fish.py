from code.Entity import Entity
import random


class Fish(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.base_speed = random.randint(1, 3)
        self.speed = self.base_speed

    def move(self):
        self.rect.y += self.speed