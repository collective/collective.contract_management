# -*- coding: utf-8 -*-
from collective.contract_management import _
from collective.contract_management.testing import (  # noqa
    COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles, TEST_USER_ID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory, IVocabularyTokenized

import unittest


class RenewalPeriodsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTRACT_MANAGEMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_vocab_renewal_periods(self):
        vocab_name = "collective.contract_management.RenewalPeriods"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(vocabulary.getTerm("3").title, _(u"3 months"))
