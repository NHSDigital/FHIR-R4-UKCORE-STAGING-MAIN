## Extensions

More information about the extensions on the <code>{{variable:issue}}</code> profile can be found using the links below.

<fql>
    from
	StructureDefinition
where
	url = %subject
for differential.element.where(sliceName.exists()).where(type.code='Extension')
 select
	Extension:sliceName,Context:path, Link:type.profile, Comment:short
</fql>