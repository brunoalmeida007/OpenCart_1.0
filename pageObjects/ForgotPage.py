from selenium.webdriver.common.by import By


class ForgotPage():
    txt_email_xpath = "//*[@id='input-email']"
    text_message = "//*[@id='account-login']/div[1]/text()"
    btn_continue_xpath= "//*[@id='form-forgotten']/div/div[2]/button"
    info="/html/body/div/main/div[2]/div[1]/text()"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def checkmessage(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_message).text

        except:
            return None

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def getmsgEmailSent(self):
            try:
                return self.driver.find_element(By.XPATH, self.info).text

            except:
                return None