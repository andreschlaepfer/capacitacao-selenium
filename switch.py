from selenium import webdriver
import time


class Switch:
    def __init__(self, driver):
        self.driver = driver
        self.url1 = 'http://www.facebook.com'
        self.url2 = 'http://google.com'

    def nav(self):
        self.driver.get(self.url1)

    def switchTo(self, url):
        self.driver.implicitly_wait()

        self.driver.get(url)


chrome = webdriver.Chrome()

troca = Switch(chrome)

troca.nav()
time.sleep(3)
troca.switchTo('http://google.com')
