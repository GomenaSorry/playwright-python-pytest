import allure
import pytest
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage
from pages.productPage import ProductPage

PRODUCTS = [
    '1',
    '2',
]

@allure.epic("Product Demo")
@allure.feature("Product Details")
@allure.story("Product Details Customer Experience")
@pytest.mark.parametrize('phrase', PRODUCTS)
def test_product_url_is_correct(
        phrase: str,
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage) -> None:
    login_page.navigate_to_login_page()
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.page.get_by_role("link", name=f"Product {phrase}").click()
    url = page.url
    assert f"/product_details/{phrase}" in url

@allure.epic("Product Demo")
@allure.feature("Product Details")
@allure.story("Product Details Customer Experience")
@pytest.mark.parametrize('phrase', PRODUCTS)
def test_product_name_header_is_correct(
        phrase: str,
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage) -> None:
    login_page.navigate_to_login_page()
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.page.get_by_role("link", name=f"Product {phrase}").click()
    expect(product_page.product_name_header).to_have_text(f"Product {phrase}")

@allure.epic("Product Demo")
@allure.feature("Product Details")
@allure.story("Product Details Customer Experience")
@pytest.mark.parametrize('phrase', PRODUCTS)
def test_product_name_description_is_correct(
        phrase: str,
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage) -> None:
    login_page.navigate_to_login_page()
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.page.get_by_role("link", name=f"Product {phrase}").click()
    expect(product_page.product_description_paragraph).to_have_text(f"This is product {phrase}.")