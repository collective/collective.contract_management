# -*- coding: utf-8 -*-
from collective.contract_management.behaviors.contract_event_basic import IContractEventBasicMarker
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ContractEventBasicIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_contract_event_basic(self):
        behavior = getUtility(IBehavior, 'collective.contract_management.contract_event_basic')
        self.assertEqual(
            behavior.marker,
            IContractEventBasicMarker,
        )
