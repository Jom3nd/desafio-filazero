# Desafio Técnico — Estágio Dev/Growth Filazero

Automação desenvolvida como parte da etapa técnica do processo seletivo para **Estágio Dev/Growth — Filazero**.

O projeto realiza o provisionamento de novas unidades a partir de um arquivo CSV, enriquecendo os dados de endereço através da API pública do **ViaCEP**, gerando arquivos JSON com os resultados e disponibilizando testes automatizados para os principais serviços da aplicação.

---

## 📌 Sobre o projeto

A automação simula um processo de provisionamento de unidades de uma rede de clínicas.

O fluxo principal é:

```text
unidades.csv
     ↓
Leitura dos dados
     ↓
Consulta ao ViaCEP
     ↓
Validação e tratamento de erros
     ↓
Geração do slug
     ↓
Processamento das unidades
     ↓
provisionamento.json
     +
relatorio.json
```

Cada unidade é processada individualmente. Caso ocorra algum problema, como CEP inválido ou indisponibilidade da API do ViaCEP, o erro é registrado e o processamento continua para as próximas unidades.

---

## 🛠️ Tecnologias utilizadas

* **Python 3.11**
* **Requests** — comunicação com a API do ViaCEP
* **Python Slugify** — geração de slugs
* **CSV** — leitura dos dados de entrada
* **JSON** — geração dos arquivos de saída
* **Dataclasses** — representação dos dados das unidades
* **Git/GitHub** — versionamento

As dependências externas estão disponíveis em `requirements.txt`.

---

## 📁 Estrutura do projeto

```text
desafio-filazero/
│
├── data/
│   └── unidades.csv
│
├── src/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── exceptions/
│   │   └── ...
│   │
│   ├── models/
│   │   ├── endereco.py
│   │   └── unidade.py
│   │
│   ├── services/
│   │   ├── csv_service.py
│   │   ├── provisionamento_service.py
│   │   └── viacep_service.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_provisionamento.py
│   ├── test_slug.py
│   └── test_viacep.py
│
├── .gitignore
├── requirements.txt
├── run_tests.py
└── README.md
```

### Responsabilidade de cada parte

| Arquivo/Diretório  | Responsabilidade                             |
| ------------------ | -------------------------------------------- |
| `data/`            | Contém os dados de entrada da automação      |
| `src/config/`      | Configurações da aplicação                   |
| `src/models/`      | Modelos utilizados para representar os dados |
| `src/services/`    | Regras de negócio e integrações              |
| `src/exceptions/`  | Exceções específicas da aplicação            |
| `src/main.py`      | Ponto de entrada da aplicação                |
| `tests/`           | Testes dos principais serviços               |
| `run_tests.py`     | Executor dos testes                          |
| `requirements.txt` | Dependências externas                        |

---

# 🚀 Instalação

## Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

* Python 3 instalado
* Git instalado
* conexão com a internet para utilização da API ViaCEP

## 1. Clonar o repositório

```bash
git clone https://github.com/Jom3nd/desafio-filazero.git
```

Entre no diretório:

```bash
cd desafio-filazero
```

---

## 2. Criar um ambiente virtual

É recomendado utilizar um ambiente virtual para manter as dependências do projeto isoladas.

### Windows

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

---

## 3. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

As dependências são:

```text
requests==2.32.4
python-slugify==8.0.4
```

---

# ▶️ Executando a aplicação

A aplicação deve ser executada a partir da **raiz do projeto**.

Utilize:

```bash
python -m src.main
```

### Por que utilizar `-m`?

A aplicação utiliza imports a partir do pacote `src`, por exemplo:

```python
from src.models.unidade import Unidade
```

Por isso, executar o projeto como módulo garante que a raiz do projeto seja utilizada corretamente para os imports.

Evite executar diretamente:

```bash
python src/main.py
```

---

# 📄 Dados de entrada

Os dados utilizados pela automação estão em:

```text
data/unidades.csv
```

O arquivo possui a seguinte estrutura:

```csv
nome,cidade,uf,cep,servicos
Clínica Vida Aracaju,Aracaju,SE,49010-390,"Consulta;Exame;Retorno"
Clínica Vida Salvador,Salvador,BA,40020-000,"Consulta;Exame"
Clínica Vida Recife,Recife,PE,50030-230,"Consulta;Retorno;Vacina"
```

O serviço de leitura interpreta cada linha como uma unidade e separa os serviços utilizando `;`.

---

# 🌐 Integração com ViaCEP

Para cada unidade, o CEP informado no CSV é utilizado para consultar a API pública do ViaCEP:

```text
https://viacep.com.br/ws/{cep}/json/
```

A consulta fornece informações adicionais de endereço, como:

* logradouro;
* bairro;
* cidade;
* uf;
* cep.

A aplicação possui tratamento para situações como:

* CEP inválido;
* CEP não encontrado;
* erro de comunicação;
* indisponibilidade da API;
* resposta inválida.

Quando uma unidade apresenta erro, ela é registrada como falha e o processamento continua para as demais unidades.

---

# 📤 Arquivos de saída

Após a execução, a aplicação gera os resultados no diretório configurado em:

```text
src/config/settings.py
```

## `provisionamento.json`

Contém as unidades processadas com sucesso.

