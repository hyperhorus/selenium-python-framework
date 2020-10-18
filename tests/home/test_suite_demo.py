import unittest
from tests.home.login_test import LogintTest
from tests.courses.register_courses_csv_data import RegisterMultipleCourseCsvTest

#Get all the tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LogintTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterMultipleCourseCsvTest)

#Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc2, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)