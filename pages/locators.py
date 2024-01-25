from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    CONFIRM_PASS_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    ENTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alertinner strong")
    BUSCET_MINI = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_BUTTON = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_PRODUCT = (By.CSS_SELECTOR, "form.basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "p a")
