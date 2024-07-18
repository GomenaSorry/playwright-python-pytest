from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_name_header = page.get_by_role("heading")
        self.product_description_paragraph = page.get_by_role("paragraph").first
        self.view_cart_button = page.get_by_role("link", name="View Cart")
        self.add_to_cart_link = page.get_by_role("link", name="Add to Cart")

    def click_view_cart_button(self):
        self.view_cart_button.click()

    def click_add_to_cart_link(self):
        self.add_to_cart_link.click()