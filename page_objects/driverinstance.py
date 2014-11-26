from pyvirtualdisplay import Display
from selenium import webdriver

from config import settings as config


class DriverService():

    def __init__(self):
        self.displays = []
        self.drivers = []
        if config.UI_SERVER_MODE:
            display = Display(visible=0, size=(800, 600))
            self.displays.append(display)
            display.start()
        d_type = config.DRIVER_TYPE.upper()
        if d_type == 'CHROME':
            self.driver_type = webdriver.Chrome
        elif d_type == 'FIREFOX':
            self.driver_type = webdriver.Firefox

    def configure_driver(self):
        driver = self.driver_type()
        self.drivers.append(driver)
        driver.implicitly_wait(30)
        return driver

    def close(self):
        for driver in self.drivers:
            driver.close()
        for display in self.displays:
            display.stop()