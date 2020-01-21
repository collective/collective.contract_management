# -*- coding: utf-8 -*-
from collective.contract_management.testing import (  # noqa
    COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING,
)
from datetime import datetime
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


class ContractIcalIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.contracts = api.content.create(
            container=self.portal, type="Contracts", id="contracts", title="Contracts management"
        )
        self.contract1 = api.content.create(
            container=self.contracts,
            type="Contract",
            id="contract1",
            title="Test Contract Ä",
            start=datetime(2020, 1, 15),
            end=datetime(2020, 6, 15),
            notice_period=datetime(2020, 5, 31),
            reminder=u"14",
        )
        self.contract2 = api.content.create(
            container=self.contracts,
            type="Contract",
            id="contract2",
            title="Test Contract B",
            start=datetime(2020, 1, 1),
            end=datetime(2020, 8, 30),
            notice_period=datetime(2020, 7, 30),
            reminder=u"30",
        )
        self.contract_collection = api.content.create(
            type="Collection",
            id="contracts_overview",
            title=u"Contracts",
            container=self.contracts,
        )
        query = [
            {
                "i": "path",
                "o": "plone.app.querystring.operation.string.relativePath",
                "v": "..::1",
            },
            {
                "i": "portal_type",
                "o": "plone.app.querystring.operation.selection.any",
                "v": ["Contract"],
            },
        ]
        self.contract_collection.setQuery(query)

    def test_calendar_from_event(self):
        from collective.contract_management.ical import IICalendar

        cal = IICalendar(self.contract1)
        result = cal.to_ical()
        self.assertIn("SUMMARY:[Contracts management]: Test Contract Ä", result.decode())
        self.assertNotIn("SUMMARY:[Contracts management]: Test Contract B", result.decode())
        self.assertIn("DTSTART;VALUE=DATE:20200615", result.decode())
        self.assertIn("DTEND;VALUE=DATE:20200616", result.decode())
        self.assertIn("TRIGGER:-P29D", result.decode())

    def test_calendar_from_collection(self):
        from collective.contract_management.ical import IICalendar

        cal = IICalendar(self.contract_collection)
        result = cal.to_ical()
        self.assertIn("SUMMARY:[Contracts management]: Test Contract Ä", result.decode())
        self.assertIn("SUMMARY:[Contracts management]: Test Contract B", result.decode())
        self.assertIn("DTSTART;VALUE=DATE:20200615", result.decode())
        self.assertIn("DTSTART;VALUE=DATE:20200830", result.decode())
        self.assertIn("DTEND;VALUE=DATE:20200616", result.decode())
        self.assertIn("TRIGGER:-P29D", result.decode())
        self.assertIn("TRIGGER:-P61D", result.decode())
