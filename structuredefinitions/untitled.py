'''A Quality Control Checker for the IOPS FHIR repos, which runs whenever there is a push to any branch. 

This checks the following:
- XML code for errors
- Files are in the correct path
- Certain elements are present and have correct vales as per the UK Core requirments
- Draft / Active Profiles are within the CapabilityStatement

If any of these are deemed incorrect the workflow will fail. '''

import xml.etree.ElementTree as ET
import json
import os
import sys

def getRepoVariables():
    '''Returns the repo name in lower case'''
    repoPath = os.getcwd()
    repoParent = os.path.dirname(repoPath)
    repoName = os.path.basename(repoParent).lower()
    
    '''Creates main variables for use with UKCore and NHSE assets'''
    #if 'ukcore' in repoName:
    if 'ukcore' in repoPath.lower(): # USED FOR TESTIMG ____________________DELETE_____________________
        from repoVariables import ukcoreVar as mainVar
    else:
        from repoVariables import nhseVar as mainVar
    return mainVar

def openXMLFile(path,file):        
    try:
        tree = ET.parse("./"+path+"/"+file)
    except ET.ParseError as e:
        print("\t",file,"- The XML code has an error that needs to be fixed before it can be checked:",e)
        error=True
        return None
    except:
        return None
    root = tree.getroot()
    return root

def openJSONFile(path, file):
    ''' loads JSON File returns dict named contents '''
    try:
        with open(f"./{path}/{file}", 'r') as j:
            contents = json.loads(j.read())
    except json.JSONDecodeError as e:
        print(f"\t{file} - The JSON code has an error that needs to be fixed before it can be checked: {e}")
        error = True  # Assuming you handle errors similarly to the XML case
        return None  # Return None to signify error
    except Exception as error:
        print("error found whilst trying to open",file,":",error)
    return contents

def getXMLCoreElements(path,file,warnings):
    '''Gets all elements from the xml file that needs to be checked. Will return empty key value pairs on any retired assets'''
    try:
        if root.findall('.//{*}'+str('status'))[0].get('value') == 'retired':
            elements = {}
            return elements,warnings
    except IndexError:
        warnings.append("\t",file," - The element 'status' is missing")
#    except:
#        print("active",root.findall('.//{*}'+str('status'))[0].get('value'))   

    '''check for missing elements'''
    stop = 0
    elements = {}
    #elements = {'id':'id','url':'url','name':'name','title':'title','version':'version','status':'status','date':'date','description':'description','copyright':'copyright'}
    fileKeys = ['id','url','name','title','version','status','date','description','copyright']
    for k in fileKeys:
        try:
            elements.update({k:root.findall('.//{*}'+str(k))[0].get('value')}) 
        except:
            elements.update({k:None})
            #warnings.append("\t",file," - The element '"+k+"' is missing")
    return elements,warnings
        
def getJSONCoreElements(jsonFile,warnings):
    '''Gets all elements from the json file that needs to be checked. Will return empty on any retired elemets'''
    fileKeys = ['id','url','name','title','version','status','date','description','copyright']
    elements = {}
    try:
        if jsonFile['status']=='retired':
            elements = {}
            return elements,warnings
    except:
        warnings.append("\t",file," - The element 'status' is missing")
    for k in FileKeys:
        try:
            elements.update({k:jsonFile[k]})
        except:
            elements.update({k:None})
            #warnings.append("\t",file," - The element '"+key+"' is missing")
    return elements,warnings

def checkElementNamingConvention(elements, warnings, file):
    fileName = os.path.splitext(os.path.basename(file))[0]
    assets = {"valuesets":"ValueSet","codesystems":"CodeSystem","structuredefinitions":"StructureDefinition"}
    '''check elements naming convention are correct'''
    if elements == {}:
        return warnings
    if path == 'codesystems' or path == 'valuesets':
        fileName = '-'.join(fileName.split('-')[1:])
    if not fileName == elements['id']:
        warnings.append("\t\t"+elements['id']+" - the 'id' is incorrect")
    '''Check all url's unless they starts with one in the ignore list'''
    uriCheck=True
    for elem in mainVar['ignoreURLPrefix']:
        if elements['url'].startswith(elem):
            uriCheck=False
            break
    if uriCheck == True:        
        if not fileName == elements['url'].split('/')[-1]:
            warnings.append("\t\t"+elements['url']+" - The 'url' element is incorrect")
        if not elements['url'].startswith(mainVar['urlPrefix']+assets[path]):
            warnings.append("\t\t"+elements['url']+" - The 'url' element prefix is incorrect")
    if not ''.join(fileName.split('-')) == elements['name'].split('/')[-1]:
        warnings.append("\t\t"+elements['name']+" - The 'name' element is incorrect")
    if not fileName.replace('-','') == elements['title'].replace(' ',''):
        warnings.append("\t\t"+elements['title']+" - The 'title' element is incorrect")
    return warnings
    

def checkXMLStructureDefinitionElements(root,path,warnings):
    ''' Check purpose element is present in Profiles and Extensions '''
    try:
        root.findall('.//{*}'+str('purpose'))[0].get('value')
    except:
        warnings.append("\t\tpurpose - This element is missing'")
    return warnings

def checkJSONStructureDefinitionElements(jsonFile, warnings):
    try:
        jsonFile['purpose']
    except:
        warnings.append("\t\tpurpose - This element is missing'")
    return warnings

