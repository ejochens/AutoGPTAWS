import yaml

class Config:
    def __init__(self, config_file="config.yaml"):
        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, key, default=None):
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value or default

config = Config()
