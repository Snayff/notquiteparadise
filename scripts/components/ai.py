import tcod

from random import randint


class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):

        monster = self.owner
        #if tcod.map_is_in_fov(fov_map, monster.x, monster.y):

            # # if monster in attack range then attack, else move
            # if monster.distance_to(target) >= 2:
            #     create_event(global_data.event_hub, Event(EntityEventNames.MOVE_ASTAR, EventTopics.ENTITY, [self,
            #         target]))
            # # monster.move_astar(target, entities, game_map)
            #
            # elif target.living.hp > 0:
            #     create_event(global_data.event_hub, Event(EntityEventNames.ATTACK, EventTopics.ENTITY, [self, target]))
            # # monster.living.attack(target)

    def to_json(self):
        json_data = {
            'name': self.__class__.__name__
        }

        return json_data

    @staticmethod
    def from_json():
        basic_monster = BasicMonster()

        return basic_monster


class ConfusedMonster:
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        if self.number_of_turns > 0:
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1

            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)

            self.number_of_turns -= 1
        else:
            self.owner.ai = self.previous_ai
           # results.append({'message': Message('The {0} is no longer confused!'.format(self.owner.name), tcod.red)})

        return results

    def to_json(self):
        json_data = {
            'name': self.__class__.__name__,
            'previous_ai': self.previous_ai.__class__.__name__,
            'number_of_turns': self.number_of_turns
        }

        return json_data

    @staticmethod
    def from_json(json_data, owner):
        previous_ai_name = json_data.get('previous_ai')
        number_of_turns = json_data.get('number_of_turns')

        if previous_ai_name == 'BasicMonster':
            previous_ai = BasicMonster()
            previous_ai.owner = owner
        else:
            previous_ai = None

        confused_monster = ConfusedMonster(previous_ai, number_of_turns)

        return confused_monster
