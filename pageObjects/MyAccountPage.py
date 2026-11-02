from selenium.webdriver.common.by import By


class MyAccountPage():
    msg_myaccount = "Subscriptions"
    lnk_logout = "Logout"

    txt_logoutconf= "//*[@id='content']/h1" #Account Logout
    continue_button ="Continue"

    def __init__(self, driver):
        self.driver = driver

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.LINK_TEXT, self.msg_myaccount).text

        except:
            return None

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_logout).click()

    def getconfirmationmsglogout(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_logoutconf).text
        except:
            None

    def clickMyAccount2(self):

        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()


    def clickLogout2(self):

        self.driver.find_element(By.XPATH, self.lnk_logout2_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.LINK_TEXT,self.continue_button).click()

