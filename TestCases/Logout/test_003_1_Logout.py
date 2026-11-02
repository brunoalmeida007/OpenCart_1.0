import pytest
import time

from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os


class Test_003_1_Logout():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******* Starting test_002_1_logout **********")
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

        # wait
        # time.sleep(5)
        # Alternative
        self.hp.clickMyAccount()
        self.map = MyAccountPage(self.driver)  # instancia para MyAccountPage que tem o botão Logout
        time.sleep(5)
        self.map.clickLogout()

        self.conflogout = self.map.clickContinue()
       # print(self.conflogout)
       # if self.conflogout == "None":
       #      self.driver.quit()
       #      assert True
       # else:
    #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
    #     self.driver.quit()
    #       assert False


# MyAccountPage
        #self.driver.quit()
        #time.sleep(2)
        # self.targetpage = self.lp.isMyAccountPageExists()
        # self.ma = MyAccountPage(self.driver) #instancia para MyAccountPage que tem o botão Logout
        # self.hp.clickLogout()
        # time.sleep(5)

        # self.confmsglogout = self.hp.getconfirmationmsglogout()

        # print(self.confmsglogout)

        #  if self.confmsglogout == "Account Logout":
        #     self.driver.quit()
        #     assert True
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
        #     self.driver.quit()
        #    assert False


