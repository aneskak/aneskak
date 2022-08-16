from time import sleep
import pyautogui
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://psatotvshml.crm2.dynamics.com/main.aspx?appid=c90f2537-8851-eb11-a812-000d3a8852cb"
imgBotaoDownload = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\botaoDownload.png"
imgRazaoDoStatus = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\razaoDoStatus.png"
imgFiltrarPor = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\filtrarPor.PNG"
imgBusca = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\campoBusca.PNG"
imgGanha = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\ganha.PNG"
imgAcessarAnexo = r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\img\acessar_anexo.PNG"

# TELA DE LOGIN
login_psa = config('LOGIN_PSA')
password_psa = config('PASSWORD_PSA')
browser = webdriver.Chrome(
    executable_path=r"D:\ProgrammingProjects\PythonProjects\automacao_psa_totvs\chromedriver.exe"
)
browser.maximize_window()
browser.get(url)
sleep(2)


# Label username
browser.find_element(By.XPATH, "//input[@id='i0116']").send_keys(login_psa)
# Label password
browser.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
# Button Login
browser.find_element(By.XPATH, "//input[@id='i0118']").send_keys(password_psa)
sleep(2)
# colocar um try exeption para possiveis erros de senha
browser.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
browser.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
sleep(5)



sleep(10)
# APP PSA
# Botão Serviços
browser.find_element(By.XPATH, "//*[@id='areaSwitcherId']/span[2]/span").click()
sleep(10)

browser.find_element_by_css_selector("span[title='Serviços de Projeto']").click()
sleep(10)

browser.find_element_by_xpath("//span[normalize-space()='Cotações']").click()
sleep(5)

browser.find_element_by_xpath("//*[@id='ViewSelector_2_008fbb15-98e9-4c5d-a81a-e685ff8ccc2c']/span/i").click()
browser.find_element_by_xpath("//span[normalize-space()='Todas as Cotações']").click()
sleep(5)

# Filtro de Nome
browser.find_element_by_xpath("//*[@id='entity_control-pcf_grid_control_container']/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/div/div/div[3]/i").click()
browser.find_element_by_xpath("//i[contains(text(),'')]").click()
sleep(5)

campoPesquisa = browser.execute_script("return document.querySelector('.ms-Callout-main form .ms-TextField-wrapper .ms-TextField-fieldGroup input').id")
browser.find_element_by_id(campoPesquisa).send_keys("[ TONIN ] R.A. 200721 RICARDO")
sleep(1)

# Botão Aplicar
browser.find_element(By.CLASS_NAME, "ms-Button--primary").click()
sleep(5)

# Filtrar Status da Proposta
botaoRazaoDoStatus = pyautogui.locateCenterOnScreen(imgRazaoDoStatus)
pyautogui.moveTo(botaoRazaoDoStatus)
sleep(0.5)
pyautogui.click()

browser.find_element(By.XPATH, "//span[normalize-space()='Filtrar por']").click()

pyautogui.moveTo(x=646, y=414, duration=0.5)
pyautogui.click()


pyautogui.moveTo(x=629, y=570)
pyautogui.click()

pyautogui.moveTo(x=646, y=414, duration=0.5)
pyautogui.click()


pyautogui.moveTo(x=770, y=474, duration=0.5)
pyautogui.click()


pyautogui.moveTo(x=365, y=324, duration=0.5)
pyautogui.click()

sleep(5)
browser.find_element(By.XPATH, "//span[contains(text(),'Acessar Anexos')]").click()

sleep(10)
botaoDownload = pyautogui.locateCenterOnScreen(imgBotaoDownload, confidence=0.7)
pyautogui.click(botaoDownload)

sleep(1000)

browser.close()
