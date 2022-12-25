import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest


class ScrollbarsTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_Scrollbars(self):
        '''Scrollbars'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Scrollbars']").click()
        hiding_button = self.driver.find_element(By.XPATH, "//button[@id='hidingButton']")
        self.driver.execute_script("arguments[0].scrollIntoView()", hiding_button)
        hiding_button.click()
        hiding_btn_text = hiding_button.text
        time.sleep(3)

        if hiding_btn_text == "Hiding Button":
            self.assertEqual("Hiding Button", hiding_btn_text, "Button text after click didn't match.")
            print(f"Button text is : {hiding_btn_text}")
            print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
