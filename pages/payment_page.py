import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base
from utilities.logger import Logger


class PaymentPage(Base):

    # Locators

    assert_text = "//h1[contains(text(), 'Payment Method')]"
    estimated_total = "//div[@class='OrderSummary-Total']/div[2]"

    # Getters

    def get_assert_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_text)))

    def get_estimated_total(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.estimated_total)))
        return element.text


    # Actions

    def assert_estimated_total(self):
        actual_estimated_total = self.get_estimated_total()
        expected_estimated_total = self.get_data('estimated_total_checkout')
        assert actual_estimated_total == expected_estimated_total, "assert false"
        print("Estimated total assert true")

    # Methods

    """Reconciliation of url, text, final price, screenshot on the final page"""
    def payment_finish_actions(self):
        with allure.step("Reconciliation of url, text, final price, screenshot on the final page"):
            Logger.add_start_step(method="payment_finish_actions")
            self.get_current_url()
            self.assert_url("https://www.thriftbooks.com/checkout/payment/")
            self.assert_word(self.get_assert_text(), "Payment Method")
            self.assert_estimated_total()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="payment_finish_actions")
