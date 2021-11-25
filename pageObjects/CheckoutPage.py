from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage(BasePage):

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    firstCheckoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def firstCheckout(self):
        return self.driver.find_element(*CheckOutPage.firstCheckoutButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
