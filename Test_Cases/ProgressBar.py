import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProgressBarTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_ProgressBar(self):
        '''Progress Bar'''
        try:
            ex_wait = WebDriverWait(self.driver, 45)
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Progress Bar']").click()

            t1 = time.time()
            ex_wait.until(EC.element_to_be_clickable((By.ID, "startButton"))).click()
            ex_wait.until(
                EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, '[role="progressbar"]'), "aria-valuenow",
                                                           "75"))
            ex_wait.until(EC.element_to_be_clickable((By.ID, "stopButton"))).click()
            t2 = time.time()

            progress_time_taken = t2 - t1
            print(f"Progress time takes : {progress_time_taken} seconds.")

            result = self.driver.find_element(By.XPATH, "//p[@id='result']")
            print("Result is : ", result.text)

            self.assertTrue(progress_time_taken <= 45, "Progress time is more than 45 second.")
            print("Test Passed.")
        except:
            raise Exception

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
