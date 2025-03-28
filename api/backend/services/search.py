import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'relatorio_cadop.csv')

df_operators = pd.read_csv(DATA_PATH, sep=";", dtype=str)

df_operators.rename(columns={
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

def serialize_row(row):
    """Retorna os campos relevantes como dicionário JSON, tratando valores nulos."""
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
    """Busca por texto na razão social ou nome fantasia (case-insensitive)."""
    query = query.lower()
    results = df_operators[
        df_operators["corporate_name"].str.lower().str.contains(query, na=False) |
        df_operators["trade_name"].str.lower().str.contains(query, na=False)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]

def search_by_ans_code(query: str):
    """Busca pelo código ANS iniciando com o valor fornecido."""
    results = df_operators[
        df_operators["ans_code"].str.startswith(query)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]

def search_by_cnpj(query: str):
    """Busca por CNPJ iniciando com o valor fornecido."""
    results = df_operators[
        df_operators["cnpj"].str.startswith(query)
    ]
    return [serialize_row(row) for _, row in results.iterrows()]
