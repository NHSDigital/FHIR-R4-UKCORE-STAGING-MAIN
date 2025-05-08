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


    ig_path = './'+ig_folder+'/Home'
    ig_pages = list_ig_pages(ig_path)
    
    '''!!!!!!!!! add str path to variables.json!!!!!!!!!!!!!!'''
    extension_path = ig_path+'/ProfilesandExtensions/ExtensionLibrary'
    profile_path = ig_path+'/ProfilesandExtensions'
    codesystem_path = ig_path+'/Terminology/CodeSystems'
    valueset_path = ig_path+'/Terminology/ValueSets'
    examples_profile_path = ig_path+'/Examples/Profile-Examples'
    examples_extension_path = ig_path+'/Examples/Extension-Examples'

    codesystem_pages = list_ig_pages(codesystem_path)
    valueset_pages = list_ig_pages(valueset_path)


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

    '''
    todo:
    add examples to index page
    check if asset is newly amended
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
    print(examples)

    for asset in profiles:
        for page in ig_pages:
            if asset.id in page:
                break
            else:   
                print(f"{asset.id} is not in the IG.")
                create_Profile_page(asset, profile_path)

    for asset in extensions:
        for page in ig_pages:
            if asset.id in page:
                break
            else:   
                print(f"{asset.id} is not in the IG.")
                create_Extension_page(asset, extension_path)
    create_toc(extension_path)

    for asset in valuesets:
        for page in valueset_pages:
            if asset.id in page:
                break
            else:   
                print(f"{asset.id} is not in the IG.")
                create_Terminology_page(asset, valueset_path, 'ValueSet')
    create_toc(valueset_path)

    for asset in codesystems:
        for page in codesystem_pages:
            if asset.id in page:
                break
            else:   
                create_Terminology_page(asset, codesystem_path, 'CodeSystem')
    create_toc(codesystem_path)

    for asset in examples:
        if 'audit' in asset.id.lower():
            pass
        if '-Sn-' in asset.id: #ignore snippets
            continue
        for page in ig_pages:
            if asset.id in page:
                break
            else:   
                print(f"{asset.id} is not in the IG.")
                if 'extension' in asset.id.lower():
                    create_Example_page(asset, examples_extension_path)
                else:
                    create_Example_page(asset, examples_profile_path)
    create_toc(examples_profile_path)
    create_toc(examples_extension_path)

'''N.B Above does not work if asset has the same name / id as another asset.
This should be fixed, but in mean time the code needs to look in the specific folder '''


