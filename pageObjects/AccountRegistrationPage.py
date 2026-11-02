from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    #txt_telphone_name = "telephone"
    txt_password_name = "password"
    #txt_confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//*[@id='form-register']/div/button"

    text_msg_conf_xpath = "/html/body/div/main/div[2]/div/div/h1"

    text_msg_conf_firstnameerror = "//*[@id='error-firstname']"
    text_msg_conf_lastnameerror = "//*[@id='error-lastname']"
    text_msg_conf_emailerror = "// *[ @ id = 'error-email']"
    text_msg_conf_passerror = "// *[ @ id = 'error-password']"
    text_msg_alert= "//*[@id='alert']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

   # def setTelephone(self, tel):
      #  self.driver.find_element(By.NAME, self.txt_telphone_name).send_keys(tel)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

   # def setConfirmPassword(self, cnfpwd):
       # self.driver.find_element(By.NAME, self.txt_confpassword_name).send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None

    def getmsgfirstname(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_firstnameerror).text
        except:
            None

    def getmsglastname(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_lastnameerror).text
        except:
            None

    def getmsgemail(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_emailerror).text
        except:
            None

    def getmsgpassword(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_passerror).text
        except:
            None

    def getmsgEmailError(self):
        try:
            return self.driver.find_element_by_tag_name('Insira uma parte depois de "@". "a@" está incompleto.')
        except:
            None

    def getmsgAlert(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_alert).text
        except:
            None
