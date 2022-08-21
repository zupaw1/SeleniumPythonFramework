import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    @pytest.mark.xfail
    def test_e2e_2(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "iphone X":
                checkOutPage.getCardFooter()[i].click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkOutPage.getCheckOutButton()
        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering the country name")
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirmPage.getCountry().send_keys("ita")
        # Explicit wait
        self.verifyLinkPresence("Italy")
        # self.driver.find_element_by_link_text("India").click()
        confirmPage.getCountryText2()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirmPage.getCheckBox()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmPage.getSubmit()
        # successText = self.driver.find_element_by_class_name("alert-success").text
        textMatch = confirmPage.getSuccess().text
        log.info("Text received from the application is:" + textMatch)
        assert "Success! Thank you!" in textMatch
        self.driver.get_screenshot_as_file("screen.png")
