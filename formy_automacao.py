from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


#dataframe

df=pd.read_excel("dados_ficticios_formy.xlsx")

#abrindo navegador
navegador=webdriver.Chrome()
navegador.get("https://formy-project.herokuapp.com/form")
# aguardando 2 segundos

time.sleep(1)
#maximizando tela 
navegador.maximize_window()

print(df["Anos de experiencia"].unique())
for indice,linha in df.iterrows():

    #campos
    campo_nome=navegador.find_element("id","first-name")
    campo_sobrenome=navegador.find_element("id","last-name")
    campo_cargo=navegador.find_element("id","job-title")
    high_school=navegador.find_element("id","radio-button-1")
    college=navegador.find_element("id","radio-button-2")
    grad_school=navegador.find_element("id","radio-button-3")
    masculino=navegador.find_element("id","checkbox-1")
    feminino=navegador.find_element("id","checkbox-2")
    outros=navegador.find_element("id","checkbox-3")
    anos_ex=navegador.find_element("id","select-menu")
    campo_data=navegador.find_element("id","datepicker")

    #preenchendo campos
    campo_nome.send_keys(linha["Nome"])
    time.sleep(1)

    campo_sobrenome.send_keys(linha["Sobrenome"])
    time.sleep(1)

    campo_cargo.send_keys(linha["Cargo"])
    time.sleep(1)

    #verificando o grau de escolaridade
    if linha["Escolaridade"]=="High School":
        high_school.click()

    elif linha["Escolaridade"]=="College":
        college.click()

    else:
        grad_school.click()

    time.sleep(1)
    navegador.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
    #verificando o genero

    if linha["Sexo"]=="Female":
        feminino.click()

    elif linha["Sexo"]=="Male":
        masculino.click()

    else:
        outros.click()

    time.sleep(1)

   # verificando anos de experiência
anos_ex.click()

anos = linha["Anos de experiencia"]

if anos == "0-1":
    anos_ex.select_by_visible_text("0-1")

elif anos == "1-2":
    anos_ex.select_by_visible_text("2-4")

elif anos == "2-4":
    anos_ex.select_by_visible_text("2-4")

elif anos == "5-9":
    anos_ex.select_by_visible_text("5-9")

elif anos == "10+":
    anos_ex.select_by_visible_text("10+")

    time.sleep(1)
    #data

    campo_data.click()
    campo_data.send_keys(linha["Data"])



try:
    # seu código de automação

    input("Pressione ENTER para fechar o navegador")

except Exception as erro:
    print("Erro encontrado:", erro)
    input("Pressione ENTER para fechar o navegador")

finally:
    navegador.quit()

navegador.quit()

