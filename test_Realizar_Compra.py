import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Caso de Teste 3: Efetuar compra de dois produtos.
'''
Passos:
1 - Realizar login na aplicação com usuário e senha validos;
2 - Escolher Primeiro produto e clicar no botão [Add to cart];
3 - Clicar no botão do carrinha e acessar tela "Your Cart";
4 - Retornar para tela inicial e inserir um novo produto ao carrinho;
5 - Retornar a tela "Your Cart", verificar se segundo produto foi inserido corretamente;
6 - clicar no botão [Checkout];
7 - Inserir informações(Nome, Sobrenome e CEP) na tela "Checkout: Your Information";
8 - Na tela "Checkout: Overview" validar produtos inseridos nos Steps 1 e 4, e clicar no botão [Continue];
9 - Validar se constam produtos corretos;
10 - Clicar no botão [Finish]
11 - Validar mensagem de Sucesso "Thank you for your order!" na tela "Checkout: Complete!"
'''


driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#Realizar login na aplicação com usuário e senha validos;"
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')

#Inserir login e senha
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


# Comando que procura o botão [Checkout] na tela do "Carrinho"
driver.find_element(By.ID, "checkout")
driver.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium checkout_button' and text()='Checkout']").click()


# Tela Checkout: Your Information - 
# Como para inserir informações do cliente(Nome, Sobrenome e CEP)

first_name = driver.find_element(By.ID, 'first-name')
last_name = driver.find_element(By.ID, 'last-name')
postal_code = driver.find_element(By.ID, 'postal-code')

first_name.send_keys('Igor')
last_name.send_keys('Anselmo')
postal_code.send_keys('13.175-667')

#Clicar nos botão [Continue] que será encaminhado para a tela "Checkout: Overview"

driver.find_element(By.XPATH, "//*[@value='Continue']").click()

#Tela - Checkout: Overview
#Valição 01 Checkout: Overview - Verificar se foi acessada a tela "Checkout: Overview"
chk_overview = driver.find_element(By.XPATH, "//*[@class='title' and text()='Checkout: Overview']")
print("Tela que irá exibir produtos que serão comprados:")
print(chk_overview.text)

assert chk_overview.text == "Checkout: Overview"

time.sleep(3)

#Validação 02 Checkout: Overview - Verificar pelo nome dos produtos inseridos para compra, na tela "Checkout: Overview"

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Test.allTheThings() T-Shirt (Red)']").is_displayed()

#Validação 03 Checkout: Overview - 
driver.find_element(By.ID, "finish")
driver.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium cart_button' and text()='Finish']").click()

time.sleep(2)


#Tela - Checkout: Complete!
#Validação 01 - Checkout: Complete! - Verificar se mensagem "Thank you for your order!" esta sendo exibida.

mensagem_sucesso = driver.find_element(By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']")
print("Verificação para mensagem, compra efetuada com sucesso:")
print(mensagem_sucesso.text)

assert mensagem_sucesso.text == "Thank you for your order!"

print("Caso de Teste 3: Efetuar compra de dois produtos, realizado com sucesso!")

time.sleep(3)
