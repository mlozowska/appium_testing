import os
from appium import webdriver

# Returns abs path relative to this file and not cwd
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['app'] = app_path

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

digit_1_selector = (MobileBy.ID, "digit_1")
plus_selector = (MobileBy.ACCESSIBILITY_ID, "plus")
digit_2_selector = (MobileBy.ID, "digit_2")
equals_selector = (MobileBy.ACCESSIBILITY_ID, "equals")
result_selector = (MobileBy.ID, "result_final")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(digit_1_selector)).click()
driver.find_element(*plus_selector).click()
driver.find_element(*digit_2_selector).click()
driver.find_element(*equals_selector).click()
result_value = driver.find_element(*result_selector).text
assert result_value == "3"
