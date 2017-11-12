import configparser


class Config:
    def __init__(self, config_location):
        self.config_location = config_location
        self.config = configparser.ConfigParser()
        self.config.read(self.config_location)

    def save_config(self):
        with open(self.config_location, 'w') as config_file:
            self.config.write(config_file)

    def get_config(self):
        return self.config['USER']
