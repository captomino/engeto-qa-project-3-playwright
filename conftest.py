import pytest

@pytest.fixture
def login(page):
    def _login(username="standard_user", password="secret_sauce"):
        page.goto("/")

        page.fill('[data-test="username"]', username)
        page.fill('[data-test="password"]', password)
        page.click('[data-test="login-button"]')

        return page

    return _login

@pytest.fixture
def open_page(page):
    page.goto("/")
    return page

@pytest.fixture
def logged_in_page(login):
    return login()