import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class NonBreakingSpaceTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_NonBreakingSpace(self):
        '''Non-Breaking Space'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Non-Breaking Space']").click()

        # btn = driver.find_element(By.XPATH, "//button[text()='My Button']")
        '''This XPATH will not work. As Text caption may contain non-breaking spaces that have no visual difference 
        from generic spaces.'''
        btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='My Button']")
        btn.click()
        print("Button name is:", btn.text)

        self.assertEqual("My Button", btn.text, "Button text didn't match.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
