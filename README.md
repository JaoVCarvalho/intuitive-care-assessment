# Intuitive Care – Teste de Nivelamento

Este repositório contém a implementação do teste de nivelamento proposto pela **Intuitive Care**, abordando tarefas de **web scraping**, **transformação de dados**, **persistência em banco de dados** e **construção de uma API com interface web**.

## Estrutura do Projeto

```bash
.
├── data_transformation/        # Extração, limpeza e transformação do PDF em CSV
├── database/                   # Scripts SQL para estruturação e consulta dos dados
├── scraping/                   # Web scraping dos anexos I e II
├── api/                        # API FastAPI + Front-end Vue.js
├── utils/                      # Funções utilitárias (como compactação ZIP)
```

---

## Testes Realizados

### 1. Teste de Web Scraping
- Acessa a página da ANS e faz o download dos anexos I e II em PDF.
- Compacta os arquivos em um único `.zip`.

### 2. Teste de Transformação de Dados
- Extrai as tabelas do PDF do Anexo I usando `pdfplumber`.
- Realiza limpeza e substituição de siglas (`OD` e `AMB`).
- Exporta os dados em formato `.csv` e compacta em `.zip`.

### 3. Teste de Banco de Dados
- Criação das tabelas `operators` e `financial_reports`.
- Importação dos dados utilizando `LOAD DATA`.
- Queries analíticas para identificar operadoras com maiores despesas médicas.

### 4. Teste de API
- Criação de servidor FastAPI com rotas de busca por **nome**, **ANS code** e **CNPJ**.
- Integração com interface web desenvolvida com **Vue.js 3 + Vite**.
- Paginação dos resultados.
- Testes das rotas realizados via Postman.

---


## Extras
- O projeto pode ser encontrado em: https://github.com/JaoVCarvalho/intuitive-care-assessment
- Na pasta raiz, utilize `pip install -r requirements.txt` para instalar as dependências do projeto.
- O projeto foi modularizado para garantir **alta coesão** e **baixo acoplamento**.
- Seguiu-se o padrão `conventional commits` para versionamento semântico.
- Código comentado e estruturado com foco em **legibilidade** e **manutenibilidade**.

---

## Observação

Este projeto foi desenvolvido exclusivamente para fins de avaliação técnica, conforme proposto no teste de nivelamento da Intuitive Care. Os dados utilizados são públicos e obtidos de repositórios oficiais da **ANS** (Agência Nacional de Saúde Suplementar).

---

## Contato

João Victor Carvalho dos Santos  
jaovcarvalho1@gmail.com 
https://github.com/JaoVCarvalho
