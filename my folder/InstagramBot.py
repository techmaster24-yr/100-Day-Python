from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException, ElementClickInterceptedException
import time

insta_email = "Your Email"
insta_password = "Your Password"
account_name = "Your Account Name"
instagram_URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.insta_URL = instagram_URL
        self.favourite_account = account_name
        self.user_email = insta_email
        self.user_password = insta_password

    # --------- INSTAGRAM TOGIN FUNCTIONS ------------>>

    def login(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.Instagram_driver = webdriver.Chrome(options=chrome_options)
        self.Instagram_driver.get(self.insta_URL)
        time.sleep(1)
        try:
            username_input = self.Instagram_driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'
            )
            username_input.send_keys(self.user_email)
            instagram_password = self.Instagram_driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input'
            )
            instagram_password.send_keys(self.user_password)
            time.sleep(2)
            username_input.send_keys(Keys.ENTER)
            instagram_password.send_keys(Keys.ENTER)
            time.sleep(4)
            popups_1 = self.Instagram_driver.find_element(
                By.XPATH, '//div[text()="Not now"]'
            )
            popups_1.click()
            time.sleep(4)
        except NoSuchElementException:
            print("Nooo element!")

#-------=======================>>>>>>  POP UP THE FOLLOWERS PAGE ---------------------------------
    def find_followers(self):
        try:
            self.Instagram_driver.get(f"{instagram_URL}/{account_name}/")
            time.sleep(2)
            followers_button = self.Instagram_driver.find_element(
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a",
            )
            followers_button.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Nooo element!")

# ============>>> FOLLOW TO EACH FOLLOWERS =================================>>>>>>
    def follow(self):
        for n in range(1, 500):
            try:
                Follow = self.Instagram_driver.find_element(
                    By.XPATH,
                    f"/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{n}]/div/div/div/div[3]/div/button/div/div",
                )
                Follow.click()
                self.Instagram_driver.execute_script(
                    "arguments[0].scrollIntoView();", Follow
                ) #You can also use 'arguments[0].scrollTop=arguments[0].scrollHeight,follow in this case
                time.sleep(3)
            except ElementClickInterceptedException:
                dismiss_popup = self.Instagram_driver.find_element(
                    By.XPATH,
                    "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]",
                )
                dismiss_popup.click()
                self.Instagram_driver.execute_script(
                    "arguments[0].scrollIntoView();", Follow
                )
                time.sleep(3)
Insta_Bot = InstaFollower()
Insta_Bot.login()
Insta_Bot.find_followers()
Insta_Bot.follow()