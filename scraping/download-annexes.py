from services.annex_scraper import get_pdf_links, download_pdf, DOWNLOAD_DIR
from utils.file_utils import zip_files

if __name__ == "__main__":
    links = get_pdf_links()

    if not links:
        print("No matching PDF files were found.")
    else:
        files = download_pdf(links)
        zip_files(files, "files/annexes_bundle.zip")





