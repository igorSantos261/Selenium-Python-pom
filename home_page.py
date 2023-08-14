import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        
    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)
    