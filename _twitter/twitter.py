from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        
        # options parametresi kullanılmalı
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username=username
        self.password=password

    def singIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(4)

        usernameInput=self.browser.find_element(By.XPATH,"//input[@autocomplete='username']")
        usernameInput.send_keys(self.username)

        btmSubmit=self.browser.find_element(By.XPATH,"//span[contains(text(), 'Next')]")
        btmSubmit.click()
        time.sleep(4)

        passwordInput=self.browser.find_element(By.XPATH,"//input[@autocomplete='current-password']")
        passwordInput.send_keys(self.password)
        time.sleep(4)

        btmSubmit=self.browser.find_element(By.XPATH,"//span[contains(text(), 'Log in')]")
        btmSubmit.click()
        time.sleep(4)
    
    def search(self,hashtag):
        searchInput=self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(6)
        results = []
        list = self.browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']//span")   
        time.sleep(2)
        print("count: "+ str(len(list)))

        for i in list:
            results.append(i.text)



        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 3:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1

        list = self.browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']//span")        
        time.sleep(2)
        print("count: "+ str(len(list)))
        for i in list:
          results.append(i.text)

        
        count = 1
        with open("tweets.txt","w",encoding="UTF-8") as file:
         for item in results:
             file.write(f"{count}-{item}\n")
             count+=1     
        
        # for item in list:
        #     print(item.text)
        #     print("*************")
        #     print(len(item))
twitter=Twitter(username,password)
twitter.singIn()
twitter.search("python") 