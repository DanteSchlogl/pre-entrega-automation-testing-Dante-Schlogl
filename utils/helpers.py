from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import time

url = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    
    driver.implicitly_wait(3)
    return driver


def login_saucedemo( driver ):
    driver.get(url)
    
    driver.find_element(By.NAME,'user-name').send_keys(USERNAME)
    driver.save_screenshot("ingresarUsuario.png")

    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    driver.save_screenshot("ingresarPass.png")
    
    driver.find_element(By.ID,'login-button').click()
    
    




