## Constraints (differential)

More information about the constraints on the <code>{{variable:issue}}</code> profile can be found below.

<fql>
    from StructureDefinition
    where url = %subject
    select differential.element {
    join constraint {
        Key:key,
        Severity:severity,
        Expression:expression,
        Human_Description:human
        }
    }
</fql>