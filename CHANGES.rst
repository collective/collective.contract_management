Changelog
=========


2.0 (2020-02-17)
----------------

- Allow collectionfilter to work with contentlisting view
  [MrTango]


2.0b8 (2020-02-04)
------------------

- Fix bug in ical export when contract end date was missing
  [MrTango]


2.0b7 (2020-02-04)
------------------

- Fix pdf landscape mode
  [MrTango]


2.0b6 (2020-02-04)
------------------

- Use landscape for pdf export
  [MrTango]


2.0b5 (2020-02-04)
------------------

- Optimize layout of Contracts view table
  [MrTango]

2.0b4 (2020-02-03)
------------------

- Don't implement IEvent, because it breaks the event portlet.
  [MrTango]

- Add PDF-Export view for Contracts and add buttons for PDF and iCal-Export
  [MrTango]


2.0b3 (2020-01-27)
------------------

- only process IContract objects not IEvent objects
  [MrTango]


2.0b2 (2020-01-21)
------------------

- Add uid and url fields to ICS export.
  [MrTango]

- Add summery_prefix to exported event summeries, based on most upper parent Contracts obj.
  [MrTango]


2.0b1 (2020-01-20)
------------------

- Add contracts_ics_view, calendar_from_collection adapter, locales and optimize styling on contract_view


1.0b5 (2020-01-14)
------------------

- Add contract_amount field to Contract and add an index for it
  [MrTango]


1.0b4 (2019-11-26)
------------------

- Allow nested Contracts containers
  [MrTango]

- Make start/end date not required
  [MrTango]

- Fix upgrade steps to not show up in addon control panel
  [MrTango]


1.0b3 (2019-11-21)
------------------

- Add Collection to allowed_content_types for Contracts CT
  [MrTango]

- Add contract_view and locales
  [MrTango]


1.0b2 (2019-11-21)
------------------

- Enable Notice period criteria for Collections
  [MrTango]

- Fix vocabularies
  [MrTango]

- Add indexer for contract_reminder and enable it for Collections
  [MrTango]


1.0b1 (2019-11-21)
------------------

- Initial release.
  [MrTango]
