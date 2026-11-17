from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abrir o navegador
navegador = webdriver.Chrome()

# Acessar o formulário
navegador.get("https://demoqa.com/automation-practice-form")

# Esperar 5 segundos
time.sleep(2)

#Colocar o navegador em tela cheia
navegador.maximize_window()

#selecionar o elemento na tela
campo_name=navegador.find_element("id","firstName")
campo_lastName=navegador.find_element("id","lastName")
campo_email=navegador.find_element("id","userEmail")
campo_numero=navegador.find_element("id","userNumber")
campo_data=navegador.find_element("id","dateOfBirthInput")


#adicionando informações ao formulário
campo_name.send_keys("Amel")
time.sleep(1)
campo_lastName.send_keys("Meire")
time.sleep(1)
campo_email.send_keys("amel@gmail.com")
time.sleep(1)
#selecionando campos
feminino=navegador.find_element("id","gender-radio-1")
feminino.click()
time.sleep(1)

#adicionando número
campo_numero.send_keys("61972364957")
time.sleep(1)

#data
campo_data.click()
campo_data.send_keys(Keys.CONTROL, "a")
campo_data.send_keys("31 Dec 2003")
campo_data.send_keys(Keys.ENTER)
time.sleep(1)

#subject
campo_subject=navegador.find_element("id","subjectsInput")

campo_subject.send_keys("Computer Science")
time.sleep(2)
campo_subject.send_keys(Keys.ENTER)
campo_subject.send_keys("Maths")
time.sleep(2)
campo_subject.send_keys(Keys.ENTER)


time.sleep(2)
navegador.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
#hobbie

time.sleep(1)
campo_hobbie=navegador.find_element("id","hobbies-checkbox-2")
campo_hobbie.click()

#selecionando imagem
time.sleep(2)
campo_imagem=navegador.find_element("id","uploadPicture")
campo_imagem.send_keys("C:/Users/amand/Downloads/ADd.png")

#endereço 

campo_endereco=navegador.find_element("id","currentAddress")
time.sleep(1)
campo_endereco.send_keys("Rua das Acácias, 245, Jardim Primavera, Brasília-DF, CEP 72450-120.")
time.sleep(2)

#campo cidade
campo_estado = navegador.find_element("id", "state")
campo_estado.click()

time.sleep(1)

opcoes = navegador.find_elements("css selector", "#state div[id*='-option-']")

opcoes[1].click()

campo_cidade=navegador.find_element("id","city")
campo_cidade.click()

opcoes = navegador.find_elements("css selector", "#city div[id*='-option-']")
opcoes[2].click()

campo_encerrar=navegador.find_element("id","submit")
campo_encerrar.click()
time.sleep(2)

navegador.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
campo_close=navegador.find_element("id","closeLargeModal")

campo_close.click()

input("Pressione ENTER para fechar o navegador")

navegador.quit()