Cada unidade possui:

```json
{
    "unidade": "Clínica Vida Aracaju",
    "endereco": {
        "logradouro": "...",
        "bairro": "...",
        "cidade": "Aracaju",
        "uf": "SE",
        "cep": "49010-390"
    },
    "servicos": [
        "Consulta",
        "Exame",
        "Retorno"
    ],
    "slug": "clinica-vida-aracaju"
}
```

O `slug` é gerado a partir do nome da unidade, removendo acentos e caracteres inadequados e utilizando hífens para separar as palavras.

---

## `relatorio.json`

Contém um resumo do processamento:

```json
{
    "sucesso": 3,
    "falhas": 0,
    "errors": []
}
```

Quando existem falhas, elas são registradas no campo `errors`, permitindo identificar qual unidade apresentou problema e o motivo.

---

# 🖥️ Resumo no terminal

Ao finalizar o processamento, a aplicação apresenta um resumo:

```text
==========RESUMO DO PROVISIONAMENTO==========
Unidades processadas com sucesso: 3
Falhas: 0

Todas as unidades foram processadas com sucesso!
```

Quando existem falhas:

```text
==========RESUMO DO PROVISIONAMENTO==========
Unidades processadas com sucesso: 2
Falhas: 1

Falhas encontradas:
- Clínica Vida Recife: CEP inválido
```

Dessa forma, é possível acompanhar rapidamente o resultado da execução sem precisar abrir os arquivos JSON.

---

# 🧪 Testes

O projeto possui testes automatizados para os principais serviços.

Para manter o projeto simples, não foi utilizado `pytest`. Foi desenvolvido um pequeno executor próprio utilizando os recursos nativos do Python.

Execute os testes com:

```bash
python run_tests.py
```

Os testes abrangem:

* processamento das unidades;
* geração dos slugs;
* integração com o serviço ViaCEP.

O executor apresenta no terminal quais testes foram aprovados ou apresentaram falha.

---

# 🧠 Decisões técnicas

## Separação por serviços

A aplicação foi dividida em serviços com responsabilidades específicas.

Por exemplo:

* `csv_service.py` → leitura dos dados;
* `viacep_service.py` → comunicação com a API;
* `provisionamento_service.py` → coordenação do processo de provisionamento.

Essa separação facilita a manutenção e permite testar cada responsabilidade individualmente.

---

## Tratamento individual de erros

Uma decisão importante foi processar cada unidade individualmente.

Assim, um erro em uma unidade não impede o processamento das demais.

Por exemplo:

```text
Unidade A → sucesso
Unidade B → erro no ViaCEP
Unidade C → sucesso
```

O resultado será:

```text
2 unidades processadas
1 unidade com falha
```

em vez de interromper toda a automação.

---

## Logging

Além do resumo apresentado no terminal, a aplicação possui logging para registrar informações e erros durante a execução.

Os logs são armazenados no diretório configurado pela aplicação e não fazem parte dos arquivos-fonte do projeto.

---

## Imports utilizando `src`

Os módulos são importados a partir da raiz do projeto:

```python
from src.models.unidade import Unidade
from src.services.provisionamento_service import ProvisionamentoService
```

Por esse motivo, a aplicação deve ser executada com:

```bash
python -m src.main
```

a partir da raiz do repositório.

---

# ⚠️ Limitações conhecidas

* A aplicação depende da disponibilidade da API pública do ViaCEP.
* O processamento depende de uma conexão com a internet para consultar os CEPs.
* A entrada é baseada no formato esperado do arquivo `unidades.csv`.
* O projeto foi desenvolvido como uma mini-automação para o desafio e não possui persistência em banco de dados.
* O executor de testes foi desenvolvido especificamente para o tamanho deste projeto e não possui todos os recursos de frameworks de testes como `pytest`.

---

# 🔄 Fluxo completo

De forma resumida, o funcionamento da aplicação é:

```text
                unidades.csv
                     │
                     ▼
              Leitura do CSV
                     │
                     ▼
          Processamento da unidade
                     │
                     ▼
              Consulta ViaCEP
                     │
              ┌──────┴──────┐
              │             │
           Sucesso        Erro
              │             │
              ▼             ▼
       Gera endereço     Registra falha
              │             │
              └──────┬──────┘
                     ▼
               Gera slug
                     │
                     ▼
          Resultado do processamento
                     │
              ┌──────┴──────┐
              ▼             ▼
     provisionamento.json  relatorio.json
```

---

# 📌 Como outra pessoa pode assumir o projeto

Para continuar o desenvolvimento, basta:

1. Clonar o repositório.
2. Criar e ativar o ambiente virtual.
3. Instalar as dependências.
4. Verificar `data/unidades.csv`.
5. Executar `python -m src.main`.
6. Executar `python run_tests.py` para validar as alterações.
7. Consultar `src/services/` para entender as principais regras de negócio.
8. Consultar `src/config/settings.py` caso seja necessário alterar diretórios ou configurações.

As principais regras de negócio estão concentradas nos serviços, enquanto `main.py` funciona como ponto de entrada e apresentação dos resultados.

---

Projeto desenvolvido para o desafio técnico do processo seletivo de **Estágio Dev/Growth — Filazero**.
