from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alertinner strong")
    BUSCET_MINI = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "h1")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")