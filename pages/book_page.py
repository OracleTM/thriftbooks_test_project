import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base
from utilities.logger import Logger


class BookPage(Base):

    # Locators

    book_title = "//h1[@class='WorkMeta-title Alternative Alternative-title']"
    add_cart_button = "//button[contains(text(), 'Add to Cart')]"
    continue_shopping_button = "//button[contains(text(), 'Continue Shopping')]"
    cart_button = "//div[@id='GlobalCartContainer']"
    book_price = "//span[@class='price']"



    # Getters

    def get_book_title_text(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_title)))
        return element.text

    def get_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button)))

    def get_continue_shopping_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_book_price_text(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_price)))
        return element.text

    # Actions

    def click_add_cart_button(self):
        self.get_add_cart_button().click()
        print("Add book in cart")

    def click_continue_shopping_button(self):
        self.get_continue_shopping_button().click()
        print("Click continue shopping button")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    def compare_titles(self):
        actual_title = self.get_book_title_text()
        expected_title = self.get_data('Attack on Titan, Vol. 1')
        self.assert_title(expected_title, actual_title)



    # Methods

    """Adding a selected book to the shopping cart"""
    def add_cart_book(self):
        with allure.step("Adding a selected book to the shopping cart"):
            Logger.add_start_step(method="add_cart_book")
            self.get_current_url()
            self.compare_titles()
            self.save_text('book_page_title', self.get_book_title_text())
            self.save_text('book_page_price', self.get_book_price_text())
            self.click_add_cart_button()
            self.click_continue_shopping_button()
            self.click_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="add_cart_book")
