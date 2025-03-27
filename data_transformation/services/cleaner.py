def clean_dataframe(df):

    df.columns = [col.replace('\n', ' ').strip() for col in df.columns]

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.replace('\n', ' ', regex=False)
            df[col] = df[col].str.strip()

    return df