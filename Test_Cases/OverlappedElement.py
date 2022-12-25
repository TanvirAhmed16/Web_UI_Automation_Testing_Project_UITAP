import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


class OverlappedElementTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_OverlappedElement(self):
        '''Overlapped Element'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Overlapped Element']").click()

        id_field = self.driver.find_element(By.XPATH, "//input[@id='id']")
        name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")

        id_field.send_keys("3708")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView()", name_field)
        name_field.send_keys("NameTest")
        name_field = self.driver.find_element(By.XPATH, "//input[@id='name']")

        self.assertEqual(True, name_field.is_displayed(), "Name field is not visible.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
