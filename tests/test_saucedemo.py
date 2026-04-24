import pytest
from playwright.sync_api import expect

# ---------------------------
# LOGIN TESTY
# ---------------------------

def test_login_success(login):
    """
    Uživatel se přihlásí pomocí platných údajů
    a je přesměrován na inventory stránku.
    """
    page = login()

    expect(page).to_have_url("/inventory.html")


def test_login_fail(login):
    """
    Systém odmítne přihlášení při zadání neplatných údajů
    a zobrazí chybovou hlášku.
    """
    page = login("wrong_user", "wrong_password")

    error = page.locator('[data-test="error"]')

    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password")


# ---------------------------
# INVENTORY TEST
# ---------------------------

def test_inventory_loaded(logged_in_page):
    """
    Po úspěšném přihlášení se zobrazí seznam dostupných produktů.
    """
    items = logged_in_page.locator('.inventory_item')
    
    # fixní počet produktů (saucedemo)
    expect(items).to_have_count(6)
    
    # variabilní počet produktů (jiné aplikace)
    # expect(items.first).to_be_visible()


# ---------------------------
# KOŠÍK TESTY
# ---------------------------

def test_add_to_cart(logged_in_page):
    """
    Produkt lze přidat do košíku
    a počet položek se aktualizuje v badge.
    """
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

    badge = logged_in_page.locator('.shopping_cart_badge')

    expect(badge).to_have_text("1")


def test_remove_from_cart(logged_in_page):
    """
    Produkt lze odebrat z košíku
    a indikátor počtu položek zmizí.
    """
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    
    logged_in_page.click('[data-test="remove-sauce-labs-backpack"]')

    badge = logged_in_page.locator('.shopping_cart_badge')

    expect(badge).not_to_be_visible()
    
    # pokud badge zůstává, měl by být prázdný
    # expect(badge).to_have_count(0)


def test_cart_contains_item(logged_in_page):
    """
    Košík zobrazuje přidaný produkt správně.
    """
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    logged_in_page.click('.shopping_cart_link')

    item = logged_in_page.locator('.inventory_item_name')

    expect(item).to_have_text("Sauce Labs Backpack")


# ---------------------------
# PARAMETRIZOVANÝ TEST
# ---------------------------

@pytest.mark.parametrize("product_id", [
    "sauce-labs-backpack",
    "sauce-labs-bike-light",
    "sauce-labs-bolt-t-shirt"
])
def test_add_multiple_products_to_cart(logged_in_page, product_id):
    """
    Ověření, že různé produkty lze přidat do košíku.
    """
    logged_in_page.click(f'[data-test="add-to-cart-{product_id}"]')

    badge = logged_in_page.locator('.shopping_cart_badge')

    expect(badge).to_be_visible()


# ---------------------------
# LOGOUT TEST
# ---------------------------

def test_logout(logged_in_page):
    """
    Uživatel se odhlásí pomocí menu a je vrácen na přihlašovací stránku.
    """
    logged_in_page.click('#react-burger-menu-btn')

    logout_button = logged_in_page.locator('#logout_sidebar_link')
    expect(logout_button).to_be_visible()

    logout_button.click()

    expect(logged_in_page).to_have_url("/")
