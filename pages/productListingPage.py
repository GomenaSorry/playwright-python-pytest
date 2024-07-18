from playwright.sync_api import Page

class ProductListingPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_name_header = page.get_by_role("heading", name="Products")
        self.product_list = page.get_by_role("list")
        self.product_1_item_link = page.get_by_role("link", name="Product 1")
        self.product_1_item_add_to_cart_link = page.locator("//a[.='Product 1']//following-sibling::a")
        self.product_2_item_link = page.get_by_role("link", name="Product 2")
        self.product_2_item_add_to_cart_link = page.locator("//a[.='Product 2']//following-sibling::a")
        self.view_cart_button = page.get_by_role("link", name="View Cart")

    def click_view_cart_button(self):
        self.view_cart_button.click()

    def click_product_1_item_link(self):
        self.product_1_item_link.click()
    
    def click_product_1_item_add_to_cart_link(self):
        self.product_1_item_add_to_cart_link.click()

    def click_product_2_item_link(self):
        self.product_2_item_link.click()
    
    def click_product_2_item_add_to_cart_link(self):
        self.product_2_item_add_to_cart_link.click()