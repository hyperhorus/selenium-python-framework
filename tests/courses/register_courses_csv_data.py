from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
import unittest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCsvFile
import time
import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterMultipleCourseCsvTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToUserIcon()

    @pytest.mark.run(order=1)
    @data(*getCsvFile("C:\\Users\\g_lla\\workspace_python\\LetsKodeIt\\test_cases.csv"))
    @unpack
    def test_invalidEnrollment(self, coursename, ccCN, ccexp, cccvv):
        self.courses.enterCourseName(coursename)
        time.sleep(1)
        self.courses.selectCourseToEnroll(coursename)
        time.sleep(1)
        self.courses.enrollCourse(num=ccCN, exp=ccexp, cvv=cccvv)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='dynamic-link' and contains(text(),'ALL COURSES')]").click()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment failed")

