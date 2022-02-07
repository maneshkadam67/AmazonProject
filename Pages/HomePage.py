from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.SearchElement import SearchElement
import time

class HomePage:

    login_link_outer = "//span[normalize-space()='Account & Lists']"
    login_link_inner= "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']"

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action=ActionChains(self.driver)

    def clickOnLogin(self):
        #s=SearchElement()
        #login1=s.searchElement(By.XPATH,self.login_link_outer)
        time.sleep(5)
        login1=self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.login_link_outer)))
        #login1=self.driver.find_element(By.XPATH,self.login_link_outer)
        self.action.move_to_element(login1).perform()
        time.sleep(3)
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.login_link_inner))).click()
        time.sleep(3)
        #login2=self.driver.find_element(By.XPATH,self.login_link_inner)
        #login2.click()





