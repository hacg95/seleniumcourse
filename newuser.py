import unittest
from selenium import webdriver

class registerNewUser(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account.is_displayed() and create_account.is_enabled())
        create_account.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        newsletter = driver.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and newsletter.is_enabled()
        and submit_button.is_enabled())

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    
    def tearDown(self) -> None:
        self.driver.quit()


def run():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run()