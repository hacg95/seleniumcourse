import unittest 
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= r"C:\Users\hacg9\Harold\Programación\Python\Selenium\chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.platzi.com")

    def test_visitfb(self):
        self.driver.get("https://www.facebook.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def run():
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reports", report_name="hello-world-report"))

if __name__ == "__main__":
    run()