from scripts.core import global_data
from scripts.core.constants import LoggingEventTypes, GameStates
from scripts.events.game_events import ChangeGameStateEvent
from scripts.events.logging_events import LoggingEvent


class TurnManager:
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

    def build_new_turn_queue(self):
        from scripts.core.global_data import game_manager, entity_manager
        log_string = f"Building a new turn queue."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))

        # create a turn queue from the entities list
        for entity in entity_manager.entities:
            if entity.ai or entity == entity_manager.player:
                self.turn_queue[entity] = entity.actor.time_of_next_action

        # get the next entity in the queue
        self.turn_holder = min(self.turn_queue, key=self.turn_queue.get)

    def end_turn(self, spent_time):
        from scripts.core.global_data import game_manager
        entity = self.turn_holder

        log_string = f"Ending {entity.name}'s turn."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))

        #  update actor's time spent
        entity.actor.spend_time(spent_time)

        self.next_turn()

    def next_turn(self):
        from scripts.core.global_data import game_manager

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
        if self.turn_holder == global_data.entity_manager.player:
            game_manager.create_event(ChangeGameStateEvent(GameStates.PLAYER_TURN))
        # if turn holder is not player and we aren't already in enemy turn then update to enemy turn
        elif game_manager.game_state != GameStates.ENEMY_TURN:
            game_manager.create_event(ChangeGameStateEvent(GameStates.ENEMY_TURN))

        log_string = f"It is now {self.turn_holder.name}'s turn."
        game_manager.create_event(LoggingEvent(LoggingEventTypes.INFO, log_string))
