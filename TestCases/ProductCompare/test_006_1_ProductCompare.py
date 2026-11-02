import os
import time

import pytest
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductsPage import ProductsPage

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_006_1_ProductCompare:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging


    def test_search_prod(self, setup):
        self.logger.info("**** test_006_1_ProductCompare started *** ")
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
        time.sleep(3)
        # Change to Products Page
        self.pp = ProductsPage(self.driver)
        self.pp.clickElement1img()
        time.sleep(2)
        self.pp.clickcompareimg()
        self.pp.clickSearch()
        #self.pp.clickElement2()
        self.pp.ProductComp()

        #End
        #self.driver.quit()




