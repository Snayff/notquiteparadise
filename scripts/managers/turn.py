from scripts.core import global_data
from scripts.core.constants import LoggingEventTypes, GameStates
from scripts.events.game_events import ChangeGameStateEvent
from scripts.events.logging_events import LoggingEvent


class TurnManager:
    """
    Manager of turns functions.
    """
    # TODO What do we need from the turn queue?
    #  Add all entities that are within X range of the player;
    #  Add new entities to the queue as they get into range;
    #  Amend an entities position in the queue;
    #  Keep track of rounds;

    def __init__(self):
        self.turn_holder = None
        self.turn_queue = {}  # (entity, time)
        self.round = 0
        self.time = 0
        self.time_of_last_turn = 0

        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, f"TurnManager initialised."))

    def build_new_turn_queue(self):
        """
        Build a new turn queue for all entities
        """
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, f"Building a new turn queue..."))

        # create a turn queue from the entities list
        from scripts.core.global_data import world_manager
        entities = world_manager.entity_existence.get_all_entities()

        for entity in entities:
            if entity.ai or entity == world_manager.player:
                self.turn_queue[entity] = entity.actor.time_of_next_action

        # get the next entity in the queue
        self.turn_holder = min(self.turn_queue, key=self.turn_queue.get)

        # log result
        queue = []
        for entity, time in self.turn_queue.items():
            queue.append((entity.name, time))

        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, f"-> Queue built. {queue}"))

    def end_turn(self, spent_time):
        """
        End the current turn and apply time spent

        Args:
            spent_time:
        """
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG, f"Ending {self.turn_holder.name}'s turn..."))

        entity = self.turn_holder

        #  update actor's time spent
        entity.actor.spend_time(spent_time)

        self.next_turn()

    def next_turn(self):
        """
        Proceed to the next turn setting the next entity to act as the turn holder.
        """
        from scripts.core.global_data import game_manager
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, f"Moving to the next turn..."))

        if not self.turn_queue:
            self.build_new_turn_queue()

        # update turn holders time of next action
        self.turn_queue[self.turn_holder] = self.turn_holder.actor.time_of_next_action

        # get the next entity in the queue
        self.turn_holder = min(self.turn_queue, key=self.turn_queue.get)

        # update time using last action and when new turn holder can act
        self.time += self.turn_holder.actor.time_of_next_action - self.time_of_last_turn
        self.time_of_last_turn = self.time

        # if turn holder is the player then update to player turn
        from scripts.core.global_data import world_manager
        if self.turn_holder == world_manager.player:
            game_manager.create_event(ChangeGameStateEvent(GameStates.PLAYER_TURN))
        # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
        elif game_manager.game_state != GameStates.ENEMY_TURN:
            game_manager.create_event(ChangeGameStateEvent(GameStates.ENEMY_TURN))

        game_manager.create_event(LoggingEvent(LoggingEventTypes.DEBUG,
                                               f"-> It is now {self.turn_holder.name}'s turn."))
