import pytest
import time

from pageObjects import MyAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os

class Test_002_2_Login():

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_2_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        self.msgLoginFail = self.lp.getmsgLoginFail()
        time.sleep(5)
        print(self.msgLoginFail)  # print text

       #  if self.msgLoginFail == "":
       #     assert True
       #     self.driver.quit()
       # else:
       #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "Test_001_AccountReg1.png")
       #     self.logger.error("Account registration is failed.")
       #     self.driver.quit()
       #     assert False
       # self.logger.info("**** test_002_2_login finished *** ")

       # self.driver.quit()
