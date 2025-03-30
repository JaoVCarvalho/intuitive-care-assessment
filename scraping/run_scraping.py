from services.scraper_service import get_pdf_links, download_pdf, DOWNLOAD_DIR
from utils.file_utils import zip_files

"""
run_scraping.py
----------------
Script principal para realizar o web scraping dos Anexos I e II da ANS.
Este script:
  - Coleta os links dos PDFs via get_pdf_links()
  - Baixa os arquivos PDF com download_pdf()
  - Compacta todos os PDFs baixados em um arquivo ZIP
  
"""

if __name__ == "__main__":
    try:
        links = get_pdf_links()
        if not links:
            print("No matching PDF files were found.")
        else:
            files = download_pdf(links)
            if not zip_files(files, "files/annexes_bundle.zip"):
                print("Failed to create ZIP file.")
    except Exception as e:
        print("Error in run_scraping.py: ", str(e))


