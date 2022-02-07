import time

import allure


import allure_behave
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


@given(u'Launch the App')
def step_impl(context):
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    myLogger.info("Driver initialized")
    context.driver.get(baseURL)
    myLogger.info("Browser Launched")
    context.driver.maximize_window()
    myLogger.info("Browser Maximized")
    context.driver.save_screenshot(".\\ScreenShots\\" + "HomePageLoad.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="AmazonLoginTest",
                   attachment_type=AttachmentType.PNG)

@when(u'Verify page title')
def step_impl(context):
    global hpage
    #hpage=HomePage(context.driver)
    hpage.clickOnLogin()
    context.driver.save_screenshot(".\\ScreenShots\\" + "HomePageTitle.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="AmazonLoginTest",
                   attachment_type=AttachmentType.PNG)


    time.sleep(5)

@when(u'close the browser')
def step_impl(context):
    context.driver.close()
    myLogger.info("Browser closed")
