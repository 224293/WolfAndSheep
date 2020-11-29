import logging
from math import sqrt

from data import Data
from sheep import Sheep
from wolf import Wolf


class Simulation:
    sheep_list = []
    wolf = None
    turns_number = None
    sheep_number = None
    alive_sheep_number = None
    eaten_sheep_list = []
    json_data = []
    write_data = Data()
    wait_character = None

    def __init__(self, init_pos_limit, sheep_move_dist,
                 wolf_move_dist, sheep_number, turns_number, wait):
        log = "Info level: Setting simulation details " + str(init_pos_limit) + " " + str(sheep_move_dist) + " " + \
              str(wolf_move_dist) + " " + str(sheep_move_dist) + " " + str(sheep_number) + " " + str(turns_number) + " "
        logging.info(log)
        self.turns_number = turns_number
        self.wolf = Wolf(wolf_move_dist)
        self.wait_character = wait
        self.sheep_number = sheep_number
        self.alive_sheep_number = sheep_number
        for _ in range(sheep_number):
            self.sheep_list.append(Sheep(init_pos_limit, sheep_move_dist))

    def start_simulation(self):
        log = "Debug level: start_simulation "
        logging.debug(log)
        for i in range(self.turns_number):
            if self.alive_sheep_number == 0:
                return
            self.sheep_move()
            if self.wolf_attack():
                self.wolf_move()
            print("Tur: " + str(i) + ", wolf position: " + str("{:.3f}".format(self.wolf.x_position))
                  + " " + str("{:.3f}".format(self.wolf.y_position)))
            print("Sheep number: " + str(self.alive_sheep_number) + ",eaten sheep: " + str(self.eaten_sheep_list))
            self.write_data.add_json_data(i, self.wolf.x_position, self.wolf.y_position, self.alive_sheep_number,
                                          self.sheep_list)
            self.write_data.add_csv_data([str(i), str(self.alive_sheep_number)])
            input_character = ""
            log = "Info level: End of the round"
            logging.info(log)
            while input_character != self.wait_character:
                input_character = input()

    def sheep_move(self):
        log = "Debug level: sheep_move "
        logging.debug(log)

        for i in range(self.sheep_number):
            if self.sheep_list[i].alive:
                self.sheep_list[i].move()

    def wolf_move(self):
        log = "Debug level: wolf_move "
        logging.debug(log)
        i = self.closed_sheep()
        dist = self.sheep_from_wolf_distance(self.sheep_list[i])
        delta_x = abs(self.wolf.x_position - self.sheep_list[i].x_position)
        delta_y = abs(self.wolf.y_position - self.sheep_list[i].y_position)
        x = (self.wolf.wolf_move_dist * delta_x) / dist
        y = (self.wolf.wolf_move_dist * delta_y) / dist
        if self.wolf.x_position > self.sheep_list[i].x_position:
            x = -x
        if self.wolf.y_position > self.sheep_list[i].y_position:
            y = -y
        log = "Info level: Calculating wolf move"
        logging.info(log)
        self.wolf.move(x, y)

        return

    def wolf_attack(self):
        for i in range(self.sheep_number):
            if self.sheep_list[i].alive:
                if self.wolf.wolf_move_dist >= \
                        self.sheep_from_wolf_distance(self.sheep_list[i]):
                    self.alive_sheep_number -= 1
                    self.eaten_sheep_list.append(i)
                    self.sheep_list[i].alive = False
                    self.wolf.set_wolf_position(self.sheep_list[i].x_position, self.sheep_list[i].y_position)
                    log = "Debug level: wolf_attack " + "False"
                    logging.debug(log)
                    log = "Info level: Wolf can eat sheep"
                    logging.info(log)
                    return False
        log = "Info level: Wolf can't eat sheep"
        logging.info(log)
        log = "Debug level: wolf_attack " + "True"
        logging.debug(log)
        return True

    def closed_sheep(self):
        dist = 0
        sheep = None
        for i in range(self.sheep_number):
            if self.sheep_list[i].alive:
                dist = self.sheep_from_wolf_distance(self.sheep_list[i])
                sheep = i
                break
        for i in range(self.sheep_number):
            if self.sheep_list[i].alive:
                if dist > self.sheep_from_wolf_distance(self.sheep_list[i]):
                    dist = self.sheep_from_wolf_distance(self.sheep_list[i])
                    sheep = i
        log = "Info level: Finding the closed  sheep " + str(sheep)
        logging.info(log)
        log = "Debug level: closed_sheep " + str(sheep)
        logging.debug(log)
        return sheep

    def sheep_from_wolf_distance(self, sheep):
        log = "Info level: Calculating distance between the closed sheep and wolf " +\
              str(sqrt((sheep.x_position - self.wolf.x_position) * (sheep.x_position - self.wolf.x_position) +
                       (sheep.y_position - self.wolf.y_position) * (sheep.y_position - self.wolf.y_position)))
        logging.info(log)
        log = "Debug level: sheep_from_wolf_distance " + \
              str(sqrt((sheep.x_position - self.wolf.x_position) * (sheep.x_position - self.wolf.x_position) +
                       (sheep.y_position - self.wolf.y_position) * (sheep.y_position - self.wolf.y_position)))
        logging.debug(log)
        return sqrt((sheep.x_position - self.wolf.x_position) * (sheep.x_position - self.wolf.x_position) +
                    (sheep.y_position - self.wolf.y_position) * (sheep.y_position - self.wolf.y_position))
