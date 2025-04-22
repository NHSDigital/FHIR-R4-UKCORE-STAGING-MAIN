import json

def openJSONFile(file):
    try:
        with open(file, 'r') as j:
            jsonFile = json.loads(j.read())
    except Exception as e:
        print("\t\tThe code has an error that needs to be fixed before it can be checked:"+ str(e))       
        return {}
    return jsonFile

def getJSONElement(jsonFile, element):
    try:
        return jsonFile[element]
    except KeyError:
        print(f"the element {element} was not found")
        return None
