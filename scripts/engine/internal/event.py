from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from snecs.typedefs import EntityID

from scripts.engine.internal.constant import DamageTypeType, DirectionType, EventType, PrimaryStatType, UIElement
from scripts.engine.internal.definition import ActorData

__all__ = [
    "event_hub",
    "Subscriber",
    "MoveEvent",
    "DamageEvent",
    "AffectStatEvent",
    "AffectCooldownEvent",
    "AfflictionEvent",
    "AlterTerrainEvent",
    "ExitGameEvent",
    "ExitMenuEvent",
    "NewGameEvent",
    "NewTurnEvent",
    "NewRoundEvent",
    "EndRoundEvent",
    "EndTurnEvent",
    "StartGameEvent",
    "LoadGameEvent",
    "WinConditionMetEvent",
    "MessageEvent"
]


class EventHub:
    """
    Event hub to handle the interactions between events and subscribers
    """

    def __init__(self):
        self.events: List[Event] = []
        self.subscribers: Dict = {}

    def post(self, event: Event):
        """
        Log an event ready for notifying subscribers.
        """
        self.events.append(event)

    def subscribe(self, event_type: EventType, subscriber: Subscriber):
        """
        Register a subscriber with an EventType
        """
        self.subscribers.setdefault(event_type, []).append(subscriber)

    def unsubscribe(self, event_type: EventType, subscriber: Subscriber):
        """
        Remove a subscribers registration to an EventType
        """
        self.subscribers[event_type].remove(subscriber)

    def update(self):
        """
        Notify subscribers of their registered event.
        """

        # loop every event and notify every subscriber
        while self.events:
            event = self.events.pop(0)

            for sub in self.subscribers.get(event.event_type, []):
                sub.process_event(event)


event_hub = EventHub()


class Subscriber(ABC):
    """
    Class to set default behaviour for handlers listening for events
    """

    def __init__(self, name: str):
        self.name: str = name
        self.event_hub: EventHub = event_hub

    def subscribe(self, event_type: EventType):
        self.event_hub.subscribe(event_type, self)

    def unsubscribe(self, event_type: EventType):
        self.event_hub.unsubscribe(event_type, self)

    @abstractmethod
    def process_event(self, event: Event):
        """
        Process game events.
        """
        pass


class Event(ABC):
    """
    Events to cause top level actions to take place
    """

    def __init__(self, event_type: EventType):
        """
        Base class for events
        """
        self.event_type = event_type


######################### INTERACTION EVENTS #########################


class MoveEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, direction: DirectionType, new_pos: Tuple[int, int]):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.direction: DirectionType = direction
        self.new_pos: Tuple[int, int] = new_pos


class DamageEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, amount: int, damage_type: DamageTypeType, remaining_hp: int):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.amount: int = amount
        self.damage_type: DamageTypeType = damage_type
        self.remaining_hp: int = remaining_hp


class AffectStatEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, stat_to_target: PrimaryStatType, amount: int):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.stat_to_target: PrimaryStatType = stat_to_target
        self.amount: int = amount


class AffectCooldownEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, amount: int):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.amount: int = amount


class AfflictionEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, affliction_name: str):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.affliction_name: str = affliction_name


class AlterTerrainEvent(Event):
    def __init__(self, origin: EntityID, target: EntityID, terrain_name: str, duration: int):
        super().__init__(EventType.INTERACTION)

        self.origin: EntityID = origin
        self.target: EntityID = target
        self.terrain_name: str = terrain_name
        self.duration: int = duration


######################### GAME EVENTS #########################


class ExitMenuEvent(Event):
    def __init__(self, menu: UIElement):
        super().__init__(EventType.GAME)

        self.menu: UIElement = menu


class NewGameEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class StartGameEvent(Event):
    def __init__(self, player_data: ActorData):
        super().__init__(EventType.GAME)

        self.player_data: ActorData = player_data


class LoadGameEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class ExitGameEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class WinConditionMetEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class NewTurnEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class EndTurnEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class NewRoundEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class EndRoundEvent(Event):
    def __init__(self):
        super().__init__(EventType.GAME)


class MessageEvent(Event):
    def __init__(self, message: str):
        super().__init__(EventType.GAME)

        self.message = message

