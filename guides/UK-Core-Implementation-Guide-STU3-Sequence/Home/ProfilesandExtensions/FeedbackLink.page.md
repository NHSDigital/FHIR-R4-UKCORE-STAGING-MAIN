<fql output="inline" delimiter="">
select
    Link: {
        text: 'Report issue for ' + %issue,
        href: 'https://simplifier.net/HL7FHIRUKCoreR4/' + %issue + '/~issues?level=File'
    }
group by Link
</fql>