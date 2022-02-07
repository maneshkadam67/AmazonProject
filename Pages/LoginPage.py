from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig


class LoginPage:

    email="ap_email"
    continue_but = "continue"
    password_field="ap_password"
    submit="signInSubmit"
    search="//input[@id='twotabsearchtextbox']"

    userName=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    def EnterLoginDetails(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID,self.email))).send_keys(self.userName)
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.continue_but))).click()
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.password_field))).send_keys(self.password)
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.submit))).click()

        # self.driver.find_element(By.ID,self.email).send_keys(self.userName)
        # time.sleep(2)
        # self.driver.find_element(By.ID,self.continue_but).click()
        # time.sleep(4)
        # self.driver.find_element(By.ID,self.password_field).send_keys(self.password)
        # time.sleep(2)
        # self.driver.find_element(By.ID,self.submit).click()
        # time.sleep(5)


    # def setusername(self,username):
    #     self.wait.until(expected_conditions.presence_of_element_located(By.ID,username))
    #     #self.driver.find_element_by_id(self.username).send_keys(username)
    #
    # def continueBut(self,continue_but):
    #     self.driver.find_element_by_id(self.continue_but).click()
    #
    # def setuserpassword(self,password):
    #     self.driver.find_element_by_id(self.password).send_keys(password)
    #
    # def click_signIn(self,signInSubmit):
    #     self.driver.find_element_by_id(self.submit).click()
    #
