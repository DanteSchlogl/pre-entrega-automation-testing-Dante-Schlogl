import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    # Aquí puedo modificar los headless si quiero
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# --- REQUERIMIENTO: Captura de pantalla automática al fallar ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
           
            screenshot_path = f"reports/screenshots/fail_{item.name}_{now}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot guardado: {screenshot_path}")