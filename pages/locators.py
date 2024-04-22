from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_FORM = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS_CONFIRM_FORM = (By.CSS_SELECTOR, "#id_registration-password2")

