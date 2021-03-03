from selenium import webdriver
import time
import sys

#Firefox used
driver = webdriver.Firefox()

driver.get("http://github.com/login")

username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")

# password and username need to go into these values
username.send_keys("user_name")
time.sleep(1)
password.send_keys("password")
time.sleep(1)


login_form = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
login_form.click()
time.sleep(1)

prepend = ["horberlan"]


for user in prepend:
    for i in range(0, 200):
        for t in range(1, 100):
            string = "https://github.com/horberlan?tab=following"
            driver.get(string)
            time.sleep(1)

            follow_button = driver.find_elements_by_class_name("btn.btn-sm")
            time.sleep(0.3)

            try:
                for i in follow_button:
                    i.submit()
            except:
                pass
            time.sleep(1)
driver.close()
