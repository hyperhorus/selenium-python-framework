from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
#from pages.courses.register_courses_page import RegisterCoursesPage
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class LogintTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        print("classSetup ")
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyloginSuccess("xpath")
        self.ts.markFinal("TestLogin", result2, "Login was successful")



    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "caca")
        result = self.lp.verifyLoginFailed("xpath")

        assert result == True

