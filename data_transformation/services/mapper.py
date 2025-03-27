SIGLA_MAP = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

def replace_siglas(df, columns=["OD", "AMB"]):

    for col in columns:
        if col in df.columns:
            df[col] = df[col].replace(SIGLA_MAP)
    return df
