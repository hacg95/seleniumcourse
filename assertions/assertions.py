import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class assertionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path="..\chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def select_language_test(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by= how, value= what)
        except NoSuchElementException as variable:
            return False
        return True


def run():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run()