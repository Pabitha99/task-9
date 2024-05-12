import os
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver_path="C:/Users/Pabitha/PycharmProjects/chromedriver.exe"
os.environ["PATH"] += os.pathsep+os.path.dirname(driver_path)
# Create a ChromeOptions object
chrome_options = Options()

# Add experimental option
chrome_options.add_experimental_option("detach", True)
# Initialize the WebDriver with ChromeOptions
chr_driver = webdriver.Chrome(options=chrome_options)
# Load the webpage
chr_driver.get("https://www.saucedemo.com/")
# printing title of web page
print(chr_driver.title)
print(chr_driver.current_url)
driver=chr_driver.find_element(By.ID,"user-name")
driver.send_keys("standard_user")
# driver.click()
time.sleep(4)
driver=chr_driver.find_element(By.ID,"password")
driver.send_keys("secret_sauce")
time.sleep(4)
driver=chr_driver.find_element(By.ID,"login-button")
driver.click()

# extracting body element
# pagec = chr_driver.find_element(By.TAG_NAME,"body").text
file=open(r"C:\Users\Pabitha\PycharmProjects\sampletest\Webpage_task_11.txt","x")
driver=chr_driver.find_element(By.XPATH,"/html")
files=open(r"C:\Users\Pabitha\PycharmProjects\sampletest\Webpage_task_11.txt","w")
files.write(driver.text)
file.close()
files.close()
chr_driver.quit()


