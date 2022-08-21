from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryText = (By.LINK_TEXT, "Poland")
    countryText2 = (By.LINK_TEXT, "Italy")
    countryText3 = (By.LINK_TEXT, "Ukraine")
    countryText4 = (By.LINK_TEXT, "Finland")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryText(self):
        return self.driver.find_element(*ConfirmPage.countryText).click()

    def getCountryText2(self):
        return self.driver.find_element(*ConfirmPage.countryText2).click()

    def getCountryText3(self):
        return self.driver.find_element(*ConfirmPage.countryText3).click()

    def getCountryText4(self):
        return self.driver.find_element(*ConfirmPage.countryText4).click()

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox).click()

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.submit).click()

    def getSuccess(self):
        return self.driver.find_element(*ConfirmPage.successText)
