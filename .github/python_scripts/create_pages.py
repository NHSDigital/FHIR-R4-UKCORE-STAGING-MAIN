from check_assets_in_IG import FHIRAsset
import os


def create_Profile_page(asset, path):
    ''' 
    create folder
    create index
    create extensions
    create bindings
    create toc
    '''
    directory_name = path+'/'+asset.id+'TEST'
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
{{{{page:Home/ProfilesandExtensions/ProfileExtensionsTemplate.page.md}}}}

---
''', file=file)

    #create the Bindings page       
    with open(directory_name+"/Bindings.page.md", "x") as file:
        print(f'''
{{{{page:Home/ProfilesandExtensions/ProfileBindingsTemplate.page.md}}}}

---
''', file=file)
        
    #create the TOC page
    with open(directory_name+"/toc.page.md", "x") as file:
        print(f'''- name: Index
  filename: Index.page.md
- name: Extensions
  filename: Extensions.page.md
- name: Bindings
  filename: Bindings.page.md
''', file=file)

    ''' 
    ### Need to work out how to add bindings from extensions to the list, expect format to be: ###
    <table id="addToBindings">
    <tr>
    <td>ServiceRequest.extension:coverage</td>
    <td>extensible</td>
    <td>{{pagelink:ValueSet-UKCore-FundingCategory}}</td>
    </tr>
    </table>
    '''  
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

{{{{page:Home/ProfilesandExtensions/ExtensionTemplate.page.md}}}}
    ''', file=file)
        return  
    except FileExistsError:
        print(f"File '{path}/{asset.id}.page.md' already exists.")
        return  





if __name__ == "__main__":
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
    create_Extension_page(asset, extension_path)