import pytest
from selenium.webdriver.common.by import By
import conftest 


#Caso de Teste 2: Realizar inserção de dois produtos no carrinho.
'''
Passos:
1 - Realizar login na aplicação com usuário e senha validos;
2 - Escolher Primeiro produto e clicar no botão [Add to cart];
3 - Clicar no botão do carrinha e acessar tela "Your Cart";
4 - Retornar para tela inicial e inserir um novo produto ao carrinho;
5 - Retornar a tela "Your Cart", verificar se segundo produto foi inserido corretamente
'''


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        #Realizar login na aplicação com usuário e senha validos;"
        username = driver.find_element(By.ID, 'user-name')
        password = driver.find_element(By.ID, 'password')
        #Inserir login, senha e clicar no botão de logar
        username.send_keys('standard_user')
        password.send_keys('secret_sauce')
        driver.find_element(By.ID, "login-button").click()



        #Validar que foi acessado a pagina inicial
        product_title = driver.find_element(By.XPATH, "//span[@class='title']")
        print("Irá exibir o título da Tela inicial:")
        print(product_title.text)

        assert product_title.text == "Products"


        #Teste para inserir primeiro produto ao carrinho.
        driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[1]")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()



        #Irá procurar link que direciona a tela do carrinha e clicar no [botão].
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

        #Validar se o usuario esta na tela do CARRINHO.
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        your_cart = driver.find_element(By.XPATH, "//span[@class='title']")
        print("Irá exibir o título da Tela seu carrinho:")
        print(your_cart.text)

        assert your_cart.text == "Your Cart"

        #Script para retornar a tela inicial e inserir um novo produto
        driver.find_element(By.ID, "continue-shopping")
        driver.find_element(By.ID, "continue-shopping").click()


        #Nesta etapa irá inserir um segundo produto, e clicar no botão que direciona para tela de Carrinho
        driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[6]")
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()


        


