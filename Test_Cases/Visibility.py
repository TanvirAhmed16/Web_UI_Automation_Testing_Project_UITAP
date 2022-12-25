import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class VisibilityTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_Visibility(self):
        '''Visibility'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Visibility']").click()
        buttons_before_hide = self.driver.find_elements(By.XPATH, "//div[@class='container']//table/tbody/tr/td/button")
        print("Total number of button before hiding is : ", len(buttons_before_hide))
        print("Button display status before hiding...\n")

        for i in range(len(buttons_before_hide)):
            print(buttons_before_hide[i].text, "Button displayed status is : ", buttons_before_hide[i].is_displayed())

        buttons_before_hide[0].click()

        buttons_after_hide = self.driver.find_elements(By.XPATH, "//div[@class='container']//table/tbody/tr/td/button")
        print("\nTotal number of button after hiding is : ", len(buttons_after_hide))
        print("Button display status after hiding...\n")

        for i in range(len(buttons_after_hide)):
            try:
                if buttons_after_hide[i].is_displayed() == True:
                    print(buttons_after_hide[i].text, " button is not hidden.")
                else:
                    print(buttons_after_hide[i].text, "Button displayed status is : ",
                          buttons_after_hide[i].is_displayed())
            except:
                print("Exception Occured.")

        self.assertEqual("Hide", buttons_after_hide[0].text, "Hide button text didn't match.")
        print("Test Passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
