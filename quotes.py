from selenium import webdriver


class Quotes:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://quotes.toscrape.com/'

        self.exemplo = '/html/body/div/div[2]/div[2]/h2'

    def nav(self):
        self.driver.get(self.url)

    def getQuotes(self):
        self.driver.implicitly_wait(3)
        quotes = []
        lista_de_quotes = self.driver.find_elements_by_class_name('text')
        for i in lista_de_quotes:
            quotes += [i.text]

        return quotes

    def getAuthors(self):
        autores = []
        lista_de_autores = self.driver.find_elements_by_class_name('author')
        for i in lista_de_autores:
            autores += [i.text]
        return autores

    def showQuotes(self, which=None):
        if which is None:
            for quotes, autores in enumerate(self.getAuthors()):
                print(self.getQuotes()[quotes])
                print(autores)
                print('')


chromedriver = webdriver.Chrome()
quote = Quotes(chromedriver)

quote.nav()
quote.showQuotes()
