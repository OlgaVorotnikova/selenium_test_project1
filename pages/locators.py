from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    MESSAGE_SUCCESS_PRODUCT = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    MESSAGE_SUCCESS_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")