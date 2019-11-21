# -*- coding: utf-8 -*-
from collective.contract_management.content.contract import IContract  # NOQA E501
from collective.contract_management.testing import COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ContractIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Contracts',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_contract_schema(self):
        fti = queryUtility(IDexterityFTI, name='Contract')
        schema = fti.lookupSchema()
        self.assertEqual(IContract, schema)

    def test_ct_contract_fti(self):
        fti = queryUtility(IDexterityFTI, name='Contract')
        self.assertTrue(fti)

    def test_ct_contract_factory(self):
        fti = queryUtility(IDexterityFTI, name='Contract')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContract.providedBy(obj),
            u'IContract not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_contract_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Contract',
            id='contract',
        )

        self.assertTrue(
            IContract.providedBy(obj),
            u'IContract not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('contract', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('contract', parent.objectIds())

    def test_ct_contract_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contract')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_contract_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contract')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'contract_id',
            title='Contract container',
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
