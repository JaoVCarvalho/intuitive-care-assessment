# Intuitive Care Assessment

Este diretório contém os projetos de backend e frontend utilizados no teste técnico.

## Estrutura

```
api/
├── backend/       # Backend Python 3.12 com FastAPI
├── frontend/      # Frontend Vue.js (Vite)
```

---

## Requisitos

- **Python 3.12+**
- **Node.js 22.14+**
- **npm** (Node Package Manager)

Na pasta raiz, utilize `pip install -r requirements.txt` para instalar as dependências do projeto.

---

## Como rodar o Backend (FastAPI)

1. Navegue até a pasta:

```bash
cd backend
cd app
```

2. Execute o servidor:

```bash
uvicorn main:app --reload
```

- O backend estará disponível em:  
   `http://127.0.0.1:8000`

---

## Como rodar o Frontend (Vue.js)

1. Navegue até a pasta:

```bash
cd frontend
```

2. Instale as dependências:

```bash
npm install
```

3. Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

- O frontend estará disponível em:  
  `http://localhost:5173`

---

## Observações

- O frontend se comunica com o backend em `http://localhost:8000`.
- Certifique-se de rodar o **backend antes** de acessar o frontend.
- Caso altere a porta ou a URL da API, atualize a constante `BASE_URL` no arquivo:  
  `frontend/src/services/api.js`.

---

Se tiver dúvidas ou precisar de suporte adicional, sinta-se à vontade para entrar em contato.