from fastapi import FastAPI, Query
from services.search import search_by_name, search_by_ans_code, search_by_cnpj

app = FastAPI()

@app.get("/search/name", summary="Search operators by name")
def search_name(query: str = Query(..., description="Text to match against operator names")):
    return search_by_name(query)

@app.get("/search/ans-code", summary="Search operators by ANS code")
def search_ans_code(query: str = Query(..., description="ANS code or partial prefix")):
    return search_by_ans_code(query)

@app.get("/search/cnpj", summary="Search operators by CNPJ")
def search_cnpj(query: str = Query(..., description="CNPJ or partial prefix")):
    return search_by_cnpj(query)