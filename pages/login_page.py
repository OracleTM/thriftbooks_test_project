from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


from base.base_class import Base

class LoginPage(Base):

    url = 'https://www.thriftbooks.com/account/login/'

    # Locators

    email = "//input[@id='ExistingAccount_EmailAddress']"
    password = "//input[@id='ExistingAccount_Password']"
    login_button = "//input[@class='Button']"
    assert_text = "//span[@class='SuperMenuItem-link']"

    # Getters

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    # Actions

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Clock login button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.driver.maximize_window()
        self.input_email("coffeepersonal@somoj.com")
        self.input_password("12345Test")
        self.click_login_button()
