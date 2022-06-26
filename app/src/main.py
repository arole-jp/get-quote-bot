import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from quote_site_controller import QuoteSiteController

def getDriver():
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.FIREFOX.copy()
    )
    return driver


driver = getDriver()
quoteSiteController = QuoteSiteController(driver)
totalVisitors = quoteSiteController.getTotalVisitors()
quoteSiteController.searchFor("ゴルフ")
quoteSiteController.index0Open()
quoteSiteController.getPageQuotes()
driver.quit()

