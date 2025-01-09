
import time
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manage the correct version of ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_loader import fetch_proxy_list
import random

def scrape_twitter_trends(proxymesh_url, twitter_username, twitter_useremail, twitter_password):
    # Fetch proxy list and select a random proxy
    proxy_list = fetch_proxy_list(proxymesh_url)
    if not proxy_list:
        raise ValueError("No proxies available from ProxyMesh.")
    
    # Select a random proxy and fetch its IP and port
    selected_proxy = random.choice(proxy_list)
    proxy_ip = selected_proxy["ip"]
    proxy_port = selected_proxy["port"]
    print(f"Using proxy: {proxy_ip}:{proxy_port}")

    # Configure WebDriver with the selected proxy
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy_ip}:{proxy_port}')  # Use the correct proxy IP and port
    # Uncomment to run without headless mode:
    # chrome_options.add_argument("--headless")

    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Navigating to Twitter login page
        driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        print("Waiting for username field...")

        # Enter credentials
        # Waiting for the username input to appear and send keys
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
        ).send_keys(twitter_useremail)
        print("Useremail entered.")
        
        
         # Click the next button to go to password page
        next_button_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]"
        driver.find_element(By.XPATH, next_button_xpath).click()
        print("Clicked next button.")
        time.sleep(3)

        try:
            # XPaths
            password_input_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
            username_input_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input"
            next_button_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button"
            login_button_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button"

            try:
            # Try to locate the password input field
                password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, password_input_xpath))
                )
                # Input the password if the field is found
                password_input.send_keys(twitter_password)
                print("Password field found and filled.")

                login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, login_button_xpath))
                )
                login_button.click()
                print("Login button clicked.")

            except Exception:
                print("Password field not found, trying the username field.")
                # Locate the username input field
                username_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, username_input_xpath))
                )
                username_input.send_keys(twitter_username)
                print("Username field found and filled.")

                # Locate and click the "Next" button
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, next_button_xpath))
                )
                next_button.click()
                print("Next button clicked.")
                
                # Locate the password input field
                new_password_input_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
                new_password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, new_password_input_xpath)))

                new_password_input.send_keys(twitter_password)
                print("Password field found and filled.")

                # Locate and click the "Next" button
                new_login_xpath = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button"
                new_login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, new_login_xpath))
                )
                new_login_button.click()
                print("Login button clicked!")
                

        except Exception as e:
            print(f"Error during login process: {e}")
            raise
            

        # Fetch "What’s Happening" section
        try:
            time.sleep(3)
            # Wait for the "What’s Happening" section to load using a new XPath
            whats_happening_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending now')]")
            )
            )
    
            # Locate the trending section
            trending_section = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending now')]")
    
            # Find all elements within the trending section 
            elements = trending_section.find_elements(By.XPATH, ".//div[@dir='ltr']")
    
            # Extract text from the first 5 elements
            trend_names = []
            for i, element in enumerate(elements[:5]):  # Limit to the first 5 elements
                text = element.text.strip()
                if text:
                    trend_names.append(text)
                else:
                    print(f"Element {i+1} has no text.")

            # Raising an error if no trends are found
            if not trend_names:
                raise ValueError("No trends found in the 'What’s Happening' section.")

                print("Extracted trends:", trend_names)

        except Exception as e:
            print("Error fetching trends:", e)
            raise  # Optionally raising the exception for higher-level handling



        # Record details
        unique_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = driver.execute_script("return window.navigator.platform")  # Placeholder for actual proxy IP
        
        # Result
        result = {
            "unique_id": unique_id,
            "trends": trend_names,
            "timestamp": timestamp,
            "ip_address": selected_proxy
        }
 
        return result
    finally:
        driver.quit()
