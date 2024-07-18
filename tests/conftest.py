import pytest
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage
from pages.productPage import ProductPage
from pages.productCartPage import ProductCartPage
from playwright.sync_api import Page
import random
import string
import allure

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def product_listing_page(page: Page) -> ProductListingPage:
    return ProductListingPage(page)

@pytest.fixture
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)

@pytest.fixture
def product_cart_page(page: Page) -> ProductCartPage:
    return ProductCartPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            xfail = hasattr(report, "wasxfail")
            if report.failed or xfail and "page" in item.funcargs:
                page = item.funcargs["page"]
                
                def generate_random_screenshot_name(name):
                    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                    return f"{name}_{random_string}.png"
                
                screen_file = generate_random_screenshot_name(item.name)
                page.screenshot(path=screen_file)
                allure.attach(
                        page.screenshot(path=screen_file),  # Call screenshot method on the instance
                        name=str(item.name),
                        attachment_type=allure.attachment_type.PNG
                )
            else:
                print("FAILED SCREENSHOT")
        except Exception as e:
            print('Failed to take a screenshot: {}'.format(e))