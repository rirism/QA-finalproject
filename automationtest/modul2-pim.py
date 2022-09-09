import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

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

    # TC007
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

    #TC009
    def test_add_employee_a(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("Harry")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("Styles")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        self.driver.close()
    
    #TC010
    def test_add_employee_b(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("Harry")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/span').text
        self.assertIn('Required', response)
        self.driver.close()

    # TC011
    def test_add_employee_c(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("Styles")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/span').text
        self.assertIn('Required', response)
        self.driver.close()

    # TC012
    def test_add_employee_d(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("Harry")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("Styles")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/span').text
        self.assertIn('Required', response)
        self.driver.close()

    # TC013
    def test_add_employee_e(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("Harry")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("Styles")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys('0273')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/span').text
        self.assertIn('Employee Id already exists', response)
        self.driver.close()

    # TC014
    def test_add_employee_f(self):
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
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click() #Klik Add
        time.sleep(2)
        driver.find_element_by_name('firstName').send_keys("Harry")
        time.sleep(2)
        driver.find_element_by_name('lastName').send_keys("Styles")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys('1234567890')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click() #Klik Save
        time.sleep(2)
        response = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/span').text
        self.assertIn('Should not exceed 10 characters', response)
        self.driver.close()
   
if __name__ == "__main__": 
    unittest.main()