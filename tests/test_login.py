import allure
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage

@allure.epic("Product Demo")
@allure.feature("Login Page")
@allure.story("Customer Login")
def test_success_login(
        page: Page, 
        login_page: LoginPage, 
        product_listing_page: ProductListingPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login_button()
    page.wait_for_url("**/product_listing")
    expect(product_listing_page.page_name_header).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Login Page")
@allure.story("Customer Login")
def test_invalid_login_username(
        page: Page, 
        login_page: LoginPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.enter_username("invaliduser")
    login_page.enter_password("password123")
    login_page.click_login_button()
    expect(login_page.error_message).to_be_visible()

@allure.epic("Product Demo")
@allure.feature("Login Page")
@allure.story("Customer Login")
def test_invalid_login_password(
        page: Page, 
        login_page: LoginPage) -> None:
    page.goto("http://127.0.0.1:5000/")
    login_page.enter_username("testuser")
    login_page.enter_password("password124")
    login_page.click_login_button()
    expect(login_page.error_message).to_be_visible()

# @allure.epic("Product Demo")
# @allure.feature("Login Page")
# @allure.story("Customer Login")
# def test_expected_failure_screenshot_report_demo(
#         page: Page, 
#         login_page: LoginPage, 
#         product_listing_page: ProductListingPage) -> None:
#     page.goto("http://127.0.0.1:5000/")
#     login_page.enter_username("testuser")
#     login_page.enter_password("password124")
#     login_page.click_login_button()
#     page.wait_for_url("**/product_listing")
#     expect(product_listing_page.page_name_header).to_be_visible()