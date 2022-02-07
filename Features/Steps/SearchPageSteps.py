import time

import allure_behave
from allure_commons.types import AttachmentType
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig


baseURL= ReadConfig.getURL()
myLogger=LogGen.loggen()


@when(u'Search product')
def step_impl(context):
    search=SearchPage(context.driver)
    search.SearchProd()

    context.driver.save_screenshot(".\\ScreenShots\\"+"searchpage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="AmazonLoginTest",
                      attachment_type=AttachmentType.PNG)



