# -*- coding: utf-8 -*-
from collective.contract_management.content.contracts import IContracts  # NOQA E501
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ContractsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_contracts_schema(self):
        fti = queryUtility(IDexterityFTI, name='Contracts')
        schema = fti.lookupSchema()
        self.assertEqual(IContracts, schema)

    def test_ct_contracts_fti(self):
        fti = queryUtility(IDexterityFTI, name='Contracts')
        self.assertTrue(fti)

    def test_ct_contracts_factory(self):
        fti = queryUtility(IDexterityFTI, name='Contracts')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContracts.providedBy(obj),
            u'IContracts not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_contracts_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Contracts',
            id='contracts',
        )

        self.assertTrue(
            IContracts.providedBy(obj),
            u'IContracts not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('contracts', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('contracts', parent.objectIds())

    def test_ct_contracts_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contracts')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_contracts_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contracts')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'contracts_id',
            title='Contracts container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
