import pytest
from pages.login_page import LoginPage
from pages.interest_calculator_page import InterestCalculatorPage
from settings import USERNAME, PASSWORD


def test_login_button_works(driver):
    login = LoginPage(driver)
    login.click_login()

    assert login.wait_for(login.LOGIN_BUTTON_2) is not None

def test_login(driver):
    login = LoginPage(driver)
    login.click_login()
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login_button()
    calc_page = InterestCalculatorPage(driver)
    heading = calc_page.wait_for(calc_page.HEADING)

    assert heading.text.strip() == "Interest Calculator"

@pytest.mark.parametrize("rate", range(1, 15))
def test_dropdown_menu_option_present(driver, rate):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    dropdown = InterestCalculatorPage(driver)
    dropdown.click_dropdown_menu()

    locator = getattr(dropdown, f"DROPDOWN_{rate}")
    assert dropdown.is_visible(locator), f"{rate}% does not exist"

@pytest.mark.parametrize("rate", range(1, 15))
def test_dropdown_rate_click(driver, rate):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    dropdown = InterestCalculatorPage(driver)

    getattr(dropdown, f"select_dropdown_amount_{rate}")()

    assert dropdown.check_dropdown_text() == f"Selected Rate: {rate}% does not exist"

def test_daily_interest_button(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    daily_interest = InterestCalculatorPage(driver)

    daily_interest.calculate_daily_interest()

    interest_amount = daily_interest.wait_for(daily_interest.INTEREST_AMOUNT)
    assert "Interest Amount" in interest_amount.text

    total_amount = daily_interest.wait_for(daily_interest.TOTAL_AMOUNT)
    assert "Total Amount with Interest" in total_amount.text

def test_monthly_interest_button(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    monthly_interest = InterestCalculatorPage(driver)

    monthly_interest.calculate_monthly_interest()

    interest_amount = monthly_interest.wait_for(monthly_interest.INTEREST_AMOUNT)
    assert "Interest Amount" in interest_amount.text

    total_amount = monthly_interest.wait_for(monthly_interest.TOTAL_AMOUNT)
    assert "Total Amount with Interest" in total_amount.text

def test_yearly_interest_button(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    yearly_interest = InterestCalculatorPage(driver)

    yearly_interest.calculate_yearly_interest()

    interest_amount = yearly_interest.wait_for(yearly_interest.INTEREST_AMOUNT)
    assert "Interest Amount" in interest_amount.text

    total_amount = yearly_interest.wait_for(yearly_interest.TOTAL_AMOUNT)
    assert "Total Amount with Interest" in total_amount.text
    
def test_daily_interest_calculation(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    daily_interest = InterestCalculatorPage(driver)

    daily_interest.calculate_daily_interest()
    daily_interest.validate_daily_interest()

def test_monthly_interest_calculation(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    monthly_interest = InterestCalculatorPage(driver)

    monthly_interest.calculate_monthly_interest()
    monthly_interest.validate_monthly_interest()

def test_yearly_interest_calculation(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    yearly_interest = InterestCalculatorPage(driver)

    yearly_interest.calculate_yearly_interest()
    yearly_interest.validate_yearly_interest()

def test_consent_button_positive(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    consent_button = InterestCalculatorPage(driver)

    consent_button.select_dropdown_amount_10()
    consent_button.find(consent_button.CONSENT_BOX).click()
    consent_button.find(consent_button.CALCULATE_BUTTON).click()

    interest_amount = consent_button.wait_for(consent_button.INTEREST_AMOUNT)
    assert "Interest Amount" in interest_amount.text

    total_amount = consent_button.wait_for(consent_button.TOTAL_AMOUNT)
    assert "Total Amount with Interest" in total_amount.text

def test_consent_button_negative(driver):
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)
    consent_button = InterestCalculatorPage(driver)

    consent_button.select_dropdown_amount_10()
    consent_button.find(consent_button.CALCULATE_BUTTON).click()

    # Check element existence instead of its text
    interest_elems = consent_button.finds(consent_button.INTEREST_AMOUNT)
    total_elems = consent_button.finds(consent_button.TOTAL_AMOUNT)
    if interest_elems or total_elems:
        pytest.fail(
            f"Interest should not be calculated without consent."
        )
