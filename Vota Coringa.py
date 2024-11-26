from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do caminho do ChromeDriver
driver_path = r"C:\Users\Vitor\Desktop\chromedriver-win64\chromedriver.exe"  # Caminho do ChromeDriver

# Configuração do ChromeOptions (se necessário, pode ser deixado vazio)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


# Configuração do serviço para o ChromeDriver
service = Service(driver_path)

# Inicializa o WebDriver para o Chrome
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Acesse o site
    driver.get("https://peb.gg")
    print("Site carregado.")
    
    # Aguarda até que o botão de votação esteja presente e clicável
    wait = WebDriverWait(driver, 15)  # Aguarda até 15 segundos
    aba_votacao = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Home"]/header[1]/div[3]/div/div/a/span')))
    aba_votacao.click()
    print("Aba de votação acessada.")
    time.sleep(3)  # Aguarda o carregamento da aba

    # 2. Selecione a opção de votação desejada
    opcao_voto = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="swiper-wrapper-c4c21641099da37b6"]/div[5]/div[1]/img')))
    opcao_voto.click()
    print("Opção de voto selecionada.")
    time.sleep(2)  # Aguarda a interação

    # 3. Confirme o voto
    botao_confirmar = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="indicacao-publica"]/form/section[1]/div[3]/div/div/div/div[1]/button/span'))
    )
    botao_confirmar.click()
    print("Botão de confirmação de voto clicado.")
    time.sleep(3)  # Aguarda o formulário carregar

    # 4. Preencher o formulário
    nome = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="indicacao-publica"]/form/section[2]/div[1]/div[1]/label/input'))
    )
    nome.send_keys("vitor alves pacheco")

    email = driver.find_element(By.XPATH, '//*[@id="indicacao-publica"]/form/section[2]/div[1]/div[2]/label/input')
    email.send_keys("vitorpacheco02@gmail.com.br")

    telefone = driver.find_element(By.XPATH, '//*[@id="indicacao-publica"]/form/section[2]/div[1]/div[3]/label/input')
    telefone.send_keys("319989487975")
    print("Formulário preenchido com sucesso.")

    # 5. Enviar o formulário
    botao_enviar = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="botao-enviar-formulario"]'))
    )
    botao_enviar.click()
    print("Voto confirmado com sucesso!")

    # Aguarde antes de fechar para visualizar o resultado
    time.sleep(5)

finally:
    # Encerra o navegador
    driver.quit()
