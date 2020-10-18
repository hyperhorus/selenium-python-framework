from pages.courses.register_courses_page import RegisterCoursesPage
import unittest

from utilities.teststatus import TestStatus


import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class RegisterCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="4391850000572427", exp="0724", cvv="123")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment failed")
