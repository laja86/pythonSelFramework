from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    tb_country = (By.CSS_SELECTOR, "#country")
    suggestions = (By.LINK_TEXT, "Armenia")
    chk_AgreeWith = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    btn_purchase = (By.CSS_SELECTOR, "input[type='submit']")
    txa_alertsucess = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.tb_country)

    def getSuggestions(self):
        return self.driver.find_element(*ConfirmPage.suggestions)

    def getCheckboxAgreeWith(self):
        return self.driver.find_element(*ConfirmPage.chk_AgreeWith)

    def getpurchasebutton(self):
        return self.driver.find_element(*ConfirmPage.btn_purchase)

    def get_txa_alertsucess(self):
        return self.driver.find_element(*ConfirmPage.txa_alertsucess)
