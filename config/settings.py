import os

try:
    UI_SERVER_MODE = bool(os.environ["UI_SERVER_MODE"])
    DRIVER_TYPE = str(os.environ["DRIVER_TYPE"])
except KeyError:
    UI_SERVER_MODE = False
    DRIVER_TYPE = 'firefox'


CONSOLE = 'http://staging-hungryhouse.com/'