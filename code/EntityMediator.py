from code.Const import WIN_HEIGHT
from code.Entity import Entity
from code.Fish import Fish
from code.Obstacle import Obstacle
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Fish, Obstacle)):
            if ent.rect.top > WIN_HEIGHT :
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if not (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):
            return

        if isinstance(ent1, Player):
            if isinstance(ent2, Obstacle):
                ent1.health -= ent2.damage
                ent1.score = max(0, ent1.score + ent2.score)
                ent2.health = 0
            elif isinstance(ent2, Fish):
                ent1.score += ent2.score
                ent2.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)