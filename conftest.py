import pytest
from selene import browser
@pytest.fixture()
def settings():
    browser.config.window_height = 1200
    browser.config.window_width = 720
