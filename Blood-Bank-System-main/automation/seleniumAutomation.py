from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random

service_obj = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("http://localhost:3000/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@class=' text-center text-gray-700 underline']").click()
time.sleep(2)

emailGenerator = random.randint(1000, 90000)
emailGen = str(emailGenerator)
# Donar Registration
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("testdonar")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testdonar"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1245624545")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("testdonar123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//a[@class=' text-center text-gray-700 underline']").click()
time.sleep(2)
#Hospital Registration
driver.find_element(By.XPATH, "//input[@value='hospital']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='hospitalName']").send_keys("testhospital")
driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("TestHospitalOwner")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testhospital"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("4567891235")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("testhospital123")
driver.find_element(By.XPATH, "//input[@id='website']").send_keys("testhosp.com")
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("testaddress, india")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//a[@class=' text-center text-gray-700 underline']").click()
time.sleep(2)
#Organization Registration
driver.find_element(By.XPATH, "//input[@value='organization']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='organizationName']").send_keys("testorganization")
driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("TestorganizationOwner")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testorganization"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("7894561235")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("testorganization123")
driver.find_element(By.XPATH, "//input[@id='website']").send_keys("testorg.com")
driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("testaddress, india")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)


# Login Organization
driver.find_element(By.XPATH, "//input[@value='organization']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testorganization"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("testorganization123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//span[contains(@class,'cursor-pointer')]").click()
time.sleep(2)
# Adding Inventory - IN 
driver.find_element(By.XPATH, "//span[normalize-space()='Add Inventory']").click()
time.sleep(2)
dd1 = Select(driver.find_element(By.XPATH, "//select[@id='bloodGroup']"))
dd1.select_by_visible_text("O+")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testdonar"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='quantity']").send_keys("40")
driver.find_element(By.XPATH, "//button[@class='ant-btn css-dev-only-do-not-override-1agqnk8 ant-btn-primary']").click()
time.sleep(5)

# Adding Inventory - OUT
driver.find_element(By.XPATH, "//span[normalize-space()='Add Inventory']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='out']").click()
time.sleep(2)
dd1 = Select(driver.find_element(By.XPATH, "//select[@id='bloodGroup']"))
dd1.select_by_visible_text("O+")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("testhospital"+emailGen+"@gmail.com")
driver.find_element(By.XPATH, "//input[@id='quantity']").send_keys("30")
driver.find_element(By.XPATH, "//button[@class='ant-btn css-dev-only-do-not-override-1agqnk8 ant-btn-primary']").click()
time.sleep(5)

driver.close()