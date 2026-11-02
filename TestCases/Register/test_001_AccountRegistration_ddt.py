import time
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os

class Test_AccountReg_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_RegisterData.xlsx"

    def test_AccountRegister_ddt(self,setup):
        self.logger.info("**** Starting test_001_DDT_AccountRegister_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1') #retorna numero de linhas
        lst_status=[]

        self.driver = setup #driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
       # self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class
        self.rp= AccountRegistrationPage(self.driver)

        for r in range(2,self.rows+1): #2 to 5
            self.hp.clickMyAccount()
            #self.hp.clickLogin()
            self.hp.clickRegister()
#read from the excel data
            self.firstname = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.lastname = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.email=XLUtils.readData(self.path,"Sheet1",r,3)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 4)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 5)
#set from the data
            self.rp.setFirstName(self.firstname)
            self.rp.setLastName(self.lastname)
            self.rp.setEmail(self.email)
            self.rp.setPassword(self.password)

            self.rp.setPrivacyPolicy()
            self.rp.clickContinue()

            time.sleep(5)

            self.confmsg = self.rp.getconfirmationmsg()

            print(self.confmsg)

            if self.exp=='Valid':
                if self.confmsg== "Your Account Has Been Created!":
                    lst_status.append('Pass')
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()

            elif self.exp=='Invalid':
                if self.confmsg== "Register Account":
                    lst_status.append('Fail')
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()

                else:
                    lst_status.append('Pass')
                    self.hp.clickMyAccount()
                    self.ma.clickLogout()

        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_004_AccountRegister_Datadriven **********")
