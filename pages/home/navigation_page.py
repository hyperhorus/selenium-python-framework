from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.customerLogger as cl
import logging
from base.basepage import BasePage



class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _my_courses = "ALL COURSES"
    _all_courses = "MY COURSES"
    _user_icon = "//img[@class='zl-navbar-rhs-img ']"


    def navigateToMyCourses(self):
        self.elementClick(self._my_courses, locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(self._all_courses, locatorType="link")

    def navigateToUserIcon(self):
        self.elementClick(self._user_icon, locatorType="xpath")

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

