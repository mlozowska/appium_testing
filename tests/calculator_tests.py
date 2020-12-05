from appium_day.pages.home_page import HomePage


class TestCalculator:

    def test_open_close_expert_panel(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.open_expert_panel()
        self.home_page.close_expert_panel()

    def test_add(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.add_numbers(2, 5)
        result = self.home_page.get_result()
        assert result == "7"

    def test_sub(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.sub_numbers(5, 3)
        result = self.home_page.get_result()
        assert result == "2"

    def test_mul(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.mul_numbers(2, 2)
        result = self.home_page.get_result()
        assert result == "4"

    def test_div(self, driver):
        self.home_page = HomePage(driver)
        self.home_page.div_numbers(0, 1)
        result = self.home_page.get_result()
        assert result == "0"
