from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to the EdgeDriver executable
edge_driver_path = "D:/python_learn/msedgedriver.exe"  # Replace with your actual path

# Set up Edge options (if needed)
edge_options = Options()

# Initialize the WebDriver
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# Open Facebook login page
driver.get("https://www.facebook.com")

# Wait for the page to load
time.sleep(3)  # You may adjust the sleep duration as needed

# Locate the email and password input fields and login button
email_field = driver.find_element(By.ID, "email")  # Replace with the correct ID or selector
password_field = driver.find_element(By.ID, "pass")  # Replace with the correct ID or selector
login_button = driver.find_element(By.NAME, "login")  # Replace with the correct name or selector

# Enter email and password
email_field.send_keys("7095444102")  # Replace with your email
password_field.send_keys("Thulasi@05")  # Replace with your password

# Click the login button
login_button.click()
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='feed']"))  # Adjust based on the actual home page
)

# Scroll down by 1000 pixels
driver.execute_script("window.scrollBy(0, 1000);")

# Wait to see the result of scrolling
time.sleep(5)  # Adjust as needed

# Check for any alerts or errors
try:
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except:
    pass

# Wait to see the result
  # Adjust as needed


# Close the browser
#driver.quit()
