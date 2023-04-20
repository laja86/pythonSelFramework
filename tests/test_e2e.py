from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()  # it creates the HomePage at the method level in shopitems
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.firstCheckout().click()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as arm")
        confirmpage.getCountry().send_keys("ar")

        countryToFind = "Hungary"
        self.verifyLinkPresence(countryToFind)

        listsuggestions = confirmpage.get_Suggestions()

        j = -1
        for sug in listsuggestions:
            j = j + 1
            suggestion = sug.text
            log.info(suggestion)
            if suggestion == countryToFind:
                confirmpage.get_Suggestions()[j].click()
                break

        confirmpage.getCheckboxAgreeWith().click()

        confirmpage.getpurchasebutton().click()
        textMatch = confirmpage.get_txa_alertsucess().text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
