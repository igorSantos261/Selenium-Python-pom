import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, 'user-name')
        self.passaword_field = (By.ID, 'password')
        self.loginbutton = (By.ID, "login-button")
        self.erro_messege_login = (By.XPATH, "//*[@data-test='error']")
    
    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.passaword_field, senha)
        self.clicar(self.loginbutton)
        
        
    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.erro_messege_login)
        
    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        
        texto_encontrado = self.pegar_texto_elemento(self.erro_messege_login)
        assert texto_encontrado == texto_esperado , f"O texto retornado foi '{texto_encontrado}', mas o texto esperado era '{texto_encontrado}'." 