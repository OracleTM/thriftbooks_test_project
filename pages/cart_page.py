
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base

class CartPage(Base):

    # Locators

    checkout_button = "//div[@id='divCartYourOrder']//a[contains(@class, 'ShoppingCart-proceedButton')][1]"
    books_title = "//a[@class='ShoppingCartItem-title']"
    books_price = "//span[@class='ShoppingCartItem-price ShoppingCartItem-priceEach']"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_books_title(self, number):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"({self.books_title})[{number}]")))

    def get_books_price(self, number):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"({self.books_price})[{number}]")))

    # Actions

    def compare_titles_and_price(self):
        try:
            a = 1
            expected_title = self.get_data('book_page_title')
            expected_price = self.get_data('book_page_price')
            while True:
                actual_title = self.get_books_title(a).text
                actual_price = self.get_books_price(a).text
                if actual_title == expected_title and actual_price.replace("$", "") == expected_price:
                    print(f"Title {expected_title} assert {actual_title} true")
                    print(f"Price ${expected_price} assert {actual_price} true")
                    break
                else:
                    a += 1
        except TimeoutException:
            print("Elements not found")


    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods

    def checkout_book_click(self):
        self.get_current_url()
        self.compare_titles_and_price()
        self.click_checkout_button()
