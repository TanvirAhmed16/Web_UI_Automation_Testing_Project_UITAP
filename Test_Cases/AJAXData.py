import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AJAXDataTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_AJAXData(self):
        '''AJAX Data'''
        ex_wait = WebDriverWait(self.driver, 20, poll_frequency=2, ignored_exceptions=Exception)

        self.driver.find_element(By.XPATH, "//a[normalize-space()='AJAX Data']").click()
        self.driver.find_element(By.XPATH, "//button[@id='ajaxButton']").click()

        time1 = time.time()
        ajax_data = ex_wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='bg-success']")))
        time2 = time.time()

        time_taken = time2 - time1
        ajax_text = ajax_data.text
        print(f"{ajax_text} with a time of {time_taken} seconds.")
        ajax_data.click()

        self.assertEqual("Data loaded with AJAX get request.", ajax_text, "AJAX text didn't match.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
