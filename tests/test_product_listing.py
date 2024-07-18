import allure
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage

@allure.epic("Product Demo")
@allure.feature("Product Listing")
@allure.story("Product Listing Customer Experience")
def test_product_list_is_visible(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_list).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Product Listing")
@allure.story("Product Listing Customer Experience")
def test_product_list_is_not_empty(
        page: Page, 
        login_page: LoginPage ) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(page.get_by_role("listitem")).not_to_have_count(0)

@allure.epic("Product Demo")
@allure.feature("Product Listing")
@allure.story("Product Listing Customer Experience")
def test_product_list_item_links_are_visible(
        page: Page, 
        login_page: LoginPage,
        product_listing_page: ProductListingPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_1_item_link).to_be_visible()
    expect(product_listing_page.product_1_item_add_to_cart_link).to_be_visible()
    expect(product_listing_page.product_2_item_link).to_be_visible()
    expect(product_listing_page.product_2_item_add_to_cart_link).to_be_visible()