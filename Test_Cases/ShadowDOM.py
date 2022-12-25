import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
import clipboard


class ShadowDOMTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_ShadowDOM(self):
        '''Shadow DOM'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Shadow DOM']").click()

        shadow_host = self.driver.find_element(By.CSS_SELECTOR, 'guid-generator')
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        shadow_content_generate = shadow_root.find_element(By.CSS_SELECTOR, '#buttonGenerate')
        shadow_content_copy = shadow_root.find_element(By.CSS_SELECTOR, '#buttonCopy')
        shadow_content_box = shadow_root.find_element(By.CSS_SELECTOR, '#editField')

        shadow_content_generate.click()
        time.sleep(2)

        generated_key = shadow_content_box.get_attribute("value")
        print("The generated key is: ", generated_key)

        ''' As there is a possible frontend bug in the copy button, thus we can't complete the testing of the full 
            scenario based on how it is described. That's why we will perform the rest of the operation related to 
            clipboard by using another package called clipboard.'''
        # shadow_content_copy.click()

        clipboard.copy(shadow_content_box.get_attribute("value"))
        clipboard_value = clipboard.paste()
        print("The clipboard value is:", clipboard_value)

        self.assertEqual(clipboard_value, shadow_content_box.get_attribute("value"), "Shadow DOM value didn't match.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
