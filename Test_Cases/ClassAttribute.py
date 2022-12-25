import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ClassAttributeTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_ClassAttribute(self):
        '''Class Attribute'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Class Attribute']").click()
        self.driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        alert = self.driver.switch_to.alert
        atert_text = alert.text
        if atert_text == "Primary button pressed":
            alert.accept()

        self.assertEqual("Primary button pressed", atert_text, "Alert text didn't match.")
        print(f"Button is identified using btn-primary class and alert text is {atert_text}.")
        print("Test Passed...")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


