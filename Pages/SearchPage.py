from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig

class SearchPage:

    searchTab="twotabsearchtextbox"


    #userName=ReadConfig.getUserName()
    #password=ReadConfig.getPassword()
    productName = ReadConfig.getProductName()

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action=ActionChains(driver)

    def SearchProd(self):
        Search=self.wait.until(ec.presence_of_element_located((By.ID,self.searchTab)))
        self.action.send_keys(self.productName).send_keys('ENTER').perform()
        #self.driver.find_element(By.ID,self.searchTab).send_keys(self.productName).send_keys('ENTER')
        time.sleep(5)




