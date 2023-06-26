import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def vote_for_player():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Make sure you have the ChromeDriver executable in your system PATH
    #driver.get("https://www.ligaportal.at/tir/bezirksliga/bezirksliga-west/spieler-der-runde/46627-bezirksliga-west-waehle-den-beliebtesten-hausbaufuehrer-at-spieler-der-saison-22-23")

    driver.get("http://mt191087.students.fhstp.ac.at/PHP_EWEBP/datenbank/index.php")

    # Wait for the checkbox element to be visible and clickable
    link1 = driver.find_element(By.LINK_TEXT, "Zum Forum")
    link1.click()
    time.sleep(3)

    link = driver.find_element(By.CLASS_NAME, "a.gb-close")
    link.click()

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "save")))
    button.click()

    time.sleep(10)

    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
    
    # Check the checkbox
    checkbox.click()
    # # Continue with the voting process
    # player_id = "12345"  # Replace with the specific player ID
    # payload = {"player_id": player_id}

    # # Send a POST request to cast the vote
    # response = requests.post("https://example.com/vote", data=payload)

    # # Check if the vote was successful
    # if response.status_code == 200:
    #     print("Vote casted successfully!")
    # else:
    #     print("Vote failed. Please try again later.")

    # # Close the browser window
    driver.quit()

# vote_for_player()
# Main script loop
# while True:
#     vote_for_player()
#     time.sleep(660)  # Wait for 11 minutes (660 seconds) before casting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
#driver.get("http://www.python.org")
driver.get("https://www.ligaportal.at/tir/bezirksliga/bezirksliga-west/spieler-der-runde/46627-bezirksliga-west-waehle-den-beliebtesten-hausbaufuehrer-at-spieler-der-saison-22-23")
# assert "Python" in driver.title
#elem = driver.find_element(By.ID, "id-search-field")
#time.sleep(2)
#closeNotifications = driver.find_element(By.CLASS_NAME, "gb-push-denied")
# closeNotifications = driver.find_element(By.XPATH, "/html/body/app-root")
#closeNotifications.click()
#time.sleep(1)
#Scrape = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "action-buttons")))
Scrape = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "script#client-app-state")))
# closeNotification = driver.find_element(By.XPATH, "/html/body/app-root")
# element_attribute_value = closeNotification.get_attribute('innerHTML')

# time.sleep(3)


# iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "iframeDefaultSize")))
# # We switch to that iframe
# driver.switch_to.frame(iframe)
# # Once we switched to the iframe, we can get the elements you wanted
# time.sleep(1)
# blocks = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/app-root/app-theme/div/div/app-notice/app-theme/div/div/app-home/div/div[2]/app-footer/div/div[2]/app-action-buttons/div/button[2]")))
# blocks.click()

# # element_attribute_value = closeNotifications.get_attribute('innerHTML')
# # print(element_attribute_value)
# time.sleep(2)

# #/html/body/div[10]/div/div/div[2]/a


# # closeCookies = driver.find_element(By.XPATH, "/html/body/app-root/app-theme/div/div/app-notice/app-theme/div/div/app-home/div/div[2]/app-footer/div/div[2]/app-action-buttons/div/button[2]")
# # closeCookies.click()
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# time.sleep(5)
# # assert "No results found." not in driver.page_source
# driver.close()