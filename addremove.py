import unittest
from selenium import webdriver

class testAddRemove(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()

    def testingAdd(self):
        clicks_add = int(input("How many elements you want to add?: "))
        add_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/button')
        
        for i in range(clicks_add):
            add_button.click()

    def tearDown(self) -> None:
        self.driver.quit()


def run():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run()