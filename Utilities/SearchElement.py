import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class SearchElement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(driver)

    @staticmethod
    def searchElement(locatorType,locator):
        element=wait.until(expected_conditions.presence_of_element_located((locatorType,locator)))
        return element