import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base
from utilities.logger import Logger


class AttackOnTitanPage(Base):

    # Locators

    attack_on_titan_vol_1 = "//h2[contains(text(), 'Attack on Titan, Vol. 1')]"

    # Getters

    def get_attack_on_titan_vol_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attack_on_titan_vol_1)))


    # Actions


    def click_attack_on_titan_vol_1(self):
        self.get_attack_on_titan_vol_1().click()
        print("Click Attack on Titan, Vol. 1")


    # Methods

    """Choosing the first book Attack of the Titans"""
    def choosing_the_first_book_attack_on_titans(self):
        with allure.step("Choosing the first book Attack of the Titans"):
            Logger.add_start_step(method="choosing_the_first_book_attack_on_titans")
            self.get_current_url()
            self.save_text('Attack on Titan, Vol. 1', self.get_attack_on_titan_vol_1().text)
            self.click_attack_on_titan_vol_1()
            Logger.add_end_step(url=self.driver.current_url, method="choosing_the_first_book_attack_on_titans")
