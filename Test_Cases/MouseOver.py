import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MouseOverTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_MouseOver(self):
        '''Mouse Over'''
        ex_wait = WebDriverWait(self.driver, 45)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Mouse Over']").click()

        count = 0
        for i in range(2):
            ex_wait.until(
                EC.element_to_be_clickable((By.XPATH, "//section//div[@class='container']//div[1]/a"))).click()
            count += 1
        print(f"Link is clicked {count} times.")

        self.assertEqual(2, count, "Link click count didn't match.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
