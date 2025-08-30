RU

Для запуска теста вам понадобится: Python 3.9+, pip, pytest, webdriver_manager, selenium
Чтобы запустить тест: в терминале перейдите в директорию проекта, запустите тест: python -m pytest -s -v

Проект был создан в ходе обучения, тестирования сайта - https://www.thriftbooks.com/
Пройден весь бизнес путь до оплаты.
Каждый шаг выводится в консоль, присутствует сверка по названию книги, ее цены, итоговой цены с доставкой, финальным заголовком страницы, url и скриншотом.
Присутствует Faker для заполнения данных для доставки (выбран штат Colorado) 

EN

To run the test, you will need: Python 3.9+, pip, pytest, webdriver_manager, selenium.
To start the test: in the terminal, navigate to the project directory and run the test: python -m pytest -s -v.

The project was created during training, testing the website - https://www.thriftbooks.com/.
The entire business process up to payment has been completed.
Each step is logged to the console, including verification of the book title, its price, the total price with shipping, the final page title, and a screenshot.
The Faker library is used to populate shipping data (Colorado state selected).
