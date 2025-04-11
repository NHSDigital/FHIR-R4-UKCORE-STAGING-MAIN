'''This script downloads the latest version of the Ig, adds pages for all new assets using the _new templates. Ammended assets will have their template changed to _new only'''

import requests
from zipfile import ZipFile
import os
from io import BytesIO
import xml.etree.ElementTree as ET
import json

username = os.getenv("SIMPLIFIER_USERNAME")
password = os.getenv("SIMPLIFIER_PASSWORD")


ig_url = 'https://api.simplifier.net/HL7FHIRUKCoreR4/zip'
ig_folder = 'guides/UK-Core-Implementation-Guide-STU3-Sequence/Home'

def import_IG(ig_url, username, password):
    '''imports the latest version of the ig from the url provided and adds it the guides folder'''
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

def list_ig_pages(ig):
    '''returns a list of all resources in the ig'''
    '''needs to have parent folders so we can follow the structure'''
    
    pass

def asset(self, file):
    ''' get info about the asset, inc asset type, id, url, and status. '''

    pass

def check_asset_in_ig(ig, asset):
    '''check if the asset is in the ig'''
    pass

def add_asset_to_ig(ig, asset):
    '''add the asset to the ig'''
    pass

def check_asset_ammended(ig, asset):
    '''check if the asset has been ammended'''
    pass

def update_asset_in_ig(ig, asset):
    '''update the asset in the ig'''
    pass

class FHIRAsset:
    def __init__(self, url, name, status, id, filename):
        self.url = url
        self.name = name
        self.status = status
        self.id = id
        self.filename = filename

    def __repr__(self):
        return f"FHIRAsset(url={self.url}, name={self.name}, status={self.status}, id={self.id}, filename={self.filename})"
    
def openXMLFile(xml_file):        
    try:
        tree = ET.parse(xml_file)
    except Exception as e:
        print("\t\tThe code has an error that needs to be fixed before it can be checked: "+str(e))
        return {}
    root = tree.getroot()
    return root

def openXMLFile(xml_file):        
    try:
        tree = ET.parse(xml_file)
    except Exception as e:
        print("\t\tThe code has an error that needs to be fixed before it can be checked: "+str(e))
        return None
    root = tree.getroot()
    return root


def openJSONFile(file):
    try:
        with open(file, 'r') as j:
            jsonFile = json.loads(j.read())
    except Exception as e:
        print("\t\tThe code has an error that needs to be fixed before it can be checked:"+ str(e))       
        return {}
    return jsonFile


def getXMLElement(xml_file, element):
    try:
        return xml_file.findall('./{*}'+element)[0].get('value')
    except IndexError:
        return None


def getJSONElement(jsonFile, element):
    try:
        return jsonFile[element]
    except KeyError:
        return None
    
def list_files(folder):
    ''' gather a list of xml & json files within a folder. Returns xml_files, json_files '''
    xml_files = []
    json_files = []

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_files.append(os.path.join(dirpath, filename))
            elif filename.endswith('.json'):
                json_files.append(os.path.join(dirpath, filename))
    return xml_files, json_files

def list_ig_pages(path):
    '''returns a list of all the files within a folder'''
    pages = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            pages.append(os.path.join(dirpath, filename))
    return pages




#import_IG(ig_url, 'ryan.may2@nhs.net', 'T1gger22')
ig_path = './'+ig_folder
ig_pages = list_ig_pages(ig_path)


xml_files, json_files = list_files('.')
assets = []
dict_elements = {'url': 'url', 'name': 'name', 'status': 'status', 'id': 'id'}
for f in xml_files:
    asset_elements = dict_elements.copy()
    data = openXMLFile(f)
    for key in dict_elements:
        asset_elements[key] = getXMLElement(data, key)
    asset = FHIRAsset(asset_elements['url'], asset_elements['name'], asset_elements['status'], asset_elements['id'], f)
    assets.append(asset)

print(assets[1].status)


'''all assets are within assets.

todo:
add asset.filename for bug checking
sort assets in Profiles, extensions, etc
check asset in IG
add new page if not in ig
check if asset is newly ammended
create ignore list
'''
profiles = []
extensions = []
valuesets = []
codesystems = []
examples = []
for asset in assets:
    try:
        if 'example' in asset.id.lower():
            examples.append(asset)
        if asset.status != 'active':
            continue
        if 'extension' in asset.url.lower():
            extensions.append(asset)
        elif 'structuredefinition' in asset.url.lower():
            profiles.append(asset)
        elif 'valueset'in asset.url.lower():
            valuesets.append(asset)
        elif 'codesystem' in asset.url.lower():
            codesystems.append(asset)
    except Exception as e:
        print(f"Error processing asset {asset}: {e}")

for asset in profiles:
    for page in ig_pages:
        if asset.id in page:
            print(f"Asset {asset.id} has page {page}.")
            break
    else:   
        print(f"Asset {asset.id} is not in the IG. Adding it now.")
        #add_asset_to_ig(asset)

for asset in extensions:
    for page in ig_pages:
        if asset.id in page:
            print(f"Asset {asset.id} is already in the IG.")
            break
    else:   
        print(f"Asset {asset.id} is not in the IG. Adding it now.")
        #add_asset_to_ig(asset)

for asset in valuesets:
    for page in ig_pages:
        if asset.id in page:
            print(f"Asset {asset.id} has page {page}.")
            break
    else:   
        print(f"Asset {asset.id} is not in the IG. Adding it now.")
        #add_asset_to_ig(asset)

for asset in codesystems:
    for page in ig_pages:
        if asset.id in page:
            print(f"Asset {asset.id} has page {page}.")
            break
    else:   
        print(f"Asset {asset.id} is not in the IG. Adding it now.")
        #add_asset_to_ig(asset)

for asset in examples:
    for page in ig_pages:
        if asset.id in page:
            print(f"Asset {asset.id} has page {page}.")
            break
    else:   
        print(f"Asset {asset.id} is not in the IG. Adding it now.")
        #add_asset_to_ig(asset)

'''N.B Above does not work if asset has the same name / id as another asset.
This should be fixed, but in mean time need to look in the specific folder '''

'''Examples not working dues to naming convention. in Simplifier. Change that first to id'''
