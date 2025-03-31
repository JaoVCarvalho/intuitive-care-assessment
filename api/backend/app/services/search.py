from functools import lru_cache
from fastapi import HTTPException
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'relatorio_cadop.csv')

@lru_cache(maxsize=1)
def load_dataframe():
    try:
        df = pd.read_csv(DATA_PATH, sep=";", dtype=str)
        df.rename(columns={
            "Registro_ANS": "ans_code",
            "CNPJ": "cnpj",
            "Razao_Social": "corporate_name",
            "Nome_Fantasia": "trade_name",
            "Modalidade": "modality",
            "Cidade": "city",
            "UF": "state",
            "Endereco_eletronico": "email",
            "Data_Registro_ANS": "ans_registration_date"
        }, inplace=True)
        return df
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="CSV file not found.")
    except pd.errors.ParserError:
        raise HTTPException(status_code=500, detail="Error parsing CSV file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error loading data: {str(e)}")


def serialize_row(row):
    """Serializa uma linha do DataFrame em dicionário JSON, substituindo valores nulos por None."""

    return {
        "ans_code": row["ans_code"],
        "cnpj": row["cnpj"],
        "corporate_name": row["corporate_name"],
        "trade_name": row["trade_name"] if pd.notna(row["trade_name"]) else None,
        "modality": row["modality"] if pd.notna(row["modality"]) else None,
        "city": row["city"] if pd.notna(row["city"]) else None,
        "state": row["state"] if pd.notna(row["state"]) else None,
        "email": row["email"] if pd.notna(row["email"]) else None,
        "ans_registration_date": row["ans_registration_date"]
    }

def search_by_name(query: str):
    """Busca operadores com nome ou nome fantasia que contenham o texto informado (case-insensitive)."""

    df_operators = load_dataframe()
    if df_operators.empty:
        raise HTTPException(status_code=500, detail="Operator dataset is empty.")
    query = query.lower()
    results = df_operators[
        df_operators["corporate_name"].str.lower().str.contains(query, na=False) |
        df_operators["trade_name"].str.lower().str.contains(query, na=False)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]

def search_by_ans_code(query: str):
    """Busca operadores cujo código ANS começa com o prefixo informado."""

    df_operators = load_dataframe()
    if df_operators.empty:
        raise HTTPException(status_code=500, detail="Operator dataset is empty.")
    results = df_operators[
        df_operators["ans_code"].str.startswith(query)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]

def search_by_cnpj(query: str):
    """Busca operadores cujo CNPJ começa com o prefixo informado."""

    df_operators = load_dataframe()
    if df_operators.empty:
        raise HTTPException(status_code=500, detail="Operator dataset is empty.")
    results = df_operators[
        df_operators["cnpj"].str.startswith(query)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]
