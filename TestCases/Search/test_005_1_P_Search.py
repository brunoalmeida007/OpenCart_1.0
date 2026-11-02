import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductsPage import ProductsPage

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig


# Objectivo do teste é passar o parametro Produto que é uma string com o valor ="MacBook"

class Test_005_1_Search:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # for logging

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_prod(self, setup):
        self.logger.info("**** test_005_1_Search started *** ")
        print(self.logger)

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching application")

        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.logger.info("Search --> Search")

        # Não esquecer que podemos por este product em 1 Lista- Fazer depois o DDT
        self.sp = SearchPage(self.driver)
        self.productP = "MacBook"

        self.sp.setProduct(self.productP)
        self.sp.clickSearch()

        # Change to Products Page
        self.pp = ProductsPage(self.driver)

        self.targetproduct = self.pp.isProductExistsP(self.productP)
        print(self.targetproduct)

        if self.targetproduct == self.productP:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            assert False
        self.driver.quit()
