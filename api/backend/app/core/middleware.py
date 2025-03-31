from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# Permite requisições de qualquer origem (*) apenas para facilitar a integração durante os testes.
# Em produção, recomenda-se restringir os domínios autorizados.
def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
