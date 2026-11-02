import os
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig

class Test_001_1_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging
    #print(logger.path)
    # opencartdemo
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("**** test_001_AccountRegistration started *** ")
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

        self.regpage.setFirstName("Bruno")
        self.regpage.setLastName("Almeida")
        # self.regpage.setEmail("bcfa15@gmail.com")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        # self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz1")
        # self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()

        self.confmsg = self.regpage.getconfirmationmsg()

        print(self.confmsg)

        if self.confmsg == "Register Account":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "Test_001_AccountReg1.png")
            self.logger.error("Account registration is failed.")
            self.driver.quit()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")

