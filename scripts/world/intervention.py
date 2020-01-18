from scripts.core.constants import MessageTypes
from scripts.events.ui_events import MessageEvent
from scripts.core.library import library
from scripts.core.event_hub import publisher
from scripts.world.god import God


class Intervention:
    """
    An intervention to be used by a god

    Attributes:
            name(str):
            owner(God):
    """
    def __init__(self, owner, intervention_name):
        self.owner = owner  # type: God
        self.name = intervention_name

        # TODO - add cooldown

    def use(self, target_pos):
        """
        Use the intervention

        Args:
            target_pos (tuple): x y of the target
        """
        from scripts.managers.world_manager import world
        data = library.get_god_intervention_data(self.owner.name, self.name)

        target_x, target_y = target_pos

        coords = world.Skill.create_shape(data.shape, data.shape_size)
        effected_tiles = world.Map.get_tiles(target_x, target_y, coords)

        # apply any effects
        for effect_name, effect_data in data.effects.items():
            world.Skill.apply_effect(effect_data.effect_type, data.name, effected_tiles)

        # logging
        tile = world.Map.get_tile((target_x, target_y))
        entity = world.Map.get_entity_on_tile(tile)
        msg = f"#col.info {self.owner.name} intervened, using {self.name} on {entity.name}."
        publisher.publish(MessageEvent(MessageTypes.LOG, msg))
