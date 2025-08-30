from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.attack_on_titan_page import AttackOnTitanPage
from pages.book_page import BookPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.manga_page import MangaPage
from pages.payment_page import PaymentPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.page_load_strategy = 'normal' #eager
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


    print('\nStart Test')

    login = LoginPage(driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.actions_main_page()

    manga_page = MangaPage(driver)
    manga_page.actions_manga_page()

    attack_on_titan_page = AttackOnTitanPage(driver)
    attack_on_titan_page.actions_attack_on_titan_page()

    book_page = BookPage(driver)
    book_page.add_cart_book()

    cart_page = CartPage(driver)
    cart_page.checkout_book_click()

    checkout = CheckoutPage(driver)
    checkout.checkout_actions()

    payment = PaymentPage(driver)
    payment.payment_finish_actions()
