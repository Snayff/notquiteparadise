
from random import randint

from scripts.core.constants import EntityEventNames, EventTopics
from scripts.events.entity_events import MoveEvent, GetMoveTargetEvent
from scripts.events.pub_sub_hub import Event
from scripts.core.global_data import game_manager, entity_manager


class BasicMonster:
    def take_turn(self):

        monster = self.owner
        target = entity_manager.player

        if entity_manager.distance_between_entities(monster, target) >= 2:
            game_manager.create_event(GetMoveTargetEvent(monster, target))
        else:
            game_manager.create_event(MoveEvent(monster, target.x, target.y))

        # the original method is below, TODO remove when fov is in
        # if tcod.map_is_in_fov(fov_map, monster.x, monster.y):
            # if monster in attack range then attack, else move
            # monster.move_astar(target, entities, game_map)
            # monster.living.attack(target)
