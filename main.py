from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


EMAIL = "Your mail"
PASSWORD = "Your password"

chrome_driver = "C:/Users/Meng Chien/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)


class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path=driver)
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        time.sleep(3)
        account = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        account.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        time.sleep(3)
        log_in_botton = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in_botton.click()
        time.sleep(3)
        dismiss1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        dismiss1.click()
        time.sleep(3)
        dismiss2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        dismiss2.click()

    def find_followers(self):
        time.sleep(3)
        find_follow = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')
        find_follow.click()

    def follow(self):
        time.sleep(3)
        buttons = self.driver.find_elements_by_css_selector("div div button")
        for x in buttons:
            try:
                x.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.quit()
insta = InstaFollower(chrome_driver)
insta.login()
insta.find_followers()
insta.follow()