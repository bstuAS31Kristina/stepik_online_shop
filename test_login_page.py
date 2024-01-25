from .pages.login_page import LoginPage


def test_guest_should_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

