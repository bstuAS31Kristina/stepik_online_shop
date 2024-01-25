from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        login_word = "login"
        assert login_word in current_url, "Url doesn't contain login page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"

    def register_new_user(self, password, email):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        confirm_pass_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_INPUT)
        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_pass_input.send_keys(password)
        enter_button = self.browser.find_element(*LoginPageLocators.ENTER_BUTTON)
        enter_button.click()
