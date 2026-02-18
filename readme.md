## Automação Google Maps – RPA com Python + Selenium

Este projeto consiste em uma automação RPA desenvolvida em Python que acessa o Google Maps para coletar dados estruturados de estabelecimentos como restaurantes, academias e sorveterias.

O objetivo é gerar arquivos organizados em JSON e Excel, além de manter logs detalhados para rastreabilidade da execução.

### Objetivo

Simular um cenário real de automação para coleta estruturada de dados com foco em:

Inteligência de mercado

Enriquecimento de base de dados

Análise de concorrência

Geração de leads

### Funcionalidades

A automação:

Realiza buscas no Google Maps com base nos termos definidos em config.py

Coleta as seguintes informações:

Nome do estabelecimento

Categoria

Nota

Quantidade de avaliações

Endereço completo

Exporta os dados para:

JSON

Excel (.xlsx)

Gera logs detalhados de execução

Cria automaticamente as pastas logs/ e output/ caso não existam

Permite limitar a quantidade de resultados por busca

#### Tecnologias Utilizadas

Python 3.12+

Selenium

OpenPyXL

Logging (biblioteca padrão do Python)

Todas as dependências estão listadas em requirements.txt.

#### Como Executar
Clone o repositório
git clone https://github.com/kaiqueazevedo/projeto_google_maps.git
cd projeto_google_maps

Crie e ative a virtual environment
python3 -m venv venv


Linux / Mac:

source venv/bin/activate


Windows:

venv\Scripts\activate

Instale as dependências
pip install -r requirements.txt

Execute a automação
python main.py


O navegador Chrome será aberto automaticamente e os arquivos serão gerados nas pastas:

output/

logs/

#### Configurações

As principais configurações estão no arquivo config.py:

BUSCAS → termos de pesquisa

LIMITE_RESULTADOS > quantidade máxima de resultados por busca

TEMPO_CARREGAMENTO > tempo de espera para carregamento da página

TEMPO_ENTRE_ACOES > intervalo entre interações

ARQUIVO_JSON e ARQUIVO_EXCEL > caminhos de saída

LOG_INFO e LOG_AUTOMATION > caminhos de log

#### Estrutura de pastas

organização do projeto:

```
projeto
│
├─ main.py                 # Script principal
├─ utils.py                # Funções auxiliares
├─ config.py               # Configurações
├─ requirements.txt        # Dependências
├─ venv/                   # Virtual environment
├─ logs/                   # Logs gerados
│   ├─ info.log
│   └─ automation.log
└─ output/                 # Arquivos de saída
    ├─ resultados.json
    └─ resultados.xlsx
```

Observações

Necessário ter Google Chrome instalado

ChromeDriver compatível com a versão do navegador

Projeto estruturado com caminhos relativos, permitindo portabilidade




