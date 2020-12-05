import os

import pytest
from appium import webdriver


@pytest.fixture()
def driver(request):

    def close_driver():
        driver.quit()

    app_name = "calculator.apk"
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['app'] = app_path

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    request.addfinalizer(close_driver)
    return driver