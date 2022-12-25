import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class SampleAppTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_SampleApp(self):
        '''Sample App'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Sample App']").click()

        login_out_status = self.driver.find_element(By.XPATH, "//label[@id='loginstatus']")
        print(login_out_status.text)

        u_name = self.driver.find_element(By.XPATH, "//input[@class='form-control' and @name='UserName']")
        password = self.driver.find_element(By.XPATH, "//input[@class='form-control' and @name='Password']")
        log_in_out_btn = self.driver.find_element(By.XPATH, "//button[@id='login']")

        if login_out_status.text == "User logged out.":
            u_name.send_keys("DemoApp")
            password.send_keys("pwd")
            log_in_out_btn.click()

        login_out_status = self.driver.find_element(By.XPATH, "//label[@id='loginstatus']")
        print(login_out_status.text)

        self.assertEqual("Welcome, DemoApp!", login_out_status.text, "Status text didn't match.")
        print("Test Passed.")
        log_in_out_btn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
