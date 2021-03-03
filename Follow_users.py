from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

driver = webdriver.Chrome()

driver.get('https://github.com/login')
# enter with Login'
username = driver.find_element_by_id('login_field')
password = driver.find_element_by_id('password')

# values login
username.send_keys("user_name")
time.sleep(1)
password.send_keys("password")
time.sleep(1)

# login button
press_login = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
press_login.click()
time.sleep(1)

listname = 'Soldy','horberlan', '...'  # Add as many usernames as you want.
 

for name in listname:
    for page in range(1, 80):
        url = 'https://github.com/search?p={}&q={}&type=Users'.format(page, name)
        driver.get(url)
        time.sleep(1)

        # press button
        follow_user = driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")
         
         
        try:
            for i in follow_user:
                i.submit()
        except:
            pass
        time.sleep(1)
driver.close()