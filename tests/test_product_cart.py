import allure
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage
from pages.productCartPage import ProductCartPage
from pages.productPage import ProductPage

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_listing_page(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_list).to_be_visible()
    product_listing_page.click_product_1_item_add_to_cart_link()
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_listing_page_multiple_times(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_list).to_be_visible()
    for i in range(3):
        product_listing_page.click_product_1_item_add_to_cart_link()
        product_listing_page.click_view_cart_button()
        page.wait_for_url("**/view_cart")
        expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: {i + 1}")).to_be_visible()
        product_cart_page.click_back_to_product_listing_link()
        page.wait_for_url("**/product_listing")

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_different_products_from_product_listing_page(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_list).to_be_visible()
    product_listing_page.click_product_1_item_add_to_cart_link()
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    product_cart_page.click_back_to_product_listing_link()
    page.wait_for_url("**/product_listing")
    product_listing_page.click_product_2_item_add_to_cart_link()
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    expect(page.get_by_role("listitem").get_by_text("Product 2 - This is product 2. - Quantity: 1")).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_different_product_from_product_listing_page_multiple_times_from_a_non_empty_cart(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.product_list).to_be_visible()
    product_listing_page.click_product_1_item_add_to_cart_link()
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    product_cart_page.click_back_to_product_listing_link()
    page.wait_for_url("**/product_listing")
    for i in range(3):
        product_listing_page.click_product_2_item_add_to_cart_link()
        product_listing_page.click_view_cart_button()
        page.wait_for_url("**/view_cart")
        expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
        expect(page.get_by_role("listitem").get_by_text(f"Product 2 - This is product 2. - Quantity: {i + 1}")).to_be_visible()
        product_cart_page.click_back_to_product_listing_link()
        page.wait_for_url("**/product_listing")

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_page(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.click_product_1_item_link()
    page.wait_for_url("**/product_details/1")
    product_page.click_add_to_cart_link()
    page.wait_for_url("**/product_listing") 
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(product_cart_page.page_name_header).to_be_visible()
    expect(page.get_by_role("listitem").get_by_text("Product 1 - This is product 1. - Quantity: 1")).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_page(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    for i in range(6):
        product_listing_page.click_product_1_item_link()
        page.wait_for_url("**/product_details/1")
        product_page.click_add_to_cart_link()
        page.wait_for_url("**/product_listing") 
        product_listing_page.click_view_cart_button()
        page.wait_for_url("**/view_cart")
        expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: {i + 1}")).to_be_visible()
        product_cart_page.click_back_to_product_listing_link()

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_page_with_a_non_empty_cart(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.click_product_1_item_link()
    page.wait_for_url("**/product_details/1")
    product_page.click_add_to_cart_link()
    page.wait_for_url("**/product_listing") 
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    product_cart_page.click_back_to_product_listing_link()
    product_listing_page.click_product_2_item_link()
    page.wait_for_url("**/product_details/2")
    product_page.click_add_to_cart_link()
    page.wait_for_url("**/product_listing") 
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    expect(page.get_by_role("listitem").get_by_text(f"Product 2 - This is product 2. - Quantity: 1")).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Product Cart")
@allure.story("Product Cart Customer Experience")
def test_add_product_from_product_page_with_a_non_empty_cart(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage,
        product_page: ProductPage,
        product_cart_page: ProductCartPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.login("testuser", "password123")
    page.wait_for_url("**/product_listing")
    product_listing_page.click_product_1_item_link()
    page.wait_for_url("**/product_details/1")
    product_page.click_add_to_cart_link()
    page.wait_for_url("**/product_listing") 
    product_listing_page.click_view_cart_button()
    page.wait_for_url("**/view_cart")
    expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
    product_cart_page.click_back_to_product_listing_link()
    for i in range(6):
        product_listing_page.click_product_2_item_link()
        page.wait_for_url("**/product_details/2")
        product_page.click_add_to_cart_link()
        page.wait_for_url("**/product_listing") 
        product_listing_page.click_view_cart_button()
        page.wait_for_url("**/view_cart")
        expect(page.get_by_role("listitem").get_by_text(f"Product 1 - This is product 1. - Quantity: 1")).to_be_visible()
        expect(page.get_by_role("listitem").get_by_text(f"Product 2 - This is product 2. - Quantity: {i + 1}")).to_be_visible()
        product_cart_page.click_back_to_product_listing_link()