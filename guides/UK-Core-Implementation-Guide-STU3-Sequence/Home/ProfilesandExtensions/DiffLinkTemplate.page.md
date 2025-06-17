<fql output="inline" delimiter=" ">
select
    Link: {
        text: 'Code History for ' + %topic,
        href: 'https://simplifier.net/HL7FHIRUKCoreR4/' + %topic + '/~history'
    }
group by Link
</fql>
