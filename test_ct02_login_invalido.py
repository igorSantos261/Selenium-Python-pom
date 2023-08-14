import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


#Caso de Teste 1: Realizar login valindo na aplicação


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.logininvalido
class TestCT02:
    def test_ct02_login_invalido(self):
        mensagem_erro_esperado = "Epic sadface: Username and password do not match any user in this service"
        
     # Instaciar os objetos a serem utilizados no teste
        login_page = LoginPage()
       
        
       # Inserir login e senha  invalido
        login_page.fazer_login('standard_user', 'testeinvalido')
        
       # Verificar mensagem de erro para login invalido
        login_page.verificar_mensagem_erro_login_existe()
        
    # Verificar mensagem de erro para ao realizar login invalido
    # mensagem - "Epic sadface: Username and password do not match any user in this service"
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperado)

        
       