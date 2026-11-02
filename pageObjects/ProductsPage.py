from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver


class ProductsPage():
    lnk_txt_iMac = "//*[@id='product-list']/div[1]/div/div[2]/div/h4/a"



    txt_Mac2 = "iMac"
    txt_Mac3 = "MacBook Air"
    noproduct = "//*[@id='content']/p"
    my_list_MAC = ["iMac", "MacBook", "MacBook Air", "MacBook Pro"]
    txt_MAC = "Mac"
    ## This is XPath elements- Compare this Products links for iMac e MacBook
    link_C_Mac1 = "/html/body/div/main/div[2]/div/div/div[5]/div[1]/div/div[2]/form/div/button[3]"
    link_C_Mac2 = "//*[@id='product-list']/div[2]/div/div[2]/form/div/button[3]"

    link_productcomp = "//*[@id='compare-total']"

    link_img_imac = "//*[@id='product-list']/div[1]/div/div[1]/a/img"
    link_img_imac2 = "//*[@id='content']/div[1]/div[1]/div/a/img"
    link_btn_right = "/html/body/div[2]/div/button[2]"
    link_btn_X = "/html/body/div[2]/div/div[1]/div/button"
    link_compare_imac = "//*[@id='content']/div[1]/div[2]/form/div/button[2]"
    link_search = "Search"

    link_iMac_img = "//*[@id='product-list']/div[1]/div/div[1]/a/img"
    link_addtocart = "//*[@id='button-cart']"
    link_shop_cart = "//*[@id='cart']/div/button"
    link_shop_cart2="//*[@id='cart']/div/ul/li/div/p/a[1]/strong"
    link_checkout = "//*[@id='cart']/div/ul/li/div/p/a[2]/strong"

    # Product Display
    text_msg_name = "//*[@id='content']/div[1]/div[2]/h1"
    text_msg_brand = "//*[@id='content']/div[1]/div[2]/ul[1]/li[1]/a"
    text_msg_prodcod = "//*[@id='content']/div[1]/div[2]/ul[1]/li[2]"

    def __init__(self, driver):
        self.driver = driver

    def isProductExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.lnk_txt_iMac).text
        except:
            return None

    def isProductExistsP(self, productP):
        try:
            return self.driver.find_element(By.LINK_TEXT, productP).text
        except:
            return None

    def NoProduct(self):
        try:
            return self.driver.find_element(By.XPATH, self.noproduct).text
        except:
            return None

    @property
    def ListProduct_Mac(self):

        try:
            ele1 = self.driver.find_element(By.LINK_TEXT, self.txt_Mac1).text
            # ele2=self.driver.find_element(By.LINK_TEXT, self.txt_Mac3).text
            # ele3=self.driver.find_element(By.LINK_TEXT, self.txt_Mac2).text

            return ele1
        except:
            return None

    def isProductExistsMac(self, productddt):

        try:
            return self.driver.find_element(By.LINK_TEXT, productddt).text
        except:
            return None

    def clickElement1(self):
        self.driver.find_element(By.XPATH, self.link_C_Mac1).click()

    def clickElement2(self):
        self.driver.find_element(By.XPATH, self.link_C_Mac2).click()

    def ProductComp(self):
        self.driver.find_element(By.XPATH, self.link_productcomp).click()

    def clickElement1img(self):
        self.driver.find_element(By.XPATH, self.link_img_imac).click()

    def clickElement1img2(self):
        self.driver.find_element(By.XPATH, self.link_img_imac2).click()

    def clickbuttonright(self):
        self.driver.find_element(By.XPATH, self.link_btn_right).click()

    def clickbuttonX(self):
        self.driver.find_element(By.XPATH, self.link_btn_X).click()

    def clickcompareimg(self):
        self.driver.find_element(By.XPATH, self.link_compare_imac).click()

    def clickSearch(self):
        self.driver.find_element(By.LINK_TEXT, self.link_search).click()

    def clickiMac(self):
        self.driver.find_element(By.XPATH, self.link_iMac_img).click()

    def clickAddtoCart(self):
        self.driver.find_element(By.XPATH, self.link_addtocart).click()

    def clickShoppingCartBtn(self):
        self.driver.find_element(By.XPATH, self.link_shop_cart).click()

    def clickShoppingCartBtn2(self):
        self.driver.find_element(By.XPATH, self.link_shop_cart2).click()

    def clickCheckout(self):
        self.driver.find_element(By.XPATH, self.link_checkout).click()

    ######### Product Display #############

    def msgName(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_name).text
        except:
            None

    def msgBrand(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_brand).text
        except:
            None

    def msgProdCod(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_prodcod).text
        except:
            None
