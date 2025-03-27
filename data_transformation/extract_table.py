from scraping.services.annex_scraper import get_pdf_links, download_pdf, DOWNLOAD_DIR
from data_transformation.services.cleaner import clean_dataframe
from data_transformation.services.mapper import replace_siglas
from utils.file_utils import zip_files
import os
import pdfplumber
import pandas as pd

def get_anexo_i_pdf_path():
    """Verifica se o Anexo I já foi baixado, caso contrário, baixa-o e retorna o caminho."""

    expected_filename = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    local_path = os.path.join(DOWNLOAD_DIR, expected_filename)

    if os.path.exists(local_path):
        return local_path

    pdf_links = get_pdf_links()
    anexo_i_link = next(link for link in pdf_links if "anexo" in link.lower() and "i" in link.lower())
    downloaded = download_pdf([anexo_i_link])
    return downloaded[0]

def extract_tables_from_pdf(pdf_path):
    """Extrai todas as tabelas do PDF do Anexo I."""

    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_tables = page.extract_tables()
            for table in page_tables:
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    tables.append(df)

    return pd.concat(tables, ignore_index=True)

if __name__ == "__main__":

    pdf_path = get_anexo_i_pdf_path()

    df = extract_tables_from_pdf(pdf_path)
    df = clean_dataframe(df)
    df = replace_siglas(df)

    csv_path = "files/rol_de_procedimentos.csv"
    zip_path = "files/Teste_Joao_Victor.zip"

    df.to_csv(csv_path, index=False)
    print("CSV generated successfully!")

    zip_files([csv_path], "files/Teste_Joao_Victor.zip")


