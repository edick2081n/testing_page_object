from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USER_NAME = (By.CSS_SELECTOR, "#id_login-username")
    lOGIN_USER_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_NAME = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")




