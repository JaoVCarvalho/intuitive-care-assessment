from scraping.services.scraper_service import get_pdf_links, download_pdf, DOWNLOAD_DIR
import os
import pdfplumber
import pandas as pd

def get_anexo_i_pdf_path():
    """
    Verifica se o Anexo I já foi baixado.
    Caso não esteja presente, realiza o download e retorna o caminho do arquivo.
    """

    expected_filename = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    local_path = os.path.join(DOWNLOAD_DIR, expected_filename)

    if os.path.exists(local_path):
        return local_path

    pdf_links = get_pdf_links()

    try:
        anexo_i_link = next(link for link in pdf_links if "anexo" in link.lower() and "i" in link.lower())
    except StopIteration:
        print("Anexo I not found in the page.")
        return None

    downloaded = download_pdf([anexo_i_link])

    if downloaded:
        return downloaded[0]
    else:
        print("Failed to download Anexo I")
        return None

def extract_tables_from_pdf(pdf_path):
    """Extrai todas as tabelas do PDF do Anexo I."""

    print("Starting extraction of tables from PDF. This may take a few moments...")

    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_tables = page.extract_tables()
            for table in page_tables:
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    tables.append(df)

    if tables:
        print("Extraction completed successfully.")
        return pd.concat(tables, ignore_index=True)
    else:
        print("No tables were found in the PDF.")
        return pd.DataFrame()

def clean_dataframe(df):
    """
       Remove quebras de linha e espaços extras dos nomes das colunas e dos valores de colunas textuais.
    """

    df.columns = [col.replace('\n', ' ').strip() for col in df.columns]

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.replace('\n', ' ', regex=False)
            df[col] = df[col].str.strip()

    return df

SIGLA_MAP = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

def replace_siglas(df, columns=["OD", "AMB"]):
    """
        Substitui as siglas especificadas nas colunas do DataFrame pelos seus significados completos,
        conforme definido em SIGLA_MAP.
    """

    for col in columns:
        if col in df.columns:
            df[col] = df[col].replace(SIGLA_MAP)
    return df

