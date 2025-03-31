from fastapi import FastAPI, Query, HTTPException
from services.search import search_by_name, search_by_ans_code, search_by_cnpj
from core.middleware import setup_cors

app = FastAPI()
setup_cors(app)

@app.get("/search/name", summary="Search operators by name")
def search_name(query: str = Query(..., description="Text to match against operator names")):
    results = search_by_name(query)
    return results

@app.get("/search/ans-code", summary="Search operators by ANS code")
def search_ans_code(query: str = Query(..., description="ANS code or partial prefix")):
    results = search_by_ans_code(query)
    return results

@app.get("/search/cnpj", summary="Search operators by CNPJ")
def search_cnpj(query: str = Query(..., description="CNPJ or partial prefix")):
    results = search_by_cnpj(query)
    return results