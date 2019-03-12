from scripts.managers.entity_manager_methods.animation_methods import EntityAnimation
from scripts.managers.entity_manager_methods.existence_methods import EntityExistenceAmendment
from scripts.managers.entity_manager_methods.query_methods import EntityQuery


class EntityManager:
    def __init__(self):
        self.entities = []
        self.player = None
        self.query = EntityQuery(self)
        self.existence = EntityExistenceAmendment(self)
        self.animation = EntityAnimation(self)

    def update(self, game_map):
        """
        Update all entity info that requires per frame changes

        Args:
            game_map (GameMap): The current game map
        """
        self.animation.update_entity_sprites(game_map)

















