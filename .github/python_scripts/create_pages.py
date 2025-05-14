import os
from update_IG import list_ig_pages


def create_Profile_page(asset, path):
    ''' 
    create folder
    create index
    create extensions
    create bindings
    create toc
    '''
    directory_name = path+'/'+asset.id
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
        return
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    # create the index page
    with open(directory_name+"/Index.page.md", "x") as file:
        print(f'''
---
topic: {asset.id}
subject: {asset.url}
usage: {asset.baseDefinition}
issue: {asset.id}
---
              
# StructureDefinition {{{{variable:issue}}}}

<nocheck>
{{{{page:ProfileTemplate_new}}}}
</nocheck>
''', file=file)
    
    #create the Extensions page
    with open(directory_name+"/Extensions.page.md", "x") as file:
        print(f'''
{{{{page:ProfileExtensionsTemplate}}}}

---
''', file=file)

    #create the Bindings page       
    with open(directory_name+"/Bindings.page.md", "x") as file:
        print(f'''
{{{{page:ProfileBindingsTemplate}}}}

---
''', file=file)
        
    #create the Profile TOC page
    with open(directory_name+"/toc.page.md", "x") as file:
        print(f'''- name: Index
  filename: Index.page.md
- name: Extensions
  filename: Extensions.page.md
- name: Bindings
  filename: Bindings.page.md
''', file=file)
    return

def create_Extension_page(asset, path):
    try:
        with open(path+"/"+asset.id+".page.md", "x") as file:
            print(f'''
---
subject: {asset.url}
issue: {asset.id}
---
## StructureDefinition {{{{variable:issue}}}}

<table id="addToTranspose">
<tr><td>Context of Use</td>''', file=file)
                
            for context in asset.context:
                print(f'''<td>{{{{pagelink:UKCore-{context},text:{context}}}}}</td>''', file=file)

            print(f'''</tr>
</table>

{{{{page:ExtensionTemplate_new}}}}
    ''', file=file)
        return  
    except FileExistsError:
        print(f"File '{path}/{asset.id}.page.md' already exists.")
        return  

def create_Terminology_page(asset, path, terminology_type):
    try:
        with open(path+"/"+terminology_type+"-"+asset.id+".page.md", "x") as file:
            print(f'''
---
subject: {asset.url}
issue: {asset.id}
---
## {asset.title}

{{{{page:{terminology_type}Template_new}}}}
    ''', file=file)
        return
    except FileExistsError:
        print(f"File '{path}/{asset.id}.page.md' already exists.")
        return  
    
def create_Example_page(asset, path):
    try:
        with open(path+"/"+asset.id+".page.md", "x") as file:
            print(f'''
---
subject: {asset.id}
---
{{page:ExampleTemplate_new}}
    ''', file=file)
        return
    except FileExistsError:
        print(f"File '{path}/{asset.id}.page.md' already exists.")
        return  

def santise_toc(toc_path):
    ''' Input: toc.yaml
        Output: list of only lines that do not contain UKCore. This is to keep the non-asset pages'''
    with open(toc_path, "r") as f:
        lines = f.readlines()
        filtered_lines = [line for line in lines if 'UK-Core' not in line and 'UKCore' not in line]
        return filtered_lines

def create_toc(path):
    # Find all pages that contain 'ukcore' in their name. This removes all that are currently in the toc, or should be invisible pages
    pages = sorted(page for page in list_ig_pages(path) if "ukcore" in page.lower())
    toc_path = path+"/toc.yaml"
    filtered_lines = santise_toc(toc_path)

    with open(toc_path, "w") as file:
        file.writelines(filtered_lines)
        for page in pages:
            filename = page.split('/')[-1]
            name = filename.split('.')[0]
            print(f'''- name: {name}
  filename: {filename}''', file=file)
    return

def create_profile_toc(path):
    subfolders = sorted([f.name for f in os.scandir(path) if f.is_dir()])
    filtered_lines = santise_toc(toc_path)
    with open(path+"/toc.yaml", "w") as file:
        file.writelines(filtered_lines)
        for subfolder in subfolders:
            print(f'''- name: {subfolder}
  filename: {subfolder}''', file=file)
        return

if __name__ == "__main__":
    from check_assets_in_IG import FHIRAsset, list_ig_pages

    asset = FHIRAsset('https://fhir.hl7.org.uk/StructureDefinition/UKCore-ServiceRequest','ServiceRequest', 'active', 'UKCore-ServiceRequest', 'UKCore-ServiceRequest.xml', 'http://hl7.org/fhir/StructureDefinition/ServiceRequest')

    ig_folder =  "guides/UK-Core-Implementation-Guide-STU3-Sequence"
    ig_path = './'+ig_folder+'/Home'
    
    '''!!!!!!!!! add str path to variables!!!!!!!!!!!!!!'''
    extension_path = ig_path+'/ProfilesandExtensions/ExtensionLibrary'
    profile_path = ig_path+'/ProfilesandExtensions'
    codesystem_path = ig_path+'/Terminology/CodeSystems'
    valueset_path = ig_path+'/Terminology/ValueSets'
    #create_Profile_page(asset, profile_path)
    asset.context = ['Condition', 'Observation']
    #create_Extension_page(asset, extension_path)
    #create_Terminology_page(asset, valueset_path, 'ValueSet')

    #create_toc(codesystem_path)
    #create_profile_toc(profile_path)


    