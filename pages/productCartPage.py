from playwright.sync_api import Page

class ProductCartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_name_header = page.get_by_role("heading", name="Cart")
        self.back_to_product_listing_link = page.get_by_role("link", name="Back to Product Listing")

    def click_back_to_product_listing_link(self):
        self.back_to_product_listing_link.click()