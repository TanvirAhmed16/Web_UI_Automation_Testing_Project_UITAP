import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class DynamicTableTest(unittest.TestCase):
    # Opening the Browser
    def setUp(self):
        serv_obj = Service("F:\Softwares\Selenium WebDrivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()

        url = "http://uitestingplayground.com/home"
        self.driver.get(url)

    def test_DynamicTable(self):
        '''Dynamic Table'''
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Dynamic Table']").click()

        no_of_rows = len(self.driver.find_elements(By.XPATH, "//div[3]//div"))
        print("Number of rows : ", no_of_rows)
        no_of_columns = len(self.driver.find_elements(By.XPATH, "//div[2]//div[1]/span"))
        print("Number of columns : ", no_of_columns)

        for row in range(1, no_of_rows + 1):
            for col in range(1, no_of_columns + 1):
                all_data = self.driver.find_element(By.XPATH,
                                                    "//div[3]//div[" + str(row) + "]/span[" + str(col) + "]").text
                print(all_data, end="        ")
            print()

        system_names = self.driver.find_elements(By.XPATH, "//div[3]//div/span[1]")
        for i in range(len(system_names)):
            # print(system_names[i].text)
            if system_names[i].text == "Chrome":
                process_name = system_names[i].text
                process_name_index = i + 1
                print(process_name_index)

        column_names = self.driver.find_elements(By.XPATH, "//div[2]//div[1]/span")
        for i in range(len(column_names)):
            # print(column_names[i].text)
            if column_names[i].text == "CPU":
                cpu_use = column_names[i].text
                cpu_use_index = i + 1
                print(cpu_use_index)

        data = self.driver.find_element(By.XPATH, "//div[3]//div[" + str(process_name_index) + "]/span[" + str(
            cpu_use_index) + "]").text
        print(data)

        chrome_cpu_usage = f"{process_name} {cpu_use}: {data}"
        print(chrome_cpu_usage)

        result = self.driver.find_element(By.XPATH, "//p[@class='bg-warning']")

        self.assertEqual(result.text, chrome_cpu_usage, "CPU usage text didn't match.")
        print("Test passed.")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
