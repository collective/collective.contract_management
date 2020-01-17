# -*- coding: utf-8 -*-

# from collective.contract_management import _
# from plone.dexterity.browser.view import DefaultView
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IContractView(Interface):
    """
    """


@implementer(IContractView)
class ContractView(BrowserView):

    def __call__(self):
        # Implement your own actions:
        return super(ContractView, self).__call__()
