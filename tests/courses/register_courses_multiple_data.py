from pages.courses.register_courses_page import RegisterCoursesPage
import unittest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack



import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4391850000572427", "0624", "123"), ("Selenium WebDriver Advanced", "4391850000572427", "0624", "123"))
    @unpack
    def test_invalidEnrollment(self, coursename, ccCN, ccexp, cccvv):
        self.courses.enterCourseName(coursename)
        self.courses.selectCourseToEnroll(coursename)
        self.courses.enrollCourse(num=ccCN, exp=ccexp, cvv=cccvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment failed")
        self.driver.find_element_by_xpath("//a[@class='dynamic-link' and contains(text(),'ALL COURSES')]").click()
