---
statusCheck: active
---
<fql  output="inline" delimiter="">
from
	StructureDefinition
where status = %statusCheck and type != 'Extension'
select
	stuff: '< resource>< extension url="http://hl7.org/fhir/tools/StructureDefinition/resource-information">< valueString value="StructureDefinition:resource" />< /extension>< reference>< reference value="StructureDefintion/' + id + '" />< /reference>< name value="' + title + '" />< description value="' + description + '" />< exampleBoolean value="false"/>< /resource>'
</fql>

<fql  output="inline" delimiter="">
from
	StructureDefinition
where status =  %statusCheck and type = 'Extension'
select
	stuff: '< resource>< extension url="http://hl7.org/fhir/tools/StructureDefinition/resource-information">< valueString value="StructureDefinition:extension" />< /extension>< reference>< reference value="StructureDefintion/' + id + '" />< /reference>< name value="' + title + '" />< description value="' + description + '" />< exampleBoolean value="false"/>< /resource>'
</fql>

<fql  output="inline" delimiter="">
  from
	ValueSet
where status =  %statusCheck
select
	stuff: '< resource>< extension url="http://hl7.org/fhir/tools/StructureDefinition/resource-information">< valueString value="ValueSet" />< /extension>< reference>< reference value="ValueSet/' + id + '" />< /reference>< name value="' + title + '" />< description value="' + description + '" />< exampleBoolean value="false"/>< /resource>'
</fql>

<fql  output="inline" delimiter="">
from
	CodeSystem
where status =  %statusCheck
select
 
	stuff: '< resource>< extension url="http://hl7.org/fhir/tools/StructureDefinition/resource-information">< valueString value="CodeSystem" />< /extension>< reference>< reference value="CodeSystem/' + id + '" />< /reference>< name value="' + title + '" />< description value="' + description + '" />< exampleBoolean value="false"/>< /resource>'
</fql>