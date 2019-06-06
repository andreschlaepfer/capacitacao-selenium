from selenium import webdriver


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com'
        self.search_bar = 'q'  # name
        self.search_click = 'btnK'  # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, string):
        self.driver.implicitly_wait(3)
        oi = self.driver.find_element_by_name('q')
        oi.send_keys(string)

        botao = self.driver.find_element_by_name(self.search_click)
        botao.location_once_scrolled_into_view
        botao.click()


chromedriver = webdriver.Chrome()
chrome = Google(chromedriver)

chrome.navigate()
chrome.search('facebook')
