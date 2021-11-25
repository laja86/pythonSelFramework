from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class ConfirmPage(BasePage):

    tb_country = (By.CSS_SELECTOR, "#country")
    list_suggestions = (By.CSS_SELECTOR, ".suggestions a")
    chk_AgreeWith = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    btn_purchase = (By.CSS_SELECTOR, "input[type='submit']")
    txa_alertsucess = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getCountry(self):
        return self.driver.find_element(*self.tb_country)

    def get_Suggestions(self):
        return self.driver.find_elements(*self.list_suggestions) # uses * to deserialize the tuple

    def getCheckboxAgreeWith(self):
        return self.driver.find_element(*self.chk_AgreeWith)

    def getpurchasebutton(self):
        return self.driver.find_element(*self.btn_purchase)

    def get_txa_alertsucess(self):
        return self.driver.find_element(*self.txa_alertsucess)
