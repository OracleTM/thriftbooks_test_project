from datetime import datetime, timezone
from pathlib import Path

class Base():
    shared_data = {}

    def __init__(self, driver):
        self.driver = driver


    def save_data(self, key, value):
        """Save text"""
        self.shared_data[key] = value


    def get_data(self, key):
        """Get text"""
        return self.shared_data.get(key)


    def save_text(self, key, value):
        """Save text"""
        self.save_data(key,value)
        print(f"Saved text: {value}")

    def get_current_url(self):
        """Current URL"""
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    def assert_word(self, word, result):
        """Method assert text"""
        value_word = word.text
        assert value_word == result
        print("Good value text")

    def assert_title(self, expected, actual):
        expected = expected.translate(str.maketrans("", "", ".:-& and,Vol"))
        actual = actual.translate(str.maketrans("", "", ".:-& and,Vol"))
        assert expected in actual, f"Titles assert false"
        print(f"Titles assert true")

    def get_screenshot(self):
        """Method Screenshots"""
        now_date = datetime.now(timezone.utc).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        base_path = Path(__file__).parent.parent / "screen"
        base_path.mkdir(parents=True, exist_ok=True)
        screenshot_path = base_path / name_screenshot
        self.driver.save_screenshot(screenshot_path)
        print("Save screenshot")

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
