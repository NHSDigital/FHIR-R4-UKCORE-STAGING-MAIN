## Mandatory and Must Support Data Elements

The following elements are identified as MustSupport, and it is expected that consumers and suppliers SHALL support these as per the {{pagelink:Guidance-MustSupport}}.

<fql>
from StructureDefinition
where url = %subject
for differential.element.where(mustSupport.exists())
select 
    Element:'<code>' + path + '</code>',
    Reason: short 
</fql>