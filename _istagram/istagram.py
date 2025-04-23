from instagramUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        
        # options parametresi kullanılmalı
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username=username
        self.password=password
        # self.followers=[]
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
 
        usernameInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        passwordInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
         
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//a[contains(@href, '/followers/')]").click()
        time.sleep(5)  
        
        dialog=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] div")
        # followerCount=len(dialog.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3'))
        followerCount=len(dialog.find_elements(By.CSS_SELECTOR,'div[role=button][tabindex="0"]'))

        print(f"first count: {followerCount}")

        action =webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount=len(dialog.find_elements(By.CSS_SELECTOR, 'div[role=button][tabindex="0"]'))
            if followerCount !=newCount:
                followerCount=newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break
        followers=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')

        for user in followers:
            try:
                unfollow_button = user.find_element(By.XPATH, ".//div[contains(text(), 'Çıkar')]")
                if unfollow_button:
                    link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    print(f"Unfollow user: {link}")
            except:
                pass
    
    def followUser(self,username): 
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)

        followButtom=self.browser.find_element(By.TAG_NAME,"button")
        # if followButtom.text !="Takiptesin":
        if followButtom.text !="Following":
            followButtom.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME,"button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div').click()
        else:
            print("zaten takip etmiyorsunuz.")


instagram=Instagram(username,password)
instagram.signIn()
# instagram.getFollowers()
# instagram.followUser("kod_evreni")
instagram.unFollowUser("kod_evreni")