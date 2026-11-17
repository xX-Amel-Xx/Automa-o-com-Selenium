
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# dataframe
df = pd.read_excel("dados_ficticios_formy.xlsx")

# abrindo navegador
navegador = webdriver.Chrome()

url = "https://formy-project.herokuapp.com/form"

try:

    navegador.maximize_window()

    print(df["Anos de experiencia"].unique())

    for indice, linha in df.iterrows():

        # abrindo o formulário para cada pessoa
        navegador.get(url)
        time.sleep(2)

        # campos
        campo_nome = navegador.find_element("id", "first-name")
        campo_sobrenome = navegador.find_element("id", "last-name")
        campo_cargo = navegador.find_element("id", "job-title")

        high_school = navegador.find_element("id", "radio-button-1")
        college = navegador.find_element("id", "radio-button-2")
        grad_school = navegador.find_element("id", "radio-button-3")

        masculino = navegador.find_element("id", "checkbox-1")
        feminino = navegador.find_element("id", "checkbox-2")
        outros = navegador.find_element("id", "checkbox-3")

        anos_ex = Select(navegador.find_element("id", "select-menu"))

        campo_data = navegador.find_element("id", "datepicker")

        botao_subimit= navegador.find_element("class name","btn btn-1g btn-primary")

        # preenchendo campos
        campo_nome.send_keys(linha["Nome"])
        campo_sobrenome.send_keys(linha["Sobrenome"])
        campo_cargo.send_keys(linha["Cargo"])

        # verificando escolaridade
        if linha["Escolaridade"] == "High School":
            high_school.click()

        elif linha["Escolaridade"] == "College":
            college.click()

        else:
            grad_school.click()

        # verificando genero
        if linha["Sexo"] == "Female":
            feminino.click()

        elif linha["Sexo"] == "Male":
            masculino.click()

        else:
            outros.click()

        # verificando anos de experiencia
        anos = str(linha["Anos de experiencia"]).strip()

        faixas = {
            "0-1": "0-1",
            "1-2": "2-4",
            "2-4": "2-4",
            "5-9": "5-9",
            "10+": "10+"
        }

        anos_ex.select_by_visible_text(faixas[anos])

        # preenchendo data
        data = pd.to_datetime(
            linha["Data"], dayfirst=True
        ).strftime("%m/%d/%Y")

        campo_data.send_keys(data)

        time.sleep(1)

        # enviando formulario
        botao_subimit.click()

        time.sleep(2)

    input("Pressione ENTER para fechar o navegador")

except Exception as erro:
    print("Erro encontrado:", erro)
    input("Pressione ENTER para fechar o navegador")

finally:
    navegador.quit()
