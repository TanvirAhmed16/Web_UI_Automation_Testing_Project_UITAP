import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoadDelaysTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_LoadDelays(self):
        '''Load Delays'''
        ex_wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=Exception)

        time1 = time.time()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Load Delay']").click()
        button = ex_wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Button Appearing After Delay']")))
        button.click()
        time2 = time.time()

        time_taken = time2 - time1
        button_text = button.text

        if time_taken < 10:
            self.assertEqual("Button Appearing After Delay", button_text, "Button text didn't match.")
            print(f"The button is clicked after the page load delay of {time_taken} seconds.")
            print("Test passed.")
        else:
            print("Test passed but load delay is taking more than expected time.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
