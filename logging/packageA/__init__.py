from  .module1 import MyFilter

from logging.config import dictConfig
import yaml

print("packageA __init__.py")

#print(__name__)
with open("logging-config.yaml","r") as file:
    config = yaml.safe_load(file)
    print(config)
    dictConfig(config)