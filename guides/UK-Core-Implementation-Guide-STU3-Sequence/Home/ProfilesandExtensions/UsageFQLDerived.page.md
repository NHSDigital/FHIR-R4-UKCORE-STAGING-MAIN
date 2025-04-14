<fql>
from
	StructureDefinition
select id,baseDefinition,status
  where baseDefinition = %subject
  and status = 'active'
with header
</fql>