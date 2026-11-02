from selenium.webdriver.common.by import By


class HomePage():
    #Saber como se encontram estes elementos
    lnk_myaccount_xpath = "//*[@ id='top']/div/div/div[2]/ul/li[2]/div/span/span"
    #// a[ @ title = 'My Account']
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"
    lnk_logout_linktext = "//*[@id='top']/div/div/div[2]/ul/li[2]/div/ul/li[5]/a"

    txt_logoutconf = "//*[@id='content']/h1" #Account Logout

#saber como se comporta este construtor
    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_logout_linktext).click()

    def getconfirmationmsglogout(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_logoutconf).text
        except:
            None

