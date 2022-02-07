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
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig


baseURL= ReadConfig.getURL()
myLogger=LogGen.loggen()


@when(u'Enter login')
def step_impl(context):
    #global hpage1
    #global lpage

    hpage1=HomePage(context.driver)
    lpage=LoginPage(context.driver)
    hpage1.clickOnLogin()
    lpage.EnterLoginDetails()
    expectedTitle="amazon"
    actualTitle=context.driver.title
    context.driver.save_screenshot(".\\ScreenShots\\"+"LoginPage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="AmazonLoginTest",
                      attachment_type=AttachmentType.PNG)
    myLogger.info("Assert true")


