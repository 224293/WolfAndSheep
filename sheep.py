import logging
from random import choice, uniform


class Sheep:
    x_position = None
    y_position = None
    sheep_move_dist = None
    alive = True

    def __init__(self, init_pos_limit, sheep_move_dist):
        self.x_position = uniform(-init_pos_limit, init_pos_limit)
        self.y_position = uniform(-init_pos_limit, init_pos_limit)
        self.sheep_move_dist = sheep_move_dist
        log = "Info level: Setting sheep details: " + str(self.x_position) + " " + str(self.y_position) + \
              str(self.sheep_move_dist)
        logging.info(log)

    def move(self):
        directions = ("right", "left", "up", "down")
        direction = choice(directions)
        log = "Debug level: Sheep move"
        logging.debug(log)
        log = "Info level: Sheep moving " + direction
        logging.info(log)
        if direction == "right":
            self.y_position += self.sheep_move_dist
            return
        if direction == "left":
            self.y_position -= self.sheep_move_dist
            return
        if direction == "up":
            self.x_position += self.sheep_move_dist
            return
        if direction == "down":
            self.x_position -= self.sheep_move_dist
            return
