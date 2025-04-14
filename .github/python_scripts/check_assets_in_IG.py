'''This script downloads the latest version of the Ig, adds pages for all new assets using the _new templates. Ammended assets will have their template changed to _new only'''


import xml.etree.ElementTree as ET
from update_IG import import_IG
from update_json import *
import os

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

def getXMLElement(xml_file, element):
    try:
        return xml_file.findall('./{*}'+element)[0].get('value')
    except IndexError:
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
if __name__ == "__main__":
#    import_IG()

    variables = openJSONFile('variables.json')
    ig_folder = variables['ig_folder']
    ig_path = './'+ig_folder
    ig_pages = list_ig_pages(ig_path)
    codesystem_pages = list_ig_pages(ig_path+'/Terminology/CodeSystems')
    valueset_pages = list_ig_pages(ig_path+'/Terminology/ValueSets')


    xml_files, json_files = list_files('../../')
    assets = []
    dict_elements = {'url': 'url', 'name': 'name', 'status': 'status', 'id': 'id'}
    for f in xml_files:
        asset_elements = dict_elements.copy()
        data = openXMLFile(f)
        for key in dict_elements:
            asset_elements[key] = getXMLElement(data, key)
        asset = FHIRAsset(asset_elements['url'], asset_elements['name'], asset_elements['status'], asset_elements['id'], f)
        assets.append(asset)

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
                continue
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
                break
        else:   
            print(f"{asset.id} is not in the IG.")
            #add_asset_to_ig(asset)

    for asset in extensions:
        for page in ig_pages:
            if asset.id in page:
                break
        else:   
            print(f"{asset.id} is not in the IG.")
            #add_asset_to_ig(asset)

    for asset in valuesets:
        for page in valueset_pages:
            if asset.id in page:
                break
        else:   
            print(f"{asset.id} is not in the IG.")
            #add_asset_to_ig(asset)

    for asset in codesystems:
        for page in codesystem_pages:
            if asset.id in page:
                break
        else:   
            print(f"{asset.id} is not in the IG.")

    for asset in examples:
        for page in ig_pages:
            if asset.id.replace('-Example','') in page: #replace is workaround as IG page not the same as the id
                break
        else:   
            print(f"{asset.id} is not in the IG.")
            #add_asset_to_ig(asset)

'''N.B Above does not work if asset has the same name / id as another asset.
This should be fixed, but in mean time need to look in the specific folder '''


