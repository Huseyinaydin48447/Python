
from githubUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class Github:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers=[]

    def sigIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH,'//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(self.password)

        time.sleep(1)
        self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[13]').click()

    def loadFollowers(self):
        items=self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed.col-12")

        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary.pl-1").text)

    def getFollowers(self):
        self.browser.get(f"https://github.com/Huseyinaydin48447?tab=following")
        time.sleep(2)

        self.loadFollowers()

        # while True:
        #     links = self.browser.find_element(By.CLASS_NAME,"BtnGroup").find_elements(By.Name,"a")

        #     if len(links) == 1:
        #         if links[0].text == "Next":
        #             links[0].click()
        #             time.sleep(1)
        #             self.loadFollowers()

        #         else:
        #             break
        #     else:
        #         for link in links:
        #             if link.text == "Next":
        #                 link.click()
        #                 time.sleep(1)
        #                 self.loadFollowers()
        #             else:
        #                 continue


github = Github(username, password)
github.sigIn()
github.getFollowers()
print(len(github.followers))
print(github.followers) 