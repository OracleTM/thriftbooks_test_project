RU

Для запуска теста вам понадобится: Python 3.9+, pip, pytest, webdriver_manager, selenium, Allure.

Чтобы запустить тест: в терминале перейдите в директорию проекта, запустите тест:
python -m pytest --alluredir=test_results/ tests/test_buy_product.py

Все логи теста хранятся в папке logs

Для проверки теста в Allure: Откройте терминал, перейдите в директорию проекта, пропишите:
allure serve test_reslults/

Проект был создан в ходе обучения, тестирования сайта - https://www.thriftbooks.com/
Пройден весь бизнес путь до оплаты.
Каждый шаг выводится в консоль, присутствует сверка по названию книги, ее цены, итоговой цены с доставкой, финальным заголовком страницы, url и скриншотом.
Присутствует Faker для заполнения данных для доставки (выбран штат Colorado) 

EN

To run the test, you will need: Python 3.9+, pip, pytest, webdriver_manager, selenium, Allure.

All test logs are stored in the logs folder.

To start the test: in the terminal, navigate to the project directory and run the test:
python -m pytest --alluredir=test_results/ tests/test_buy_product.py.

To view the test results in Allure: Open the terminal, navigate to the project directory, and run:
allure serve test_results/

The project was created during training, testing the website - https://www.thriftbooks.com/.
The entire business process up to payment has been completed.
Each step is logged to the console, including verification of the book title, its price, the total price with shipping, the final page title, and a screenshot.
The Faker library is used to populate shipping data (Colorado state selected).
