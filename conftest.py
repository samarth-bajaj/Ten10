import pytest
from selenium import webdriver
from settings import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass
