

class Actor:
    """
    Component: entity can move and interact
    """
    def __init__(self):
        self.time_of_next_action = 0

    def move(self, target_x, target_y):
        # Move the entity to a specified tile
        self.owner.x = target_x
        self.owner.y = target_y

    def spend_time(self, time_spent):
        self.time_of_next_action += time_spent
