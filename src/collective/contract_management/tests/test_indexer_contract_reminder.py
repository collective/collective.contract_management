# -*- coding: utf-8 -*-
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING
from datetime import datetime
from datetime import timedelta
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class IndexerIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        today = datetime.today()
        notice_period = today + timedelta(+14)
        self.contracts = api.content.create(
            type='Contracts', container=self.portal, id='contracts'
        )
        self.contracts1 = api.content.create(
            type='Contract',
            container=self.contracts,
            id='contract1',
            notice_period=notice_period,
            reminder='14',
        )

    def test_indexer_contract_reminder(self):
        from ..indexers.contract_reminder import contract_reminder

        expexted_contract_reminder = self.contracts1.notice_period - timedelta(
            int(self.contracts1.reminder)
        )
        delegating_indexer = contract_reminder(self.contracts1)
        self.assertEqual(
            delegating_indexer.callable(delegating_indexer.context),
            expexted_contract_reminder,
        )


class IndexerFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
