import unittest
from selenium import webdriver

class homePageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_button(self):
        button = self.driver.find_element_by_class_name("button")

    def test_search_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banner = banner_list.find_element_by_tag_name("img")
        self.assertEqual(3, len(banner))

    def tearDown(self) -> None:
        self.driver.quit()


def run():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run()