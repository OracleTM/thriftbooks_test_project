
from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base

class CheckoutPage(Base):

    # Faker
    fake = Faker("en_US")

    faker_first_name = fake.first_name()
    faker_last_name = fake.last_name()
    faker_address = fake.street_address()
    faker_city = fake.city()
    faker_zip = fake.postcode()

    # Locators

    first_name = "//input[@id='firstName']"
    last_name = "//input[@id='lastName']"
    address = "//input[@id='addressLine1']"
    city = "//input[@id='city']"
    postal_zip = "//input[@id='postalCode']"
    state_colorado = "//select[@id='state']//option[@value='CO']"
    continue_payment = "//button[contains(text(), 'Continue to Payment')]"
    unverified_address_button = "//button[contains(text(), 'Use Unverified Address')]"
    new_shipping_address = "//div[@class='Shipping-NewAddressRadioCol']"
    estimated_total = "//div[@class='OrderSummary-Total']/div[2]"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_postal_zip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_zip)))

    def get_state_colorado(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.state_colorado)))

    def get_continue_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_payment)))

    def get_unverified_address_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.unverified_address_button)))

    def get_new_shipping_address(self):
            elements = self.driver.find_elements(By.XPATH, self.new_shipping_address)
            if not elements:
                return None
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_shipping_address)))

    def get_estimated_total(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.estimated_total)))
        return element.text


    # Actions

    def input_first_name(self, faker_first_name):
        self.get_first_name().send_keys(faker_first_name)
        print(f"Input first name {faker_first_name}")

    def input_last_name(self, faker_last_name):
        self.get_last_name().send_keys(faker_last_name)
        print(f"Input last name {faker_last_name}")

    def input_address(self, faker_address):
        self.get_address().send_keys(faker_address)
        print(f"Input address {faker_address}")

    def input_city(self, faker_city):
        self.get_city().send_keys(faker_city)
        print(f"Input city {faker_city}")

    def input_postal_zip(self, faker_zip):
        self.get_postal_zip().send_keys(faker_zip)
        print(f"Input zip {faker_zip}")

    def click_state_colorado(self):
        self.get_state_colorado().click()
        print("Click Colorado State")

    def click_continue_payment(self):
        self.get_continue_payment().click()
        print("Click Continue Payment Button")

    def click_unverified_address_button(self):
        self.get_unverified_address_button().click()
        print("Click Unverified Address Button")

    def click_new_shipping_address(self):
        self.get_new_shipping_address().click()
        print("Click new shipping address Button")

    # Methods

    def checkout_actions(self):
        self.get_current_url()
        def main_steps():
            self.input_first_name(self.faker_first_name)
            self.input_last_name(self.faker_last_name)
            self.input_address(self.faker_address)
            self.input_city(self.faker_city)
            self.input_postal_zip(self.faker_zip)
            self.click_state_colorado()
            self.click_continue_payment()
            self.click_unverified_address_button()
            self.save_text('estimated_total_checkout', self.get_estimated_total())
        try:
            if self.get_new_shipping_address():
                self.click_new_shipping_address()
                main_steps()
            else:
                main_steps()
        except TimeoutException:
            main_steps()
