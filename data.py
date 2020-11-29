import logging


class Data:
    json_data_list = []
    csv_data_list = []

    def clear_data_list(self):
        self.json_data_list = []
        self.csv_data_list = []
        log = "Debug level: clear_data_list "
        logging.debug(log)
        log = "Info level: Clearing data"
        logging.info(log)

    def add_json_data(self, round_no, x, y, sheep_num, sheep_list):
        dir = {'round_no': round_no, 'wolf_pos': [x, y]}
        list = []
        for i in range(sheep_num):
            if sheep_list[i].alive:
                list.append([sheep_list[i].x_position, sheep_list[i].y_position])
            else:
                list.append([None])
        dir['sheep_pos'] = list
        self.json_data_list.append(dir)
        log = "Debug level: write_log " + str(round_no) + " " + str(x) + " " + str(y) + " " + str(sheep_num) + " " + str(sheep_list)
        logging.debug(log)
        log = "Info level: Adding json data"
        logging.info(log)

    def add_csv_data(self, data):
        self.csv_data_list.append(data)
        log = "Debug level: add_csv_data " + str(data)
        logging.debug(log)
        log = "Info level: Adding csv data"
        logging.info(log)
