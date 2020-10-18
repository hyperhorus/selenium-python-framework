import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetup(request, browser):
    print("Running conftest one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    rcp = RegisterCoursesPage(driver)
    lg = LoginPage(driver)
    lg.login("test@email.com", "abcabc")
    #rcp.login("test@email.com", "abcabc")
    #rcp.enterCourseName("JavaScript")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver #regresa el valor
    #driver.quit()
    print("Running conftest one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
