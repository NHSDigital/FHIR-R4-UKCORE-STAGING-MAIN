<fql output="inline" delimiter=" ">
select
    Link: {
        text: 'Report issue for ' + %topic,
        href: 'https://simplifier.net/HL7FHIRUKCoreR4/' + %topic + '/~issues?level=File'
    }
group by Link
</fql>