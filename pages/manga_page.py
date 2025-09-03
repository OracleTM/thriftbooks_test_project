import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base
from utilities.logger import Logger


class MangaPage(Base):

    # Locators

    attack_on_titan = "//a[contains(text(), 'Attack on Titan')]"

    # Getters

    def get_attack_on_titan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attack_on_titan)))


    # Actions


    def click_attack_on_titan(self):
        self.get_attack_on_titan().click()
        print("Click Attack on Titan")


    # Methods

    """Select Attack of the Titans in the filter"""
    def select_attack_on_titan_in_filter(self):
        with allure.step("Select Attack of the Titans in the filter"):
            Logger.add_start_step(method="select_attack_on_titan_in_filter")
            self.get_current_url()
            self.click_attack_on_titan()
            Logger.add_end_step(url=self.driver.current_url, method="select_attack_on_titan_in_filter")
