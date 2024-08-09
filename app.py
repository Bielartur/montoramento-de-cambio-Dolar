from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import datetime
from time import sleep

# Salvar nome/link do site escolhido para cotação do Dólar para Real
SITE = 'https://www.xe.com/pt/currencyconverter/convert/?Amount=1&From=USD&To=BRL'

# Configurar Driver
options = ChromeOptions()
options.add_argument('--icognito')
driver = Chrome()

def entrar_no_site():
    # Entrar no site
    driver.get(SITE)
    wait = WebDriverWait(driver, 10)
    sleep(0.3)


def extrair_cotacao():
    # Coletar o valor do Dólar para o dia atual
    cotacao = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]')
    cotacao = cotacao.text
    cotacao = cotacao[:4]
    return cotacao


def reconhecer_data_atual():
    # Salvar a data a qual foi acessado o site
    data_atual = datetime.date.today()
    data_atual = str(data_atual)
    data_atual = data_atual.replace('-', '/')
    return data_atual

entrar_no_site()
cotacao = extrair_cotacao()
data_atual = reconhecer_data_atual()
print(f'A cotação atual é de R$ {cotacao}')
print(f'Data atual: {data_atual}')

# Salvar print do site
# Tornar esses dados em um relatório PDF
