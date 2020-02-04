# -*- coding: utf-8 -*-
from collective.contract_management.testing import (
    COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING,
    COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from zope.component import getMultiAdapter

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Collection', 'contracts')

    def test_contracts_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['contracts'], self.portal.REQUEST),
            name='contracts-view'
        )
        self.assertTrue(view.__name__ == 'contracts-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in contracts-view'
        # )


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
