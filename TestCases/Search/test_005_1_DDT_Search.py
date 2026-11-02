import time
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.ProductsPage import ProductsPage
from pageObjects.SearchPage import SearchPage
from utilities import XLUtils
from utilities.ReadProperties import ReadConfig
from utilities.CustomLogger import LogGen
import os

class Test_Search_1_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_SearchDataMac.xlsx"

    def test_Search_005_1_ddt(self,setup):
        self.logger.info("**** Starting test_005_1_DDT_Search_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1') #retorna numero de linhas
        lst_status=[]

        self.driver = setup #driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.sp = SearchPage(self.driver)
        self.pp = ProductsPage(self.driver)

        for r in range(2, self.rows + 1):  # 2 to 5


            # read from the excel data
            self.productddt = XLUtils.readData(self.path, "Sheet1", r, 1)

            # set from the data
            self.sp.setProduct(self.product)
            self.sp.clickSearch()

            time.sleep(2)

            #Change to Products Page

            #self.pp.isProductExistsMac(self.product)

            self.targetproduct = self.pp.isProductExistsMac(self.productddt)
            print(self.targetproduct)

            if self.targetproduct == self.productddt:
                assert True
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
                assert False
            self.driver.quit()



