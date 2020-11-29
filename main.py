from configparser import ConfigParser
from simulation import Simulation
from os import getcwd, chdir
import argparse
import json
import csv
import logging


def write_to_json_file(data, path):
    if path == "":
        path = getcwd()
    else:
        path = getcwd() + "/" + path
    with open(path + "/" + "pos.json", "w") as file:
        json.dump(data, file, indent=2)
    log = "Debug level: write_to_json_file " + str(data) + " " + path
    logging.debug(log)
    log = "Info level: Saving json data"
    logging.info(log)


def write_to_csv_file(data, path):
    if path == "":
        path = getcwd()
    else:
        path = getcwd() + "/" + path
    with open(path + "/" + "alive.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    log = "Debug level: write_to_csv_file " + str(data) + " " + path
    logging.debug(log)
    log = "Info level: Saving csv data"
    logging.info(log)


def read_config_file(name):
    config = ConfigParser()
    config.read(name)
    init_pos_limit = config.get('Terrain', 'InitPosLimit')
    sheep_move_dist = config.get('Movement', 'SheepMoveDist')
    wolf_move_dist = config.get('Movement', 'WolfMoveDist')
    if float(init_pos_limit) < 0 or float(sheep_move_dist) < 0 or float(wolf_move_dist) < 0:
        log = "Critical level: read_config_file Value have to be more than 0"
        logging.critical(log)

        raise ValueError("Value have to be more than 0")

    log = "Debug level: read_config_file " + name + " " + init_pos_limit + " " + sheep_move_dist + " " + wolf_move_dist
    logging.debug(log)
    log = "Info level: Reading config file"
    logging.info(log)
    return float(init_pos_limit), float(sheep_move_dist), float(wolf_move_dist)


def write_log(level, path):
    if level == "DEBUG" or level == 10:
        level = logging.DEBUG
    elif level == "INFO" or level == 20:
        level = logging.INFO
    elif level == "WARNING" or level == 30:
        level = logging.WARNING
    elif level == "ERROR" or level == 40:
        level = logging.ERROR
    elif level == "CRITICAL" or level == 50:
        level = logging.CRITICAL
    else:
        log = "Error level: write_log It is a bad value"
        logging.error(log)
        raise ValueError("It is a bad value")
    common_path = getcwd()
    chdir(getcwd() + "/" + path)
    logging.basicConfig(filename="chase.log", level=level)
    chdir(common_path)
    log = "Info level: Writing logs"
    logging.info(log)
    log = "Debug level: write_log " + str(level) + " " + path
    logging.debug(log)
    print(level)

def main():
    parser = argparse.ArgumentParser(description="Wolf and sheep simulation")
    parser.add_argument("-c", "--config", metavar="FILE", help="Set config file", action="store",
                        dest="config_file_name")
    parser.add_argument("-d", "--dir", metavar="DIR", help="Set subdirectory where files will be saved", action="store",
                        dest="dir_file_name")
    parser.add_argument("-l", "--log", metavar="LEVEL", help="Set log level", action="store", dest="log_level")
    parser.add_argument("-r", "--round", metavar="NUM", help="Set rounds number", action="store", dest="rounds_num")
    parser.add_argument("-s", "--sheep", metavar="NUM", help="Set sheep number", action="store", dest="sheep_num")
    parser.add_argument("-w", "--wait", help="Set the character to press before starting the next round",
                        action="store", dest="wait_character")
    arguments = parser.parse_args()
    if arguments.config_file_name:
        init_pos_limit, sheep_move_dist, wolf_move_dist = \
            read_config_file(arguments.config_file_name)
    else:
        init_pos_limit = 10.0
        sheep_move_dist = 0.5
        wolf_move_dist = 1.0
    if arguments.dir_file_name:
        path = arguments.dir_file_name
    else:
        path = ""

    if arguments.rounds_num:
        round_no = arguments.rounds_num
    else:
        round_no = 50

    if arguments.rounds_num:
        sheep_num = arguments.sheep_num
    else:
        sheep_num = 15

    if arguments.wait_character:
        wait = arguments.wait_character
    else:
        wait = ""
    if arguments.log_level:
        write_log(arguments.log_level, path)
    simulation = Simulation(init_pos_limit, sheep_move_dist, wolf_move_dist, sheep_num, round_no, wait)
    simulation.start_simulation()
    write_to_csv_file(simulation.write_data.csv_data_list, path)
    write_to_json_file(simulation.write_data.json_data_list, path)



if __name__ == "__main__":
    main()
