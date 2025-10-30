from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CommonOps:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)
        self._action = ActionChains(self.driver)

    # Waiting and element helpers
    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def wait_visible(self, locator, timeout: float = 10.0):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def is_visible(self, locator, timeout: float = 10.0) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    # Actions and alerts
    def context_click(self, element):
        return self._action.context_click(element)

    def alert(self):
        return self._wait.until(EC.alert_is_present())

    @property
    def title(self) -> str:
        return self.driver.title

