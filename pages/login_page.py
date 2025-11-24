from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Selectores encapsulados aquí
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    
    # --- NUEVO: Selector para el mensaje de error ---
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']") 

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, user, password):
        self.type(self.USERNAME_INPUT, user)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    # --- NUEVO: Método para obtener el texto del error ---
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)