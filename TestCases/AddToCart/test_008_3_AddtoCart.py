import os
import pytest
import time

from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductsPage import ProductsPage

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_008_1_AddtoCart:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging


    def test_search_prod(self, setup):
        self.logger.info("**** test_008_1_AddtoCart started *** ")
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
        self.pp.clickiMac()
        time.sleep(2)
        self.pp.clickAddtoCart()
        time.sleep(3)
        self.pp.clickShoppingCartBtn()
        time.sleep(3)
        self.pp.clickShoppingCartBtn2()

        #time.sleep(5)
        #self.pp.clickCart()
        #time.sleep(5)
        #self.pp.clickCheckout()
        #time.sleep(5)






