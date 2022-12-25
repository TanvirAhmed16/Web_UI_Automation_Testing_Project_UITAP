import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class DynamicIDTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_DynamicID(self):
        '''Dynamic ID'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Dynamic ID']").click()
        btn = self.driver.find_element(By.XPATH,
                                  "//button[@class='btn btn-primary' and contains(text(),'Button with Dynamic ID')]")
        btn.click()
        btn_text = btn.text

        self.assertEqual("Button with Dynamic ID", btn_text, "Button text is not same.")
        print(btn.text + " is grabbed and clicked without using ID.")
        print("Test Passed...")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


