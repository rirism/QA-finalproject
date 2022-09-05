import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Admin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #TC006
    def test_search_success_a(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() #Klik Login Button
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click() #Klik Menu PIM
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Aaliyah Haq') #Input Nama Employee
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click() #Klik Search
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        self.assertIn('(1) Records Found', response)
        self.driver.close()

    #TC007
    def test_search_success_b(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() #Klik Login Button
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click() #Klik Menu PIM
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('0038') #Input ID Employee
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click() #Klik Search
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        self.assertIn('(1) Record Found', response)
        self.driver.close()

    #TC008
    def test_search_notfound(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() #Klik Login Button
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click() #Klik Menu PIM
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('9999') #Input ID Employee
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click() #Klik Search
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        self.assertIn('No Records Found', response)
        self.driver.close()

   
if __name__ == "__main__": 
    unittest.main()