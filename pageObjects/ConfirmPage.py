from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class ConfirmPage(BasePage):

    tb_country = (By.CSS_SELECTOR, "#country")
    list_suggestions = (By.CSS_SELECTOR, ".suggestions a")
    chk_AgreeWith = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    btn_purchase = (By.CSS_SELECTOR, "input[type='submit']")
    txa_alertsucess = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.tb_country)

    def get_Suggestions(self):
        return self.driver.find_elements(*ConfirmPage.list_suggestions) # cambiar todos a self

    def getCheckboxAgreeWith(self):
        return self.driver.find_element(*ConfirmPage.chk_AgreeWith)

    def getpurchasebutton(self):
        return self.driver.find_element(*ConfirmPage.btn_purchase)

    def get_txa_alertsucess(self):
        return self.driver.find_element(*ConfirmPage.txa_alertsucess)
