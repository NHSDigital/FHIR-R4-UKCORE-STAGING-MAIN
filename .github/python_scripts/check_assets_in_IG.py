'''This script downloads the latest version of the Ig, adds pages for all new assets using the _new templates. Ammended assets will have their template changed to _new only'''


import xml.etree.ElementTree as ET
import os

class FHIRAsset:
    def __init__(self, url, title, status, id, filename, baseDefinition):
        self.url = url
        self.title = title
        self.status = status
        self.id = id
        self.filename = filename
        self.baseDefinition = baseDefinition 
        self.context = None

    def __repr__(self):
        return f"FHIRAsset(url={self.url}, name={self.title}, status={self.status}, id={self.id}, filename={self.filename}), baseDefinition={self.baseDefinition})"
    
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

def getXMLElement(xml_file, element, child=0):
    try:
        return xml_file.findall('./{*}'+element)[child].get('value')
    except IndexError:
        return None
    
def get_extension_context_expression(xml_file):
    namespace = {'fhir': 'http://hl7.org/fhir'}
    return [
        expr.get('value')
        for context in xml_file.findall('fhir:context', namespace)
        for expr in context.findall('fhir:expression', namespace)
        if expr is not None and expr.get('value') is not None
    ]
 
def list_files(folder):
    ''' gather a list of xml & json files within a folder. Returns xml_files, json_files '''
    xml_files = []
    json_files = []

    for dirpath, dirnames, filenames in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in ['.git', '.github']]
        
        # Skip files in the root folder, as these arent FHIR assets
        if dirpath == folder:
            continue
        
        for filename in filenames:
            if filename.endswith('.xml'):
                xml_files.append(os.path.join(dirpath, filename))
            elif filename.endswith('.json'):
                json_files.append(os.path.join(dirpath, filename))
    return xml_files, json_files


if __name__ == "__main__":
    from update_IG import import_IG, list_ig_pages
    from update_json import *
    from create_pages import *

    # imoprts IG and returns the ig_folder name
    ig_folder = import_IG()

    '''########### Instead of checking every file, check only in path below. Quicker and more accurate#######'''
    ig_path = './'+ig_folder+'/Home'
    #ig_pages = list_ig_pages(ig_path)
    
    '''!!!!!!!!! add str path to variables.json!!!!!!!!!!!!!!'''
    extension_path = ig_path+'/ProfilesandExtensions/ExtensionLibrary'
    profile_path = ig_path+'/ProfilesandExtensions'
    codesystem_path = ig_path+'/Terminology/CodeSystems'
    valueset_path = ig_path+'/Terminology/ValueSets'
    examples_profile_path = ig_path+'/Examples/Profile-Examples'
    examples_extension_path = ig_path+'/Examples/Extension-Examples'

    codesystem_pages = list_ig_pages(codesystem_path)
    valueset_pages = list_ig_pages(valueset_path)
    profile_pages = list_ig_pages(profile_path)
    extension_pages = list_ig_pages(extension_path)
    example_profile_pages = list_ig_pages(examples_profile_path)
    example_extension_pages = list_ig_pages(examples_extension_path)

    print("Checking assets in IG...")
    xml_files, json_files = list_files('.')
    assets = []
    dict_elements = {'url': 'url', 'title': 'title', 'status': 'status', 'id': 'id', 'baseDefinition': 'baseDefinition'}
    for filename in xml_files:
        asset_elements = dict_elements.copy()
        data = openXMLFile(filename)
        for key in dict_elements:
            asset_elements[key] = getXMLElement(data, key)
        asset = FHIRAsset(
            asset_elements['url'], 
            asset_elements['title'], 
            asset_elements['status'], 
            asset_elements['id'], 
            filename, 
            asset_elements['baseDefinition']
            )
        
        try:
            if 'extension' in asset.url.lower():
                asset.context = get_extension_context_expression(data)
        except:
            pass
        assets.append(asset)
    print(f"Found {len(assets)} assets and examples in the IG.")

    print(f"sorting assets into types...")
    profiles = []
    extensions = []
    valuesets = []
    codesystems = []
    examples = []
    for asset in assets:
        try:
            asset_id = asset.id.lower()
            try:
                asset_url = asset.url.lower()
            except:
                pass

            if 'example' in asset_id:
                examples.append(asset)
                continue
            
            if asset.status != 'active':
                continue
            
            if 'extension' in asset_url:
                extensions.append(asset)
            elif 'structuredefinition' in asset_url:
                profiles.append(asset)
            elif 'valueset' in asset_url:
                valuesets.append(asset)
            elif 'codesystem' in asset_url:
                codesystems.append(asset)
        except Exception as e:
            print(f"Error processing asset {asset}: {e}")

    print(f"assets sorted")

    print(f"Checking assets have a page in the IG...")
    def process_assets(assets, pages, create_fn, path, *extra):
        for asset in assets:
            if not any(asset.id in page for page in pages):
                print(f"{asset.id} is not in the IG.")
                create_fn(asset, path, *extra)
        if 'profile' in create_fn.__name__.lower():
            create_profile_toc(path)
        else:
            create_toc(path)

    # General assets mapping
    asset_fn_map = {
        'profiles':    (profiles, profile_pages, create_Profile_page, profile_path),
        'extensions':  (extensions, extension_pages, create_Extension_page, extension_path),
        'valuesets':   (valuesets, valueset_pages, create_Terminology_page, valueset_path, 'ValueSet'),
        'codesystems': (codesystems, codesystem_pages, create_Terminology_page, codesystem_path, 'CodeSystem'),
    }

    # Process general assets
    for name, data in asset_fn_map.items():
        assets, pages, create_fn, path, *extra = data
        process_assets(assets, pages, create_fn, path, *extra)
    
    # Process examples separately
    for asset in examples:
        asset_id = asset.id.lower()

        if '-sn-' in asset_id:
            continue  # Skip snippet examples

        if 'extension' in asset_id:
            if not any(asset.id in page for page in example_extension_pages):
                print(f"{asset.id} is not in the IG.")
                create_Example_page(asset, examples_extension_path)
        else:
            if not any(asset.id in page for page in example_profile_pages):
                print(f"{asset.id} is not in the IG.")
                create_Example_page(asset, examples_profile_path)

    # Only call TOC builders once per section
    create_toc(examples_extension_path)
    create_toc(examples_profile_path)

    print("Script Complete")
