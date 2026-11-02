import os
import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig

class Test_001_10_Register:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_account_reg(self, setup):
        self.logger.info("**** test_001_9_AccountRegistration started *** ")
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

        self.rp = AccountRegistrationPage(self.driver)

        self.rp.setFirstName("Bruno")
        self.rp.setLastName("Almeida")
        # self.regpage.setEmail("bcfa15@gmail.com")
        #self.email = randomeString.random_string_generator() + '@gmail.com'
        self.rp.setEmail("@")
        # self.regpage.setTelephone("65656565")
        self.rp.setPassword("123456")
        # self.regpage.setConfirmPassword("abcxyz")
        self.rp.setPrivacyPolicy()
        self.rp.clickContinue()

        time.sleep(3)
        self.msgEmailFail = self.rp.getmsgEmailError()
        # time.sleep(5)



        #print(self.msgEmailFail)  # print text

        # Get Text
        #print(element.text)

        if  self.alertwindow.text == "Insira uma parte depois de '@'. 'a@' está incompleto.":
            #and self.msgpassword == "Password must be between 6 and 40 characters!":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "Test_001.4_AccountReg1.png")
            self.logger.error("Account registration is failed.")
            self.driver.quit()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")