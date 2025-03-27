import os
from zipfile import ZipFile, ZIP_DEFLATED

def zip_files(files, output_zip_path):
    """Compacta uma lista de arquivos em um único arquivo .zip"""

    with ZipFile(output_zip_path, 'w', ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=os.path.basename(file))
    print(f"Compression successfully completed: {output_zip_path}")