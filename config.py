import os

# URL de busca
GOOGLE_MAPS_URL = "https://www.google.com/maps"

# O que será incluído nas pesquisas
BUSCAS = ["restaurantes", "academias", "sorveterias"]

# Limite de resultados por pesquisa (use None para pegar todos)
LIMITE_RESULTADOS = 10

# Tempos de espera (segundos)
TEMPO_CARREGAMENTO = 7
TEMPO_ENTRE_ACOES = 3

# Diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pastas de saída
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)

# Arquivos gerados
ARQUIVO_JSON = os.path.join(BASE_DIR, "output", "resultados.json")
ARQUIVO_EXCEL = os.path.join(BASE_DIR, "output", "resultados.xlsx")

# Logs
LOG_INFO = os.path.join(BASE_DIR, "logs", "info.log")
LOG_AUTOMATION = os.path.join(BASE_DIR, "logs", "automation.log")
