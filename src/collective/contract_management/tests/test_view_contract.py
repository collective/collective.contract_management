# -*- coding: utf-8 -*-
from collective.contract_management.testing import (
    COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING,
    COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING,
)
from collective.contract_management.views.contract_view import IContractView
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from zope.component import getMultiAdapter

import unittest


# from zope.component.interfaces import ComponentLookupError


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.contracts = api.content.create(self.portal, "Contracts", "contracts")
        self.contract1 = api.content.create(self.contracts, "Contract", "contract1")
        self.doc1 = api.content.create(self.portal, "Document", "front-page")

    def test_view_is_registered(self):
        view = getMultiAdapter((self.contract1, self.request), name="view")
        self.assertTrue(view.__name__ == "view")
        self.assertTrue(IContractView.providedBy(view))

    def test_view_not_matching_interface(self):
        # with self.assertRaises(ComponentLookupError):
        #     getMultiAdapter(
        #         (self.portal['front-page'], self.request),
        #         name='view'
        #     )
        view = getMultiAdapter((self.doc1, self.request), name="view")
        self.assertFalse(IContractView.providedBy(view))


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