def checkContactDetailsXML(root,path,warnings):            
    ''' Check Contact Details '''
    try:
        if not root.findall('.//{*}'+str('name'))[1].get('value') == mainVar['org']:
            warnings.append("\t\t contact.name - This SHALL be '"+mainVar['org']+"'")
    except:
        print("\t\tcontact.name - This element is missing")

    contact = {'system':'email','value':mainVar['email'],'use':'work','rank':'1'}
    for key,value in contact.items():
        try:
            if not root.findall('.//{*}'+str(key))[0].get('value') == value:
                try: 
                    if not root.findall('.//{*}'+str(key))[1].get('value') == value: #added as a workaround in case identifier.system and identifier.value present  
                        warnings.append("\t\t"+"contact.telecom."+key+" - This SHALL be '"+value+"'")
                except:
                    warnings.append("\t\t"+"contact.telecom."+key+" - This SHALL be '"+value+"'")
        except:
            warnings.append("\t\tcontact.telecom."+key+" - This element is missing")
    return warnings

def checkContactDetailsJSON(jsonFile,warnings):
    try:
        if not jsonFile['contact'][0]['name'] == mainVar['org']:
            warnings.append("\t\t contact.name - This SHALL be '"+mainVar['org']+"'")
    except:
        warnings.append("\t\t contact.name - This SHALL be '"+mainVar['org']+"'")
        
    contact = {'system':'email','value':mainVar['email'],'use':'work','rank':'1'}
    for key,value in contact.items():
        try:
            if not jsonFile['contact'][0]['telecom'][0][key] == value:
                warnings.append("\t\tcontact.telecom."+key+" - This SHALL be '"+value+"'")
        except:
            warnings.append("\t\tcontact.telecom."+key+" - This element is missing")
    return warnings

def checkAssets(file, warnings):
    '''Check files are in correct folder '''
    fileName = os.path.splitext(os.path.basename(file))[0]
    if path == 'structuredefinitions':
        if fileName.endswith("Example") or (not file.startswith('Extension') and not file.startswith(mainVar['project'])):
            warnings.append("\t\tThe file has either an incorrect prefix or in the wrong folder '"+path+"'")
            error=True
        if fileName.startswith(mainVar['project']): #Used for Capabilitystatement Checking
            profile = fileName.replace(mainVar['project']+'-','')
            if '-' not in profile: #ignore derived profiles
                currentProfiles.append(profile)
        if file.endswith("xml"):
            warnings = checkXMLStructureDefinitionElements(root,path,warnings)
        else:
            warnings = checkJSONStructureDefinitionElements(jsonFile,warnings)
    if path == 'valuesets' and not file.startswith('ValueSet'):
        warnings.append("\t\tThe file has either an incorrect prefix or in the wrong folder '"+path+"'")
        error=True
    if path == 'codesystems' and not file.startswith('CodeSystem'):
        warnings.append("\t\tThe file has either an incorrect prefix or in the wrong folder '"+path+"'")
        error=True
    return warnings

def checkExamples():
    '''check example filenames'''
    try:
        examplesPath = os.listdir('./examples')
        print('examples')
    except:
        examplesPath = []
    for example in examplesPath:
        fileName = os.path.splitext(example)[0]
        if not fileName.endswith("-Example") :
            error=True
            print("\t",example," - The filename is does not have the suffix '-Example'")
        '''open file to find element values'''
        if example.endswith("xml"):
            root = openXMLFile("examples",example)
            if not root.findall('.//{*}id')[0].get('value') == example.replace('.xml',''):
                error=True
                print("\t",example,"The 'id' element is incorrect")
        elif example.endswith("json"):
            elements = openJSONFile("examples",example)
            if not elements['id'] == fileName:
                print(elements['id'])
                print( example.replace('.xml',''))
                error=True
                print("\t",example,"The 'id' value '"+elements['id']+"' does not match filname '"+fileName+"'")
        else:
            print("\t",example,"The 'file extension' is incorrect")
            
def CheckCapabilityStatementProfiles():
    '''CapabilityStatement Checker - checks if all Profiles are in the CapabilityStatement'''
    root = openXMLFile("CapabilityStatements","CapabilityStatement-"+mainVar['project']+".xml")
    print('CapabilityStatement')
    capabilityStatement = []
    if root != None:
        for tag in root.findall('.//{*}type'):
            capabilityStatement.append(tag.attrib["value"])

        for p in currentProfiles:
            if p not in capabilityStatement:
                error=True
                print("\t",p,"is missing from the CapabilityStatement")

'''Creates an error state, if any of the checks fails it will cause the action to fail'''
error=False
mainVar = getRepoVariables()
currentProfiles = [] #Used for checking against CapabilityStatement

paths = ['structuredefinitions','valuesets','codesystems']

''' Find each file within paths and check for Quality Control. Prints outcome if issues found and sets error to True.'''
for path in paths:
    try:
        files = os.listdir('./'+path)
        print(path)
    except:
        continue
    for file in files:
        warnings = []
        if file.endswith("xml"):
            root = openXMLFile(path,file)
            warnings = checkContactDetailsXML(root,path,warnings)
            elements,warnings = getXMLCoreElements(path,file,warnings)
        elif file.endswith("json"):
            jsonFile = openJSONFile(path,file)
            warnings = checkContactDetailsJSON(jsonFile,warnings)
            elements,warnings = getJSONCoreElements(jsonFile,warnings)
        else:
            print('\t',file,'is neither in xml or json format and has not been checked')
            continue

        warnings = checkAssets(file, warnings)
        warnings = checkElementNamingConvention(elements, warnings, file)    
        if warnings:
            error=True
            print("\t",file)
            for x in warnings:
                print(x)

checkExamples()
CheckCapabilityStatementProfiles()