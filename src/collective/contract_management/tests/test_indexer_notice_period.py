# -*- coding: utf-8 -*-
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class IndexerIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])


class IndexerFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
