# Importação de pacotes e modulos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from utils import configurar_logs, salvar_json, gerar_excel_do_json
import config
import time
import logging
import re


# Função extração de quantidade de avaliações
def extrair_numero(texto):
    if not texto:
        return None
    # converte numeros para inteiros
    return int(re.sub(r"\D", "", texto))

# Função para coordenar toda a automação
def main():
    configurar_logs(config.LOG_INFO, config.LOG_AUTOMATION)
    logging.info("Iniciando automação Google Maps")

    # Inicializa o navegador e aumenta a tela com tratativas de erro
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(config.GOOGLE_MAPS_URL)
        time.sleep(5)
    except WebDriverException:
        logging.critical("Falha ao iniciar navegador ou conexão")
        return

    # Procura o campo de busca do Google Maps / Caso não encontre retorna erro e fecha automação
    try:
        campo_busca = browser.find_element(By.ID, "UGojuc")
    except Exception:
        logging.critical("Erro ao localizar campo de busca")
        browser.quit()
        return

    # Lista para armazenar dados coletados
    resultados = []

    # Looping para as buscas
    for estabelecimento in config.BUSCAS:
        logging.info(f"Buscando por: {estabelecimento}")

        campo_busca.clear() # Limpa o campo
        campo_busca.send_keys(estabelecimento) # Escreve no campo
        campo_busca.send_keys(Keys.ENTER) # Pressiona enter

        time.sleep(config.TEMPO_CARREGAMENTO)

        icone_estabelecimentos = browser.find_elements(By.CSS_SELECTOR, "div[role='article'] a.hfpxzc")

        # Se Não encontrar resultado, vai para proxima busca
        if not icone_estabelecimentos:
            logging.warning(f"Nenhum resultado encontrado para {estabelecimento}")
            continue

            # Loop para pesquisas de cada estabelecimento individual
        for icone_estabelecimento in icone_estabelecimentos[:config.LIMITE_RESULTADOS]:
            try:
                # Obtem nome do estabelecimento
                nome = icone_estabelecimento.get_attribute("aria-label")

                #Acesso com clique
                icone_estabelecimento.click()
                time.sleep(config.TEMPO_CARREGAMENTO)

                # coleta dados de avaliação / Tratativa de erro
                try:
                    nota = browser.find_element(By.CSS_SELECTOR, "div.F7nice span").text
                except:
                    nota = None
                    logging.debug("Nota não encontrada")

                # Coleta Quantidade de avaliação / Tratativa de erro
                try:
                    aval_texto = browser.find_element(By.CSS_SELECTOR, "div.F7nice span:last-child").text
                    avaliacoes = extrair_numero(aval_texto)
                except:
                    avaliacoes = None
                    logging.debug("Avaliações não encontradas")

                # Coleta endereço / Tratativa de erro 
                try:
                    endereco = browser.find_element(By.CSS_SELECTOR,"button[data-item-id='address'] div.fontBodyMedium").text
                except:
                    endereco = None
                    logging.debug("Endereço não encontrado")

                # Armazena os dados coletados 
                resultados.append({
                    "nome": nome,
                    "tipo": estabelecimento,
                    "nota": nota,
                    "avaliacoes": avaliacoes,
                    "endereco": endereco
                })

                logging.info(f"Coletado: {nome}")

                browser.back()
                time.sleep(config.TEMPO_ENTRE_ACOES)

            except Exception as e:
                logging.error(f"Erro ao extrair dados do estabelecimento: {e}")
                browser.back()
                time.sleep(config.TEMPO_ENTRE_ACOES)
     # Salva os dados em JSON e Excel
    salvar_json(resultados, config.ARQUIVO_JSON)
    gerar_excel_do_json(config.ARQUIVO_JSON, config.ARQUIVO_EXCEL)

    browser.quit()
    logging.info("Automação finalizada com sucesso")


if __name__ == "__main__":
    main()
