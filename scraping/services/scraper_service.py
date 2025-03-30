import os
import requests
from bs4 import BeautifulSoup

DOWNLOAD_DIR = "files"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links():
    """Coleta os links dos Anexos I e II a partir da página da ANS."""

    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

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
        try:
            filename = os.path.basename(link)
            filepath = os.path.join(DOWNLOAD_DIR, filename)
            # Se o link não for absoluto, prefixa com o domínio base
            if not link.startswith("http"):
                link = f"https://www.gov.br{link}"
            print(f"Downloading: {link}")
            response = requests.get(link)
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                f.write(response.content)
            downloaded_files.append(filepath)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {link}: {e}")
        except IOError as e:
            print(f"Error writing file {filepath}: {e}")

    return downloaded_files