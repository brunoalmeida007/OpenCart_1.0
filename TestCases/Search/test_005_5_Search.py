import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductsPage import ProductsPage

from utilities.CustomLogger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_005_5_Search:
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
        self.logger.info("clicking on MyAccount--> register")

        # Não esquecer que podemos por este product em 1 Lista- Fazer depois o DDT
        self.sp = SearchPage(self.driver)
        self.product = "Mac"
        self.sp.setProduct(self.product)
        self.sp.clickSearch()

        # Change to Products Page
        self.pp = ProductsPage(self.driver)
        #self.mylist = ["iMac", "MacBook", "MacBook Air", "MacBook Pro"]
        self.listproduct = self.pp.ListProduct_Mac


        print(self.listproduct)

       # for element in self.listproduct:
       #     print(f"Paragraph text:{element.text}")

       # if self.listproduct == self.mylist:
       #    assert True
       # else:
       #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
       #     assert False
       # self.driver.quit()