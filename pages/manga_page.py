
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base

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

    def actions_manga_page(self):
        self.get_current_url()
        self.click_attack_on_titan()
