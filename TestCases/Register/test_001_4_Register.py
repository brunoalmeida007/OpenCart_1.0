import os
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig

class Test_001_4_Register:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("**** test_001.4_AccountRegistration started *** ")
        print(self.logger)

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")

        # self.title = driver.title
        # self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")

        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("Proving customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("")
        self.regpage.setLastName("")
        # self.regpage.setEmail("bcfa15@gmail.com")
        #self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail("")
        # self.regpage.setTelephone("65656565")
        self.regpage.setPassword("")
        # self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()

        self.msgfirstname = self.regpage.getmsgfirstname()
        self.msglastname = self.regpage.getmsglastname()
        self.msgemail = self.regpage.getmsgemail()
        self.msgpassword = self.regpage.getmsgpassword()

        print(self.msgfirstname)
        print(self.msglastname)
        print(self.msgemail)
        print(self.msgpassword)

        if  self.msgemail == "E-Mail Address does not appear to be valid!"\
            and self.msgpassword == "Password must be between 6 and 40 characters!":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "Test_001.4_AccountReg1.png")
            self.logger.error("Account registration is failed.")
            self.driver.quit()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")