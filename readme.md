# Automação Google Maps – RPA

Este projeto é uma automação em Python que acessa o **Google Maps** e coleta informações sobre estabelecimentos como **restaurantes, academias e sorveterias**.

O objetivo é gerar **arquivos JSON e Excel** com dados organizados e ainda registrar **logs detalhados da execução**.

---

## Funcionalidades

O script faz o seguinte:

 Busca os estabelecimentos no Google Maps usando os termos definidos em `config.py`.
 Coleta dados como:

   Nome do estabelecimento
   Tipo (restaurante, academia ou sorveteria)
   Nota
   Quantidade de avaliações
   Endereço completo
 Salva os resultados em **JSON** e **Excel** (`output/`).
 Cria logs detalhados em **`logs/`** para acompanhar toda a execução.

---

## Dependências

O projeto precisa de **Python 3.12+** e das bibliotecas abaixo:

 selenium
 openpyxl
 logging (já incluso no Python)

Todas as dependências estão listadas no arquivo `requirements.txt`, que facilita a instalação.

---

## Como rodar o projeto

1. Clone o repositório:

```bash
git clone <https://github.com/kaiqueazevedo/projeto_google_maps.git>
cd <projeto_google_maps>
```

2. Crie a virtual environment:

```bash
python3 -m venv venv
```

3. Ative a virtual environment:

```bash
# Linux / Mac
source venv/bin/activate

# Windows CMD
venv\Scripts\activate

# Windows PowerShell
venv\Scripts\Activate.ps1
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a automação:

```bash
python main.py
```

> O script vai abrir o Chrome, fazer as buscas e gerar os arquivos JSON/Excel na pasta `output/` e os logs em `logs/`.

---

## Configurações importantes

Tudo que você precisa alterar está no arquivo `config.py`:

 `BUSCAS`: termos de pesquisa (ex: `"restaurantes"`, `"academias"`).
 `LIMITE_RESULTADOS`: define quantos resultados pegar por pesquisa (use `None` para pegar todos).
 `TEMPO_CARREGAMENTO`: tempo de espera para a página carregar (segundos).
 `TEMPO_ENTRE_ACOES`: tempo de espera entre ações (segundos).
 `ARQUIVO_JSON` e `ARQUIVO_EXCEL`: caminhos dos arquivos de saída.
 `LOG_INFO` e `LOG_AUTOMATION`: caminhos dos arquivos de log.

> O script cria automaticamente as pastas `logs/` e `output/` se elas não existirem, então você não precisa se preocupar.

---

## Estrutura de pastas

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

---

## Observações

 Use **Chrome** como navegador para a automação funcionar corretamente.
 Se for executar em outro computador, não esqueça de ter o **ChromeDriver** compatível instalado.
 A automação é totalmente **portável**, graças aos caminhos relativos no `config.py`.
