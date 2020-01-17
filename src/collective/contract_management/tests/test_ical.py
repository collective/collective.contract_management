# -*- coding: utf-8 -*-
from collective.contract_management.behaviors.contract_event_basic import (
    IContractEventBasicMarker,
)
from collective.contract_management.testing import (
    COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING,
)  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from plone import api
from zope.component import getUtility
from datetime import datetime

import unittest


class ContractIcalIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.contracts = api.content.create(
            container=self.portal, type="Contracts", id="contracts"
        )
        self.contract1 = api.content.create(
            container=self.contracts,
            type="Contract",
            id="contract1",
            title="Test Contract Ä",
            start=datetime(2020, 01, 15),
            end=datetime(2020, 06, 15),
            notice_period=datetime(2020, 05, 31),
            reminder=14,
        )

    def test_calendar_from_event(self):
        from collective.contract_management.ical import IICalendar
        import pdb; pdb.set_trace()  # NOQA: E702
        cal = IICalendar(self.contract1)
        result = cal.to_ical()
        print(result)
        # self.assertEqual(
        #     behavior.marker,
        #     IContractEventBasicMarker,
        # )
