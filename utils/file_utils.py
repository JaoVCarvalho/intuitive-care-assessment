import os
from zipfile import ZipFile, ZIP_DEFLATED

def zip_files(files, output_zip_path):
    """Compacta uma lista de arquivos em um único arquivo .zip"""

    if not files:
        print("Not files to compress.")
        return None


    with ZipFile(output_zip_path, 'w', compression=ZIP_DEFLATED) as zipf:
        for file in files:
            try:
                zipf.write(file, arcname=os.path.basename(file))
            except FileNotFoundError:
                print(f"File not found: {file}")
            except PermissionError:
                print(f"No permission to read: {file}")

    print(f"Compression successfully completed: {output_zip_path}")
    return output_zip_path