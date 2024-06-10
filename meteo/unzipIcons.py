import zipfile
import os

def unzip_file(zip_path, extract_to):
    
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"The zip file {zip_path} does not exist.")
    
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")
        


zip_file_path = 'static/meteo/icons_ipma_weather.zip'
extract_directory = 'static/meteo/'
unzip_file(zip_file_path, extract_directory)
