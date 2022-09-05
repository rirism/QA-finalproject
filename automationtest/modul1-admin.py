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
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #TC001
    def test_search_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('alice.duval')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        self.assertIn('Record Found', response)
        self.driver.close()

    #TC002
    def test_search_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('alice')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span').text
        self.assertIn('No Records Found', response)
        self.driver.close()

    #TC003
    def test_add_user_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")  
        time.sleep(3)
        driver.find_element_by_name("username").send_keys("Admin")  
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("admin123")  
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click() #Klik Login Button
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click() #Klik Menu Admin
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add Button
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click() #Dropdown User Role
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]').send_keys("Admin") #Pilih User Role Admin
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Alice Duval") #Isi nama Employee
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]').click() #Dropdown Status
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]').send_keys("Enabled") #Pilih Status Enabled
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()