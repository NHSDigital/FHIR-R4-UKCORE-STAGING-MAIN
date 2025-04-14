import requests
from zipfile import ZipFile
import os
from io import BytesIO
from update_json import openJSONFile

def import_IG():
    '''imports the latest version of the ig from the url provided and adds it the guides folder'''
    variables = openJSONFile('variables.json')
    ig_url = variables['ig_url']
    username = os.getenv("SIMPLIFIER_USERNAME")
    password = os.getenv("SIMPLIFIER_PASSWORD")
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

    else:
        print(f"Failed to download ZIP: {response.status_code} - {response.text}")

    return

if __name__ == "__main__":
    import_IG()
