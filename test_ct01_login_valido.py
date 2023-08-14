import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

#Caso de Teste 1: Realizar login valindo na aplicação


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT01:
    def test_ct01_login_valido(self):
       
       # Instaciar os objetos a serem utilizados no teste
        login_page = LoginPage()
        home_page = HomePage()
        
       # Realizar login e senha 
        login_page.fazer_login('standard_user', 'secret_sauce')
        
    # Verificar se o login foi realziado com sucesso
        home_page.verificar_login_com_sucesso()
      
        
       
        
        
        


        #text
        #product_title = driver.find_element(By.XPATH, "//span[@class='title']")
        #print("Irá exibir o título produtos:")
        #print(product_title.text)

        #assert product_title.text == "Products"


   
   