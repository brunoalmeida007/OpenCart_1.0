import pytest
import time

from pageObjects import MyAccountPage
from pageObjects.ForgotPage import ForgotPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os


class Test_004_1_ForgotPass():

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)

        self.lp.clickForgotPass()

        self.fp = ForgotPage(self.driver)
        self.fp.setEmail(self.user)

        self.fp.clickContinue()

        self.msgalert = self.fp.getmsgEmailSent()
        # time.sleep(5)
        print(self.msgalert)  # print text

      #  self.message= self.fp.checkmessage()
      #  print(self.message)

        self.driver.quit()



