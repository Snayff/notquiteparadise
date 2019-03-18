from scripts.core.global_data import game_manager, entity_manager
from scripts.events.entity_events import MoveEvent, GetMoveTargetEvent


class BasicMonster:
    # TODO create initial AI class, and then derive diff types from that
    def take_turn(self):

        monster = self.owner
        target = entity_manager.player

        if entity_manager.query.distance_between_entities(monster, target) >= 2:
            # game_manager.create_event(GetMoveTargetEvent(monster, target))
            print(f"You disabled move in AI")
        else:
            target_tile = (target.x, target.y)
            # TODO - give monsters skill and let them use them to move and act
            print( f"You disabled move in AI")
            # game_manager.create_event(MoveEvent(monster, target_tile))

