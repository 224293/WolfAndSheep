import logging


class Wolf:
    x_position = 0.0
    y_position = 0.0
    wolf_move_dist = None

    def __init__(self, wolf_move_dist):
        self.wolf_move_dist = wolf_move_dist
        log = "Info level: Setting wolf move distance: " + str(wolf_move_dist)
        logging.info(log)

    def move(self, x, y):
        self.x_position += x
        self.y_position += y
        log = "Info level: Wolf moving about: " + str(x) + " " + str(y)
        logging.info(log)
        log = "Debug level: Wolf move"
        logging.debug(log)

    def set_wolf_position(self, x, y):
        self.x_position = x
        self.y_position = y
        log = "Info level: Setting wolf position: " + str(x) + " " + str(y)
        logging.info(log)
        log = "Debug level: set_wolf_position"
        logging.debug(log)
