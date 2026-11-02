from selenium.webdriver.common.by import By
# For Alerts
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():
    txt_email_xpath = "//input[@id='input-email']"
    # //*[@id="input-email"]
    # //*[@id="input-email"]
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//*[@id='form-login']/div[3]/button"
    # msg_myaccount_xpath =
    text_msg_conf_xpath = "//*[@id='content']/h1"
    text_loginwarning = "//*[@id='alert']/div/text()"
    btn_forgotpass_xpath = "//*[@id='form-login']/div[2]/a"
    alert="alert"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()



    def getmsgLoginFail(self):
        try:
            return self.driver.find_element(By.ID, self.alert).text

        except:
            return None

    def clickForgotPass(self):
        try:
            return self.driver.find_element(By.XPATH, self.btn_forgotpass_xpath).click()

        except:
            return None
