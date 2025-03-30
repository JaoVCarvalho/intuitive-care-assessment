from data_transformation.services.transformation_service import get_anexo_i_pdf_path, extract_tables_from_pdf, clean_dataframe, replace_siglas
from utils.file_utils import zip_files

if __name__ == "__main__":

    try:
        pdf_path = get_anexo_i_pdf_path()
        if not pdf_path:
            print("PDF not found or failed to download.")
            exit(1)

        df = extract_tables_from_pdf(pdf_path)
        if df.empty:
            print("No tables were extracted from the PDF.")
            exit(1)

        df = clean_dataframe(df)
        df = replace_siglas(df)

        csv_path = "files/rol_de_procedimentos.csv"
        zip_path = "files/Teste_Joao_Victor.zip"

        try:
            df.to_csv(csv_path, index=False)
            print("CSV generated successfully!")
        except Exception as e:
            print("Error generating CSV:", e)

        if not zip_files([csv_path], "files/Teste_Joao_Victor.zip"):
            print("Failed to create ZIP file.")
    except Exception as e:
        print(f"Error in run_transformation: ", str(e))


