from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Selectores
    INVENTORY_ITEMS = (By.CLASS_NAME, 'inventory_item')
    ADD_TO_CART_BTN = (By.TAG_NAME, 'button')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')

    def get_count_products(self):
        # Retorna cantidad de productos en pantalla
        items = self.find_all(self.INVENTORY_ITEMS)
        return len(items)

    def add_first_n_products(self, quantity):
        #  Lógica de agregar 3 items, encapsulada
        items = self.find_all(self.INVENTORY_ITEMS)
        for i in range(quantity):
            if i < len(items):
                items[i].find_element(*self.ADD_TO_CART_BTN).click()

    def get_cart_badge_text(self):
        return self.get_text(self.CART_BADGE)