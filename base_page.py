import conftest



class BasePage:
    
    def __init__(self):
        self.driver = conftest.driver
        
    def localizar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def localizar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.localizar_elemento(locator).send_keys(text)
        
    def clicar(self, locator):
        self.localizar_elemento(locator).click()
        
    def verificar_se_elemento_existe(self, locator):
        self.localizar_elemento(locator).is_displayed, f"O Elemento '{locator}' não foi exibido na tela."
        
    def pegar_texto_elemento(self, locator):
        return self.localizar_elemento(locator).text
        