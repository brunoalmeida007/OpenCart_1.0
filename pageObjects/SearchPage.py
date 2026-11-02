from selenium.webdriver.common.by import By


class SearchPage():
    search_xpath = "//*[@id='container']/header/div/div/div[2]/form/input"
    search_button ="//*[@id='container']/header/div/div/div[2]/form/button"
    title_displayed_Mac = "//*[@id='product-list']/div[2]/div/div[2]/div/h4/a"

    def __init__(self, driver):
        self.driver = driver

    def setProduct(self, product):
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(product)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_button).click()
