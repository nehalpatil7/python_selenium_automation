from os import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# Initialize the browser
browser = webdriver.Chrome()

# Open the website
browser.get("https://www.niarratravel.site/begin-my-journey")

# Wait for the login div to be present
login_div = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "login"))
)

# Find the username and password input fields within the login div
username_field = login_div.find_element(By.XPATH, "//input[@type='text']")
password_field = login_div.find_element(By.XPATH, "//input[@type='password']")
login_button = login_div.find_element(By.TAG_NAME, "button")

# Print the attributes of the username and password fields
# print("Username field attributes:", username_field.get_attribute("outerHTML"))
# print("Password field attributes:", password_field.get_attribute("outerHTML"))
# print("Button field attributes:", login_button.get_attribute("outerHTML"))

username_field.send_keys("nehalpatil653")
password_field.send_keys("Qwerty@1234")
login_button.click()

time.sleep(5)

for i in range(3):
    try:
        browser.find_element(By.XPATH, ".//img[@class='menu']").click()
        break
    except Exception:
        print("Exception occured")

cell_group = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cell-group"))
)

# Find the list of divs inside the cell-group
div_elements = cell_group.find_elements(By.TAG_NAME, "div")

# Click on the first div element (you can modify this as needed)
if div_elements:
    div_elements[0].click()
else:
    browser.quit()

time.sleep(5)

for i in range(19):
    try:
        optimize_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "content-box",
                )
            )
        ).find_element(By.TAG_NAME, "button")

        optimize_button.click()
        time.sleep(7)
    except:
        print("Optimize button error.")
        break

    try:
        rate_box_radio_group = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "flex.rate-box",
                )
            )
        ).find_element(By.XPATH, ".//div[@role='radiogroup']")

        radio_buttons = rate_box_radio_group.find_elements(By.XPATH, ".//div[@role='radio']")

        # Select the last radio button (assuming it's the last one in the list)
        if radio_buttons:
            last_radio_button = radio_buttons[-1]
            last_radio_button.click()
            print("Selected 5 stars.")

        time.sleep(2)
    except:
        print("Rating selection error.")
        break

    try:
        dropdown_group = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "van-cell.van-cell--clickable.evaluation",
                )
            )
        ).click()
        print("Dropdown clicked.")
        time.sleep(2)

        popup_div = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        "van-popup.van-popup--round.van-popup--bottom",
                    )
                )
            )

        popup_list = popup_div.find_elements(By.CLASS_NAME, "van-cell__value.van-cell__value--alone")

        if popup_list:
            random.choice(popup_list).click()
            print("Selected review.")
            time.sleep(2)

        button_wrap = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME,
                    "button-wrap",
                )
            )
        ).find_element(By.TAG_NAME, "button")

        button_wrap.click()
        print("Submitted.")
    except:
        print("Review selection error.")
        break

    time.sleep(5)
