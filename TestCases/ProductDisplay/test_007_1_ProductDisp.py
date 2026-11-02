import os
import time

import pytest
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductsPage import ProductsPage

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_007_1_ProductCompare:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_prod(self, setup):
        self.logger.info("**** test_007_1_ProductDisp started *** ")
        print(self.logger)

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")

        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("Search --> Search")

        # Não esquecer que podemos por este product em 1 Lista- Fazer depois o DDT
        self.sp = SearchPage(self.driver)
        self.product = "Mac"

        self.sp.setProduct(self.product)
        self.sp.clickSearch()
        time.sleep(2)
        # Change to Products Page
        self.pp = ProductsPage(self.driver)
        self.pp.clickElement1img()
        time.sleep(1)
        self.pp.clickElement1img2()
        time.sleep(1)
        self.pp.clickbuttonright()
        time.sleep(2)
        self.pp.clickbuttonX()

       # if self.targetproduct == "MacBook":
       #     assert True
       # else:
       #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
       #     assert False
       # self.driver.quit()