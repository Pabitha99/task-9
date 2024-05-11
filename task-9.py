import os
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
# extracting body element
pagec = chr_driver.find_element(By.TAG_NAME,"body").text
chr_driver.quit()
# write extracted content
with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(pagec)

print("Content extracted and saved")