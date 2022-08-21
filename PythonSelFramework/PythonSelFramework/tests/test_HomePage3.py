
from faker.providers import DynamicProvider

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from faker import Faker


class TestHomePage3(BaseClass):

    def test_formSubmission_failed2(self):
        gender_value = DynamicProvider(
            provider_name="gender_provider",
            elements=["Male", "Female"],
        )

        fake = Faker()
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(fake.name())
        homepage.getEmail().send_keys("")
        homepage.getPassword().send_keys(fake.sentence(ext_word_list=HomePageData.my_word_list))
        homepage.getCheckBox().click()
        fake.add_provider(gender_value)
        self.selectOptionByText(homepage.getGender(), fake.gender_provider())

        homepage.submitForm().click()

        alertText = homepage.getAlertEmail().text

        assert ("Email is required" in alertText)
        self.driver.refresh()
