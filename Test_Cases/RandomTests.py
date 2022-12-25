import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RandomTests(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_Random1(self):
        '''Website Title'''
        web_title = self.driver.title
        try:
            self.assertEqual("UI  Automation Playground", web_title, "Web Page Title didn't match.")
            # print(web_title)
        except:
            raise Exception

    def test_Random2(self):
        raise unittest.SkipTest('Work in progress')

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
