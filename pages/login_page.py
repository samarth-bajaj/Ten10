from selenium.webdriver.common.by import By

from .common import CommonOps

class LoginPage(CommonOps):
    LOGIN_BUTTON = (By.XPATH, "//div[1]/button[2]")
    USERNAME = (By.ID, "UserName")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON_2 = (By.ID, "login-submit")

    def click_login(self):
        self.wait_for(self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        if username is None:
            try:
                import settings
                username = username or getattr(settings, "USERNAME", None)
            except Exception:
                pass

        if not username:
            raise ValueError("Username not provided and settings.USERNAME not set")
        
        self.find(self.USERNAME).send_keys(username)

    def enter_password(self, password):
        if password is None:
            try:
                import settings
                password = password or getattr(settings, "PASSWORD", None)
            except Exception:
                pass

        if not password:
            raise ValueError("Password not provided and settings.PASSWORD not set")
        
        self.find(self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.LOGIN_BUTTON_2).click()

    def login(self, username: str | None = None, password: str | None = None):
        if username is None or password is None:
            try:
                import settings
                username = username or getattr(settings, "USERNAME", None)
                password = password or getattr(settings, "PASSWORD", None)
            except Exception:
                pass

        if not username or not password:
            raise ValueError("Username/password not provided and settings.USERNAME/PASSWORD not set")
        
        self.click_login()
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.click_login_button()
