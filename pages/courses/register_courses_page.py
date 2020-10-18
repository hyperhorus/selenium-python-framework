from selenium.webdriver.common.by import By
import utilities.customerLogger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    #_search_box = "search"
    _search_box = "//input[@name='course']"
    _search_button = "//button[@class='find-course search-course']"
    _course = "//h4[contains(text(),'{0}')]"
    _all_courses = ""
    _enroll_button = "//button[contains(.,'Enroll in Course')]"
    _cc_number = "//input[@class='InputElement is-empty Input Input--empty' and (@name='cardnumber')]"
    #_cc_number = "cardnumber"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    _enroll_error_message = "//p[@class='dynamic-text'][contains(.,'Your card was declined')]"
    _iframe = "__privateStripeFrame3745"

    def enterCourseName(self, name):
        self.sendKeys(name, locator="", locatorType="")
        self.elementClick(locator=self._search_button, locatorType="xpath")
        """self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_button, locatorType="xpath")
        self.selectCourseToEnroll(self._course)
        self.enterCardNumber("2345 6785 2345 9876")"""


    def selectCourseToEnroll(self, fullCourseName):
        #self.elementClick(locator=self._course.format(fullCourseName))
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")
        #self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNumber(self, num):
        self.switchToiFrame(2)
        self.sendKeys(num, locator=self._cc_number, locatorType="xpath")
        self.switchToiFrame(-1)

    def enterCardExp(self, exp):
        self.switchToiFrame(4)
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToiFrame(-1)

    def enterCardCVV(self, cvv):
        self.switchToiFrame(3)
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToiFrame(-1)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    #def enterCreditCardInfo(self, num, exp, cvv):


    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.enterCardNumber(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.webScroll(direction="down")
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

