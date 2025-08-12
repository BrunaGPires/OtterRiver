import random
from code.Background import Background
from code.Player import Player
from code.Fish import Fish
from code.Obstacle import Obstacle
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'bg{i}', (0, 0)))
                    list_bg.append(Background(f'bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player':
                return Player('otter', position)
            case 'fish':
                return Fish('fish', (random.randint(0, WIN_WIDTH), 0))
            case 'obstacle':
                return Obstacle('obstacles', (random.randint(0, WIN_WIDTH), 0))
        return None