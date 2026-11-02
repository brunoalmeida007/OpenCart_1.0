import pytest
import time

from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os


class Test_002_1_Login():
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
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.map = MyAccountPage(self.driver)
        self.targetpage = self.map.isMyAccountPageExists()

        print(self.targetpage)

        if  self.targetpage =="Subscriptions":
            assert True
            self.driver.quit()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            self.driver.quit()
            assert False
