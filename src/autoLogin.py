import time
import os
from decrypt import decrypt_credentials  # Decrypt credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Decrypt username and password and fetch Website URL details
USERNAME, PASSWORD, URL = decrypt_credentials()

# Detect available WebDriver
def get_webdriver():
    """Returns the correct WebDriver and browser type based on availability."""
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Move up to project root
    chrome_driver_path = os.path.join(project_dir, "webdrivers", "chromedriver.exe")
    firefox_driver_path = os.path.join(project_dir, "webdrivers", "geckodriver.exe")

    if os.path.exists(chrome_driver_path):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-using")
        options.add_argument("--disable-software-rasterizer")

        service = webdriver.ChromeService(executable_path=chrome_driver_path)
        return webdriver.Chrome(service=service, options=options), "chrome"

    elif os.path.exists(firefox_driver_path):
        options = webdriver.FirefoxOptions()
       #  options.add_argument("--headless")

        service = webdriver.FirefoxService(executable_path=firefox_driver_path)
        return webdriver.Firefox(service=service, options=options), "firefox"

    else:
        raise Exception("No WebDriver found. Please add ChromeDriver or GeckoDriver to 'webdrivers' folder.")

# Initialize WebDriver
driver, browser = get_webdriver()
print(f"Using {browser} WebDriver.")

def automate_punch_in():
    try:
        # Login Process
        print("Opening the login page...")
        driver.get(URL)

        print("Waiting for the username field to appear...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtUsername")))

        print("Entering username...")
        driver.find_element(By.CSS_SELECTOR, "input#txtUsername").send_keys(USERNAME)
        time.sleep(3)

        print("Entering password...")
        driver.find_element(By.CSS_SELECTOR, "input#txtPassword").send_keys(PASSWORD)
        time.sleep(3)

        print("Clicking the Login button...")
        driver.find_element(By.CSS_SELECTOR, "button#btnLogin").click()

        time.sleep(20)  # Wait for the page to load

        print("Waiting for Punch In button...")
        try:
            # Check if an iframe exists
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            print(f"Found {len(iframes)} iframes.")

            # If there's at least one iframe, switch to the first one
            if len(iframes) > 0:
                driver.switch_to.frame(iframes[0])
                print("Switched to first iframe.")

            # Wait until the button is present
            punch_in_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Punch In')]")))

            # Wait until the button is clickable
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Punch In')]")))

            # Try normal click first
            print("Clicking Punch In button...")
            punch_in_button.click()
            time.sleep(10)

        except Exception as e:
            print(f"Error: {e}")
            print("Trying JavaScript click...")
            driver.execute_script("arguments[0].click();", punch_in_button)

        print("Successfully punched in!")

        time.sleep(10)  # Wait before logout
        
        # Logout Process
        print("Clicking profile dropdown...")
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "logInUser"))).click()
        time.sleep(5)

        print("Clicking Logout button...")
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "btnLogOut"))).click()

        time.sleep(15)

        print("Successfully logged out!")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        time.sleep(5)
        driver.quit()  # Ensure browser closes

if __name__ == "__main__":
    automate_punch_in() 
