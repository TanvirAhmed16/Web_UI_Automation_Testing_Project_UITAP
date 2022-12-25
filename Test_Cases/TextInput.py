import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TextInputTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_TextInput(self):
        '''Text Input'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Text Input']").click()
        text_input = self.driver.find_element(By.XPATH, "//input[@id='newButtonName']")
        action = ActionChains(self.driver)
        action.send_keys_to_element(text_input, "TestButton").perform()

        button = self.driver.find_element(By.XPATH, "//button[@id='updatingButton']")
        btn_text_before_click = button.text
        button.click()
        btn_text_after_click = button.text

        if btn_text_after_click == "TestButton":
            self.assertEqual("TestButton", btn_text_after_click, "Button text after click didn't match.")
            print(f"Button text before click is : {btn_text_before_click}")
            print(f"Button text after click is : {btn_text_after_click}")
            print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
