import pygame

#b
BASE_SPEED = 1

#c
COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

#d
DIFFICULTY_INTERVAL = 50

#e
EVENT_TIMEOUT = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'bg0': 0,
    'bg1': 0.50,
    'bg2': 1,
    'player': 5
}

ENTITY_HEALTH = {
    'bg0': 999,
    'bg1': 999,
    'bg2': 999,
    'otter': 5,
    'obstacles': 1,
    'fish': 1
}

ENTITY_DAMAGE = {
    'bg0': 0,
    'bg1': 0,
    'bg2': 0,
    'otter': 0,
    'obstacles': 1,
    'fish': 0
}

ENTITY_SCORE = {
    'bg0': 0,
    'bg1': 0,
    'bg2': 0,
    'otter': 0,
    'obstacles': -20,
    'fish': 10
}

#m
MENU_OPTION = ('NEW GAME',
             'SCORE',
             'EXIT')

MAX_DIFFICULTY = 10

#t
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 25000

#s
SPAWN_INTERVAL = 2000

#w
WIN_WIDTH = 600
WIN_HEIGHT = 480