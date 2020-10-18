from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage
import utilities.customerLogger as cl
import logging
from base.basepage import BasePage



class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # locators
    _login_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//div[@class='col-xs-12 col-md-12']"
    _login_success = "//img[@class='zl-navbar-rhs-img ']"
    _login_failed = "//span[@class='dynamic-text help-block']"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyloginSuccess(self, locatorType="id"):
        result = self.isElementPresent(self._login_success, locatorType)


        return result

    def verifyLoginFailed(self, locatorType="id"):
        result = self.isElementPresent(self._login_failed, locatorType)

        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.navigateToUserIcon()
        self.elementClick(locator="//a[contains(.,'Logout')]", locatorType="xpath")

