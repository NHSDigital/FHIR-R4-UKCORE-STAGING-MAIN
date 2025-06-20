import requests
from zipfile import ZipFile
import os
import sys
from io import BytesIO
from update_json import openJSONFile
from dotenv import load_dotenv

def import_IG():
    '''imports the latest version of the ig from the url provided and adds it the guides folder'''
    load_dotenv()
    variables = openJSONFile('.github/python_scripts/variables.json')
    ig_url = variables['ig_url']
    ig_folder = variables['ig_folder']
    username = os.getenv("simplifier_username")
    password = os.getenv("simplifier_password")
    
    response = requests.get(ig_url, auth=(username, password))

    if response.status_code == 200:
    # Open the ZIP file in memory
        with ZipFile(BytesIO(response.content)) as zfile:
            ig_files = [
                f for f in zfile.namelist()
                if f.startswith(ig_folder)
            ]

            if ig_files:
                zfile.extractall(members=ig_files)
            else:
                print(f"IG Folder '{ig_folder}' not found in the ZIP file.")
                sys.exit(1)

    else:
        print(f"Failed to download ZIP: {response.status_code} - {response.text}")
        sys.exit(1)

    return ig_folder

def list_ig_pages(path):
    '''returns a list of all the files within a folder'''
    pages = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            pages.append(os.path.join(dirpath, filename).replace('\\', '/'))
    return pages

if __name__ == "__main__":
    import_IG()
