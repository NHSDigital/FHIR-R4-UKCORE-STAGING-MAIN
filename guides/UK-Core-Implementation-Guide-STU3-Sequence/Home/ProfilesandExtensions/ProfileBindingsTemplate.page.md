## Bindings (differential)

More information about the bindings to UK Core ValueSets can be found below.

<fql>
    from StructureDefinition
    where url = %subject
    select
    join differential.element.where(binding.strength.exists() and binding.valueSet.exists())
    {
        Context: path,
        Strength: binding.strength,
        Link: binding.valueSet
    }
    order by title
</fql>
