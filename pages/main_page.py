import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    # Locators

    books_filter = "//a[@aria-label='Books']"
    manga_categories = "//a[@aria-label='Manga']"

    # Getters
    def get_books_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.books_filter)))

    def get_manga_categories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manga_categories)))


    # Actions

    def hover_books_filter(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_books_filter()).perform()
        print("Click books filter")

    def click_manga_categories(self):
        self.get_manga_categories().click()
        print("Click manga categories")



    # Methods

    """Selecting manga in the filter"""
    def select_manga(self):
        with allure.step("Selecting manga in the filter"):
            Logger.add_start_step(method="select_manga")
            self.get_current_url()
            self.hover_books_filter()
            self.click_manga_categories()
            Logger.add_end_step(url=self.driver.current_url, method="select_manga")
