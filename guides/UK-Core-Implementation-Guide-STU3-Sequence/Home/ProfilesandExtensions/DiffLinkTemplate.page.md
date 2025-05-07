<fql output="inline" delimiter=" ">
select
    Link: {
        text: 'Code History for ' + %issue,
        href: 'https://simplifier.net/HL7FHIRUKCoreR4/' + %issue + '/~history'
    }
group by Link
</fql>
