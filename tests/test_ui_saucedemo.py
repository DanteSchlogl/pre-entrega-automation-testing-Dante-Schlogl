import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_test_data

# 1. Cargo los datos del JSON al iniciar el script
data = load_test_data()

def test_catalogo_carga_correcta(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    
    # 2. Uso los datos cargados (usuario válido)
    user = data['valid_user']['username']
    password = data['valid_user']['password']
    
    login_page.login(user, password)
    
    cantidad = inventory_page.get_count_products()
    assert cantidad > 0, "El catálogo no cargó productos"

def test_agregar_3_items_al_carrito(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    
    # Uso los datos cargados
    user = data['valid_user']['username']
    password = data['valid_user']['password']
    
    login_page.login(user, password)
    
    # Acción del Page Object
    inventory_page.add_first_n_products(3)
    
    # Validación
    badge_count = inventory_page.get_cart_badge_text()
    assert badge_count == "3", f"Se esperaban 3 items, pero se encontraron {badge_count}"

# 3. Agrego el Test Negativo (Esto es Obligatorio en la consigna)
def test_login_fallido_credenciales_invalidas(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    # Usamos el usuario INVÁLIDO del JSON
    user = data['invalid_user']['username']
    password = data['invalid_user']['password']
    
    login_page.login(user, password)
    
    # Verificoo el mensaje de error
    error_text = login_page.get_error_message()
    assert "Epic sadface" in error_text, "No apareció el mensaje de error esperado"