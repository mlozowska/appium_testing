from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium_day.pages.base_page import BasePage


class HomePage(BasePage):

    plus_selector = (MobileBy.ACCESSIBILITY_ID, "plus")
    minus_selector = (MobileBy.ACCESSIBILITY_ID, "minus")
    multiply_selector = (MobileBy.ACCESSIBILITY_ID, "multiply")
    divide_selector = (MobileBy.ACCESSIBILITY_ID, "divide")
    equals_selector = (MobileBy.ACCESSIBILITY_ID, "equals")
    result_selector = (MobileBy.ID, "result_final")
    clear_selector = (MobileBy.ACCESSIBILITY_ID, "clear")
    panel_arrow_selector = (MobileBy.ID, "arrow")

    def add_numbers(self, a, b):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.digit_locator(a))).click()
        self.driver.find_element(*self.plus_selector).click()
        self.driver.find_element(*self.digit_locator(b)).click()
        self.driver.find_element(*self.equals_selector).click()

    def sub_numbers(self, a, b):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.digit_locator(a))).click()
        self.driver.find_element(*self.minus_selector).click()
        self.driver.find_element(*self.digit_locator(b)).click()
        self.driver.find_element(*self.equals_selector).click()

    def mul_numbers(self, a, b):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.digit_locator(a))).click()
        self.driver.find_element(*self.multiply_selector).click()
        self.driver.find_element(*self.digit_locator(b)).click()
        self.driver.find_element(*self.equals_selector).click()

    def div_numbers(self, a, b):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.digit_locator(a))).click()
        self.driver.find_element(*self.result_selector).click()
        self.driver.find_element(*self.digit_locator(b)).click()
        self.driver.find_element(*self.equals_selector).click()

    def get_result(self):
        result_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_selector)).text
        self.driver.find_element(*self.result_selector).clear()
        return result_value

    def digit_locator(self, value):
        selector = (MobileBy.ID, f"digit_{value}")
        return selector

    def open_expert_panel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.equals_selector))
        screen_size = self.driver.get_window_size()
        TouchAction(self.driver).tap(None, screen_size['width'] - 1, screen_size['height'] - 1, 1).perform()

    def close_expert_panel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.panel_arrow_selector)).click()