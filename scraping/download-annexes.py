import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Criar pasta de saída
DOWNLOAD_DIR =  "files"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# URL da página base
BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links():
    """Coleta os links dos Anexos I e II a partir da página da ANS."""

    response = requests.get(BASE_URL)
    # Facilita navegar no HTML (Como se fosse um DOM do navegador). Permitindo buscar por tags, atributos,textos e etc...
    soup = BeautifulSoup(response.text, 'html.parser')

    pdf_links = []

    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text().strip().lower()
        if "anexo i" in text or "anexo ii" in text:
            if href.endswith(".pdf"):
                pdf_links.append(href)

    return pdf_links

def download_pdf(links):
    """Baixa os arquivos PDF dos links informados."""
    downloaded_files = []
    for link in links:
        filename = os.path.basename(link)
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        if not link.startswith("http"):
            link = f"https://www.gov.br{link}"
        print(f"Dowloading: {link}")
        response = requests.get(link)

        with open(filepath, 'wb') as f:
            f.write(response.content)
        downloaded_files.append(filepath)

    return downloaded_files

def zip_pdfs(files):
    """Compacta os PDFs em um arquivo .zip"""
    zip_path = os.path.join(DOWNLOAD_DIR, "annexes_bundle.zip")
    with ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))
    print(f"Compression successfully completed: {zip_path}")

if __name__ == "__main__":
    links = get_pdf_links()
    print(links)

    if not links:
        print("No matching PDF files were found.")
    else:
        files = download_pdf(links)
        print(files)
        zip_pdfs(files)





