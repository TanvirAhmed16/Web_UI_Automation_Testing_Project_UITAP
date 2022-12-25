import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class VerifyTextTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_VerifyText(self):
        '''Verify Text'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Verify Text']").click()
        valid_locator_text = self.driver.find_element(By.XPATH, "//span[normalize-space(.)='Welcome UserName!']").text
        expected_test = self.driver.find_element(By.XPATH, "//div[@class='bg-primary']//span[@class='badge-secondary']").text

        self.assertEqual(valid_locator_text, expected_test, "Text didn't match.")
        print(f"{valid_locator_text} == {expected_test}")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
