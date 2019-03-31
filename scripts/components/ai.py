from scripts.core.global_data import entity_manager, game_manager


class BasicMonster:
    # TODO create initial AI class, and then derive diff types from that
    def take_turn(self):

        monster = self.owner
        target = entity_manager.player

        from scripts.events.game_events import EndTurnEvent
        game_manager.create_event(EndTurnEvent(20))
        print(f"AI passed turn")

        # if entity_manager.query.distance_between_entities(monster, target) >= 2:
        #     # game_manager.create_event(GetMoveTargetEvent(monster, target))
        #     print(f"You disabled move in AI")
        # else:
        #     target_tile = (target.x, target.y)
        #     # TODO - give monsters skill and let them use them to move and act
        #     print(f"You disabled move in AI")
        #     # game_manager.create_event(MoveEvent(monster, target_tile))
        #
