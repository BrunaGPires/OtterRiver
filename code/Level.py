import random
import pygame.display
from code.Const import WIN_WIDTH, COLOR_WHITE, WIN_HEIGHT, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, SPAWN_INTERVAL, \
    DIFFICULTY_INTERVAL, MAX_DIFFICULTY, COLOR_ORANGE
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from msilib.schema import Font
from pygame import Surface
from pygame.locals import Rect


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg'))
        self.player = EntityFactory.get_entity('player', (WIN_WIDTH // 2, WIN_HEIGHT - 50))
        self.entity_list.append(self.player)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

        self.difficulty_level = 1
        self.base_spawn_interval = SPAWN_INTERVAL

        for _ in range(3):
            self.entity_list.append(EntityFactory.get_entity('fish'))
        for _ in range(2):
            self.entity_list.append(EntityFactory.get_entity('obstacle'))

    def run(self):
        last_spawn_time = pygame.time.get_ticks()
        clock = pygame.time.Clock()
        running = True

        while running:
            current_time = pygame.time.get_ticks()
            self.update_difficulty()

            current_spawn = max(500, self.base_spawn_interval - (self.difficulty_level * 150))
            if current_time - last_spawn_time > current_spawn:
                self.spawn_entities()
                last_spawn_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True
                if self.difficulty_level >= MAX_DIFFICULTY:
                    running = False

            for ent in self.entity_list:
                ent.move()

            self.window.fill((0, 105, 148))
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)

            self.level_text(20, f"Score: {self.player.score}", COLOR_WHITE, (30, 20))
            self.level_text(20, f"Lives: {self.player.health}", COLOR_WHITE, (30, 45))
            self.level_text(20, f"Timeout: {self.timeout//1000}s", COLOR_WHITE, (WIN_WIDTH - 60, 20))
            self.level_text(20, f'Difficulty: {self.difficulty_level}', COLOR_ORANGE, (40, WIN_HEIGHT - 10))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            clock.tick(60)

            if self.player.health <= 0:
                running = False
        return None

    def update_difficulty(self):
        new_level = 1 + self.player.score // DIFFICULTY_INTERVAL
        if new_level > self.difficulty_level:
            self.difficulty_level = min(MAX_DIFFICULTY, new_level)

    def spawn_entities(self):
        fish_count = sum(1 for e in self.entity_list if e.name == 'fish')
        obstacle_count = sum(1 for e in self.entity_list if e.name == 'obstacle')

        if fish_count < 3 + min(5, self.difficulty_level):
            new_fish = EntityFactory.get_entity('fish', (random.randint(0, WIN_WIDTH), -30))
            new_fish.speed = 1 + (min(10, self.difficulty_level) * 0.3)
            self.entity_list.append(new_fish)
        if obstacle_count < 2 + min(4, self.difficulty_level // 2):
            new_obstacle = EntityFactory.get_entity('obstacle', (random.randint(0, WIN_WIDTH), -50))
            new_obstacle.speed = 1 + (min(10, self.difficulty_level) * 0.2)
            self.entity_list.append(new_obstacle)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)