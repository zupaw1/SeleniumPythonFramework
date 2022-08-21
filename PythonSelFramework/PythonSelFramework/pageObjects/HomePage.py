from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    email_alert = (By.XPATH,"//div[@class='alert alert-danger']")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    date = (By.XPATH, "//input[@name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    failerMessage = (By.XPATH, "//div[normalize-space()='Name should be at least 2 characters']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getDate(self):
        return self.driver.find_element(*HomePage.date)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def getAlertEmail(self):
        return self.driver.find_element(*HomePage.email_alert)

    def getFailerMessage(self):
        return self.driver.find_element(*HomePage.failerMessage)
