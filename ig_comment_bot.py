from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random

class Instagrambot: 
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        user_local = driver.find_element_by_xpath("//input[@name='username']")
        user_local.click()
        user_local.clear()
        user_local.send_keys(self.username)
        pass_local = driver.find_element_by_xpath("//input[@name='password']")
        pass_local.click()
        pass_local.clear()
        pass_local.send_keys(self.password)
        time.sleep(1)
        pass_local.send_keys(Keys.RETURN)
        time.sleep(4)
        self.comment_on_the_photo()
        

    def comment_on_the_photo(self):
        driver = self.driver
        #set number of repetitions
        n = 1
        for i in range(0,n):
            # insert photo url on the bottom line
            driver.get('https://www.instagram.com/p/CLZx-s6hNhu/')
            time.sleep(3)
            # set the list of comments 
            comments =["vc é muito gato","pqp, queria pegar vc","lindooooo"] 
            driver.find_element_by_class_name('Ypffh').click()
            comment_local = driver.find_element_by_class_name('Ypffh')
            time.sleep(random.randint(2, 5))
            comment_chosen = random.choice(comments)
            comment_local.send_keys(comment_chosen)
            time.sleep(2)
            driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
            # set the interval bettwen comments
            time.sleep(random.randint(60,200))
        print('finished')


# insert the credecials
igbot = Instagrambot('user','password')
igbot.login()