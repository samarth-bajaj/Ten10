import re
import math
import re
import math
from selenium.webdriver.common.by import By

from .common import CommonOps


class InterestCalculatorPage(CommonOps):

    HEADING = (By.XPATH, "//h1")
    PRINCIPAL_INPUT = (By.ID, "selectedValue")
    SLIDER = (By.XPATH, "//input[@type='range' and @id='customRange1']")
    SCREEN = (By.XPATH, "/html/body/div[1]/main/div/div[2]")
    DROPDOWN_MENU = (By.ID, "dropdownMenuButton")
    DROPDOWN_1 = (By.ID, "rate-1%")
    DROPDOWN_2 = (By.ID, "rate-2%")
    DROPDOWN_3 = (By.ID, "rate-3%")
    DROPDOWN_4 = (By.ID, "rate-4%")
    DROPDOWN_5 = (By.ID, "rate-5%")
    DROPDOWN_6 = (By.ID, "rate-6%")
    DROPDOWN_7 = (By.ID, "rate-7%")
    DROPDOWN_8 = (By.ID, "rate-8%")
    DROPDOWN_9 = (By.ID, "rate-9%")
    DROPDOWN_10 = (By.ID, "rate-10%")
    DROPDOWN_11 = (By.ID, "rate-11%")
    DROPDOWN_12 = (By.ID, "rate-12%")
    DROPDOWN_13 = (By.ID, "rate-13%")
    DROPDOWN_14 = (By.ID, "rate-14%")
    DROPDOWN_15 = (By.ID, "rate-15%")
    DURATION_DAILY = (By.XPATH, "//*[@id='durationList']/a[1]")
    DURATION_MONTHLY = (By.XPATH, "//*[@id='durationList']/a[2]")
    DURATION_YEARLY = (By.XPATH, "//*[@id='durationList']/a[3]")
    CONSENT_BOX = (By.ID, "gridCheck1")
    CALCULATE_BUTTON = (By.XPATH, "//div[5]//button")
    INTEREST_AMOUNT = (By.ID, "interestAmount")
    TOTAL_AMOUNT = (By.ID, "totalAmount")
    
    def click_dropdown_menu(self):
        self.find(self.DROPDOWN_MENU).click()

    def select_dropdown_amount_1(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_1).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_2(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_2).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_3(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_3).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_4(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_4).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_5(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_5).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_6(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_6).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_7(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_7).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_8(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_8).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_9(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_9).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_10(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_10).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_11(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_11).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_12(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_12).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_13(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_13).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_14(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_14).click()
        self.find(self.SCREEN).click()

    def select_dropdown_amount_15(self):
        self.find(self.DROPDOWN_MENU).click()
        self.find(self.DROPDOWN_15).click()
        self.find(self.SCREEN).click()

    def check_dropdown_text(self):
        button = self.wait_visible(self.DROPDOWN_MENU)
        return (button.text or "").strip()
    
    def calculate_daily_interest(self):
        self.select_dropdown_amount_9()
        self.find(self.DURATION_DAILY).click()
        self.find(self.CONSENT_BOX).click()
        self.find(self.CALCULATE_BUTTON).click()

    def calculate_monthly_interest(self):
        self.select_dropdown_amount_9()
        self.find(self.DURATION_MONTHLY).click()
        self.find(self.CONSENT_BOX).click()
        self.find(self.CALCULATE_BUTTON).click()

    def calculate_yearly_interest(self):
        self.select_dropdown_amount_9()
        self.find(self.DURATION_YEARLY).click()
        self.find(self.CONSENT_BOX).click()
        self.find(self.CALCULATE_BUTTON).click()

    def validate_daily_interest(self):
        # Read principal
        principal_elem = self.wait_visible(self.PRINCIPAL_INPUT)
        principal_raw = principal_elem.get_attribute("value") or principal_elem.text or "0"
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", principal_raw)
        if not m:
            raise AssertionError(f"Principal value not found in: {principal_raw!r}")
        principal = float(m.group(0).replace(",", ""))

        # Extract selected rate percent
        dropdown_label = self.wait_visible(self.DROPDOWN_MENU).text or ""
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", dropdown_label)
        if not m:
            raise AssertionError(f"Rate percent not found in dropdown text: {dropdown_label!r}")
        rate_percent = float(m.group(1))

        # Expected daily interest: annual rate / 365 days
        expected_daily_interest = round(principal * (rate_percent / 100.0) / 365.0, 2)

        # Read interest amount
        interest_text = (self.wait_visible(self.INTEREST_AMOUNT).text
                         or self.find(self.INTEREST_AMOUNT).get_attribute("value")
                         or "0")
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", interest_text)
        if not m:
            raise AssertionError(f"Interest amount not numeric: {interest_text!r}")
        actual_interest = round(float(m.group(0).replace(",", "")), 2)

        if actual_interest != expected_daily_interest:
            raise AssertionError(
                f"Daily interest mismatch: expected {expected_daily_interest:.2f}, "
                f"got {actual_interest:.2f} (principal={principal}, rate%={rate_percent})"
            )

    def validate_monthly_interest(self):
        # Read principal
        principal_elem = self.wait_visible(self.PRINCIPAL_INPUT)
        principal_raw = principal_elem.get_attribute("value") or principal_elem.text or "0"
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", principal_raw)
        if not m:
            raise AssertionError(f"Principal value not found in: {principal_raw!r}")
        principal = float(m.group(0).replace(",", ""))

        # Extract selected rate percent
        dropdown_label = self.wait_visible(self.DROPDOWN_MENU).text or ""
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", dropdown_label)
        if not m:
            raise AssertionError(f"Rate percent not found in dropdown text: {dropdown_label!r}")
        rate_percent = float(m.group(1))

        # Expected monthly interest: annual rate / 12
        expected_monthly_interest = round(principal * (rate_percent / 100.0) / 12.0, 2)

        # Read interest amount
        interest_text = (self.wait_visible(self.INTEREST_AMOUNT).text
                         or self.find(self.INTEREST_AMOUNT).get_attribute("value")
                         or "0")
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", interest_text)
        if not m:
            raise AssertionError(f"Interest amount not numeric: {interest_text!r}")
        actual_interest = float(m.group(0).replace(",", ""))

        actual_interest = round(float(m.group(0).replace(",", "")), 2)

        if actual_interest != expected_monthly_interest:
            raise AssertionError(
                f"Monthly interest mismatch: expected {expected_monthly_interest:.2f}, "
                f"got {actual_interest:.2f} (principal={principal}, rate%={rate_percent})"
            )

    def validate_yearly_interest(self):
        # Read principal
        principal_elem = self.wait_visible(self.PRINCIPAL_INPUT)
        principal_raw = principal_elem.get_attribute("value") or principal_elem.text or "0"
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", principal_raw)
        if not m:
            raise AssertionError(f"Principal value not found in: {principal_raw!r}")
        principal = float(m.group(0).replace(",", ""))

        # Extract selected rate percent
        dropdown_label = self.wait_visible(self.DROPDOWN_MENU).text or ""
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", dropdown_label)
        if not m:
            raise AssertionError(f"Rate percent not found in dropdown text: {dropdown_label!r}")
        rate_percent = float(m.group(1))

        # Expected yearly interest: principal * annual rate
        expected_yearly_interest = round(principal * (rate_percent / 100.0), 2)

        # Read interest amount
        interest_text = (self.wait_visible(self.INTEREST_AMOUNT).text
                         or self.find(self.INTEREST_AMOUNT).get_attribute("value")
                         or "0")
        m = re.search(r"-?\d[\d,]*(?:\.\d+)?", interest_text)
        if not m:
            raise AssertionError(f"Interest amount not numeric: {interest_text!r}")
        actual_interest = float(m.group(0).replace(",", ""))

        actual_interest = round(float(m.group(0).replace(",", "")), 2)

        if actual_interest != expected_yearly_interest:
            raise AssertionError(
                f"Yearly interest mismatch: expected {expected_yearly_interest:.2f}, "
                f"got {actual_interest:.2f} (principal={principal}, rate%={rate_percent})"
            )
